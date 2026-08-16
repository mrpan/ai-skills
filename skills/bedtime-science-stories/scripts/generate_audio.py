#!/usr/bin/env python3
"""Generate a Mandarin MP3 from a UTF-8 narration script using edge-tts."""

import argparse
import asyncio
import importlib
import os
import ssl
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="UTF-8 narration text")
    parser.add_argument("output", type=Path, help="Output MP3 path")
    parser.add_argument("--voice", default="zh-CN-XiaoxiaoNeural")
    parser.add_argument("--rate", default="-12%")
    parser.add_argument("--pitch", default="-3Hz")
    parser.add_argument("--volume", default="-3%")
    return parser.parse_args()


async def synthesize(args: argparse.Namespace) -> None:
    try:
        import edge_tts
    except ImportError as exc:
        raise SystemExit("Missing edge-tts. Install it with: python -m pip install edge-tts") from exc

    ca_file = os.environ.get("SSL_CERT_FILE")
    if ca_file:
        communicate_module = importlib.import_module("edge_tts.communicate")
        communicate_module._SSL_CTX = ssl.create_default_context(cafile=ca_file)

    text = args.input.read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("Narration text is empty")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    speech = edge_tts.Communicate(
        text=text,
        voice=args.voice,
        rate=args.rate,
        pitch=args.pitch,
        volume=args.volume,
    )
    await speech.save(str(args.output))
    if not args.output.exists() or args.output.stat().st_size == 0:
        raise SystemExit("Audio generation produced an empty file")


if __name__ == "__main__":
    asyncio.run(synthesize(parse_args()))
