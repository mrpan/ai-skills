# AI Skills

个人 AI Skills 集合，收录可在智能体中复用的技能。

## Skills

- [bedtime-science-stories](skills/bedtime-science-stories/)：面向 9 岁及以上儿童制作事实准确、容易理解的中文科普介绍，并同步生成 MP3 语音。
- [analyze-primary-math-papers](skills/analyze-primary-math-papers/)：分析拍照上传的小学数学试卷，与用户核对错题后给出有证据的错因分析报告和已确认错题清单。
- [make-primary-math-variant-test](skills/make-primary-math-variant-test/)：根据已确认错题，每题出 2 道变形题，汇总成可打印的测试卷和独立答案卷。
- [prepare-primary-chinese-reading-check](skills/prepare-primary-chinese-reading-check/)：根据当天阅读文章或语文课文，准备适合四年级的 3—5 分钟家庭检验，附家长判读、提示和延迟回顾，计入原有半小时阅读摘抄时间。

## 安装与使用

从上面的列表选一个 Skill，然后把安装请求发给支持 Skills 的智能体。下面以小学语文阅读检验为例。

> 请从 `https://github.com/mrpan/ai-skills` 安装 `skills/prepare-primary-chinese-reading-check/` 这个 Skill。

安装后，在对话中说出 Skill 名称、交代任务并提供所需材料。

> 请使用 `prepare-primary-chinese-reading-check`，根据我发的课文，给四年级孩子准备一次 3—5 分钟的阅读检验。

使用其他 Skill 时，换成对应的目录、名称和任务即可。

## 目录约定

每个 Skill 独立存放在 `skills/<skill-name>/` 目录中，并包含 `SKILL.md` 及其所需的 `agents/`、`references/`、`scripts/`、`assets/` 等资源。
