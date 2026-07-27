# Class Teacher Skills（班主任助理 class-assistant）

> 43 个场景 · 班主任 AI 工作台 · 可直接作为 Agent Skill 安装

给班主任用的 AI 技能仓库。不是泛教育 prompt 集，是围绕真实班务拆出来的可复用工作台。

**本仓库根目录本身就是一个标准 Skill（`class-assistant`）**：根目录的 `SKILL.md` 带标准 frontmatter，任何支持 Skill 机制的 Agent（Claude Code、Kimi、Hermes 等）都可以直接把整个仓库当作一个 Skill 加载。

覆盖：
- 家校沟通（通知、评语、家长会）
- 学生记录（谈话、违纪、跟踪、观察）
- 成绩与考勤分析
- 班级日报 / 周报 / 月报
- 台账、跟进表、统计
- 座位编排、分组、班委、值日
- 积分系统、游戏化管理
- 课题申报

## 快速开始

### 方式 A：作为 Agent Skill 安装（推荐）

把仓库链接发给你的 AI，直接说：

> 请安装并加载这个仓库里的 `class-assistant` skill，之后你就作为我的班主任工作助理来用。

```text
https://github.com/PIGU-PPPgu/class-teacher-skills
```

或手动安装：

```bash
git clone https://github.com/PIGU-PPPgu/class-teacher-skills.git
# 仓库根目录就是 skill 目录，直接复制到你的 skills 目录即可
cp -r class-teacher-skills ~/.agents/skills/class-assistant
```

然后直接用自然语言下任务：
- "帮我写一个明天升旗穿校服的家长群通知"
- "帮我把这次月考整理成重点学生分析"
- "给全班 50 人写期末评语"
- "出一版班级周报"

AI 会自动找对应场景的模板和范例。

### 方式 B：当模板包 / 脚本工具用

```bash
git clone https://github.com/PIGU-PPPgu/class-teacher-skills.git
cd class-teacher-skills
pip install -r requirements.txt
```

- 看 `SKILL.md` 了解整体能力
- 从 `references/` 里拿模板（通知模板、家长会指南、学生记录模板、班级日程）
- 用 `examples/` 看数据格式
- 直接跑脚本：

```bash
# 成绩分析
python scripts/analyze_grades.py --file your_scores.xlsx --output report.md

# 考勤汇总
python scripts/attendance_report.py --file attendance.csv --month 2026-02

# 学生跟踪
python scripts/student_tracker.py add 张三 --issue 注意力 --desc "上课分心"
python scripts/student_tracker.py report 张三
```

### 方式 C：只看某个具体场景

每个场景目录结构一致，照着改就行：

```text
scenarios/01-parent-daily-notice/
├── SCENARIO.md          # 这个场景的说明
├── templates.md         # 模板（可直接复制改）
└── examples/
    ├── input.sample.md  # 输入示例（脱敏）
    └── output.sample.md # 输出示例（脱敏）
```

新班级初始化请看 `QUICK_START.md`：给名单就能自动出座位表、分组、值日表等 11 项；加成绩再出 7 项。

## 43 个场景

### A. 家校沟通（1-5）
1. 家长群日常通知 · 2. 一对一家长沟通 · 3. 学生评语 · 4. 成绩分析 · 5. 家长会发言提纲

### B. 班务组织与记录（6-12）
6. 周计划 · 7. 谈话记录 · 8. 突发事件上报 · 9. 作业未交汇总 · 10. 班会提纲 · 11. 活动流程单 · 12. 值日轮值

### C. 班级汇总与跟进（13-25）
13. 日报 · 14. 周报 · 15. 月报 · 16. 请假登记 · 17. 家访记录 · 18. 违纪记录 · 19. 表扬鼓励 · 20. 考试提醒总结 · 21. 重点学生跟踪 · 22. 日度班情 · 23. 周度复盘 · 24. 月度复盘 · 25. 家长会总结跟进

### D. 台账/表格/统计（26-38）
26. 家校沟通台账 · 27. 作业催交跟进 · 28. 请假返校补课 · 29. 重点学生观察卡 · 30. 事务待办 · 31. 周统计 · 32. 月统计 · 33. 座位编排 · 34. 分组编排 · 35. 班干部分配 · 36. 小组分工 · 37. 互助结对 · 38. 轮岗安排

### E. 进阶管理（39-43）
39. 积分量化管理 · 40. 班级编排方案 · 41. 课题申报 · 42. 游戏化管理 · 43. 智能座位编排

完整场景索引见 `SCENARIOS_INDEX.md` 和 `scenarios/INDEX.md`。

## 仓库结构

```text
.
├── SKILL.md                    ← skill 主文档（带 frontmatter，Agent 入口）
├── README.md                   ← 本文件
├── QUICK_START.md              ← 新班级导入指南
├── INSTALL.md                  ← 最短安装入口
├── AGENT_INSTRUCTIONS.md       ← 给第一次读仓库的 AI 的工作指令
├── CONTRIBUTING.md             ← 贡献指南
├── VOICE_ANCHOR.md             ← 输出文字风格规范
├── SCENARIO_STYLE_GUIDE.md     ← 场景文档排版规范
├── SCENARIOS_INDEX.md          ← 43 个场景规划总表
├── scenarios/                  ← 43 个场景目录（SCENARIO.md + templates.md + examples/）
│   └── INDEX.md
├── references/                 ← 可公开模板与流程材料
├── scripts/                    ← 成绩分析 / 考勤汇总 / 学生跟踪脚本
├── examples/                   ← 脱敏样例数据
└── companion/
    └── class-teacher-market-scan/  ← 配套说明型 skill（能力摸底与方案调研笔记）
```

## 接入自己的系统

如果要接进飞书 / 钉钉 / 企业微信 / 自建 Agent，建议分三层：

1. **数据层（输入）**：成绩表、考勤数据、作业未交名单、校历、班级观察记录
2. **决策层（skill 调用）**：把 `class-assistant` 当成规则库 + 模板库 + 脚本工具 + 输入输出约定
3. **执行层（输出 + 人工确认）**：消息平台 / 定时任务，**建议保留人工确认环节**，避免直接外发

## 隐私边界

不提交：真实学生成绩、姓名、电话、家校沟通原文、token / 密钥。`data/` 为本地私有目录，`.gitignore` 已排除。

## 一句话对外介绍

> 面向班主任场景的 AI 技能仓库。覆盖 43 个高频班主任任务，从家长通知到成绩分析，从学生跟踪到班务台账。可以直接当 Skill 装，也可以当模板用，还可以接入消息平台升级成主动工作流。
