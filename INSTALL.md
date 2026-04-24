# INSTALL

如果你是别的老师，或者你已经有自己的 AI 助手，这个文件就是最短安装入口。

目标不是让人先读半天文档。
目标是：**让 agent 尽快装上、看懂、开始干活。**

## 最推荐的用法

把这个仓库链接发给你的 AI，然后直接说：

> 请安装并加载这个仓库里的 `class-assistant` skill，之后你就作为我的班主任工作助理来用。

仓库链接示例：

```text
https://github.com/PIGU-PPPgu/class-teacher-skills
```

## 给 agent 的最短指令

你可以直接把下面这段发给你的 AI：

```text
请读取这个仓库：https://github.com/PIGU-PPPgu/class-teacher-skills
重点加载 skills/class-assistant/
先阅读：
1. README.md
2. HOW_TO_USE_SKILLS.md
3. skills/class-assistant/SKILL.md
4. skills/class-assistant/README.md
然后按这个 skill 的方式工作，优先帮助我处理：家长通知、评语、成绩分析、考勤统计、学生跟踪、班务提醒。
注意：不要假装你已经接通飞书/钉钉/企业微信自动发送，除非你真的有对应权限和配置。
```

## 如果 agent 支持“安装 skill / 导入 skill”

优先让它读取这些目录和文件：

- `skills/class-assistant/SKILL.md`
- `skills/class-assistant/README.md`
- `skills/class-assistant/references/`
- `skills/class-assistant/scripts/`
- `skills/class-assistant/examples/`

## 如果 agent 不支持正式 skill 机制

那也没关系，直接让它把这里当成知识包 / 模板包使用：

- `SKILL.md`：告诉它这套能力是干什么的
- `references/`：给它模板
- `examples/`：给它输入输出样例
- `scripts/`：给它实际可运行的分析能力

## 本仓库最适合 agent 做的事

### 1. 文案类
- 起草家长群通知
- 润色班务消息
- 生成家长会 / 班会提纲
- 批量生成学生评语

### 2. 分析类
- 分析成绩表
- 汇总考勤异常
- 跟踪重点学生
- 生成班级日报 / 月报初稿

### 3. 规划类
- 根据校历生成提醒
- 根据零散观察整理学生成长记录
- 生成阶段性班务计划

## 现在不要让 agent 吹太满

这仓库**目前不是**全自动班主任系统。

别让 agent 假装它已经能：
- 自动发钉钉群
- 自动发家长微信群
- 自动连考勤系统
- 自动读作业平台
- 无确认直接外发

除非它真的已经配置好这些平台权限。

## 推荐安装后第一句怎么用

安装完以后，直接这样试：

```text
帮我起草一条发给家长群的通知：明天春游，学生穿运动鞋，带水和帽子，中午正常在学校用餐。
```

或者：

```text
我接下来会陆续给你学生表现观察，请你按 class-assistant 的方式帮我积累评语素材，期末统一生成评语。
```

## 给技术型用户的最短本地步骤

```bash
git clone https://github.com/PIGU-PPPgu/class-teacher-skills.git
cd class-teacher-skills
pip install -r requirements.txt
```

然后先看：
- `README.md`
- `HOW_TO_USE_SKILLS.md`
- `skills/class-assistant/README.md`

## 一句话总结

> 这个仓库最适合的传播方式，不是“你来研究代码”。而是“把链接交给你的 AI，让它学会怎么当班主任助理”。
