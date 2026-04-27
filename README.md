# Class Teacher Skills

给老师一套能直接干活的班主任 AI skill 仓库。

它不是空泛的“教育 AI 概念”，而是一套围绕班主任高频工作拆出来的：

- 标准场景
- 可复制模板
- 脱敏示例
- 本地脚本
- GitHub 可公开结构

目标很简单：

> 把班主任那些高频、重复、容易漏的工作，整理成 AI 和老师都能直接复用的一套工作台。

## 这套仓库现在是什么

当前这套内容已经不只是“帮老师写几段文案”。

它已经覆盖 3 层能力：

### 1. 沟通表达
- 家长群通知
- 一对一家长沟通
- 学生评语 / 鼓励 / 提醒
- 家长会 / 班会相关材料

### 2. 记录留痕
- 谈话记录
- 请假记录
- 家访记录
- 违纪 / 事件记录
- 重点学生跟踪
- 家校沟通留痕

### 3. 汇总分析与执行
- 成绩分析
- 作业未交汇总
- 值日轮值安排
- 班级日报 / 周报 / 月报
- 家长会会后总结与跟进
- 后续会继续扩充台账 / 表格 / 统计型场景

一句话说：

> 这套东西在往“班主任工作操作台”走，而不是只做一个文案生成器。

## 产品入口

如果你只想快速理解这个仓库，按下面顺序看：

1. `README.md`：仓库级总入口
2. `skills/class-assistant/README.md`：给 AI / agent 的使用入口
3. `skills/class-assistant/SKILL.md`：能力定义与边界
4. `skills/class-assistant/scenarios/INDEX.md`：已落地场景总入口
5. `skills/class-assistant/SCENARIOS_INDEX.md`：完整场景体系与规划
6. `skills/SCENARIO_STYLE_GUIDE.md`：统一写法规范

## 已落地的 32 个标准场景

### A. 家校沟通
1. 家长群日常通知
2. 一对一家长沟通
3. 学生期末评语 / 阶段评语
4. 成绩分析结论输出
5. 家长会发言提纲

### B. 班务组织与记录
6. 班级周计划 / 班务提醒
7. 谈话记录
8. 突发事件上报 / 情况说明
9. 作业未交 / 迟交汇总
10. 班会提纲
11. 活动流程单
12. 值日 / 轮值安排

### C. 班级汇总与跟进
13. 班级日报
14. 班级周报
15. 班级月报
16. 请假登记 / 请假说明
17. 家访记录
18. 违纪记录
19. 表扬 / 鼓励记录
20. 考试前提醒与复习总结
21. 重点学生跟踪清单
22. 日度班情简报
23. 周度班情复盘
24. 月度班情复盘
25. 家长会总结与后续跟进

### D. 台账 / 表格 / 统计执行场景
26. 家校沟通台账
27. 作业催交跟进表
28. 请假返校补课跟进表
29. 重点学生阶段观察卡
30. 班级事务待办清单
31. 班级数据周统计
32. 班级数据月统计

> 注：13-15 与 22-24 分别对应“标准汇总场景”和“更偏内部管理/复盘表达的场景拆分”，后续会继续收敛命名与映射。

## 适合谁用

适合这些人：

- 自己就会用 AI 的班主任
- 想给老师部署一套本地 skill 的技术人员
- 想做教师助手 / 班主任工作流产品的人
- 想把教育场景拆成 agent-friendly 目录结构的人

## 仓库怎么用

### 用法 1：直接交给 AI
把仓库链接发给你的 AI，让它优先读取：

- `skills/class-assistant/README.md`
- `skills/class-assistant/SKILL.md`
- `skills/class-assistant/scenarios/INDEX.md`

然后直接下任务，比如：

- 帮我写一个明天升旗穿校服的家长群通知
- 帮我把这次月考整理成重点学生分析
- 记一下今天和小明的谈话，加入学生跟踪
- 给我出一版班级日报
- 给我做一份家长会总结和后续跟进清单

### 用法 2：按场景直接进入
如果你知道自己要做什么，可以直接进：

- `skills/class-assistant/scenarios/`
- `skills/class-assistant/scenarios/INDEX.md`
- `PRODUCT_OVERVIEW.md`
- `EXECUTION_SCENARIOS.md`

每个场景目录通常包含：

- `README.md`
- `SCENARIO.md`
- `templates.md`
- `examples/`
- `scripts/`（如果该场景需要）

### 用法 3：直接跑脚本
当前已有脚本：

```bash
python skills/class-assistant/scripts/analyze_grades.py --file your_scores.xlsx --output report.md
python skills/class-assistant/scripts/attendance_report.py --file attendance.csv --month 2026-02
python skills/class-assistant/scripts/student_tracker.py list
```

## 仓库结构

```text
.
├── README.md
├── CONTRIBUTING.md
├── HOW_TO_USE_SKILLS.md
├── skills/
│   ├── SCENARIO_STYLE_GUIDE.md
│   └── class-assistant/
│       ├── README.md
│       ├── SKILL.md
│       ├── SCENARIOS_INDEX.md
│       ├── references/
│       ├── scripts/
│       └── scenarios/
```

## 公开仓库边界

这个仓库默认按“可公开发布”设计。

不要提交：
- 真实学生成绩
- 真实姓名、电话、家庭信息
- 家校沟通原文
- 教师内部敏感记录
- token / cookie / sessionKey / 平台密钥
- 本地私有 `data/` 目录内容

`.gitignore` 已默认排除大部分本地私有与杂项文件。

## 推荐的 GitHub 展示文案

### About
AI skill repository for class teachers: parent communication, student records, grade analysis, class reports, and execution-oriented school workflows.

### Topics
- ai-agent
- teacher-assistant
- class-teacher
- education
- workflow
- prompt-engineering
- automation
- school-operations

## 下一步最值钱的方向

优先继续做这几类闭环：

1. 台账 / 表格 / 统计型场景
2. 成绩、考勤、作业、谈话记录的结构化流转
3. 班级日报 / 周报 / 月报自动汇总
4. 发送前确认式外发闭环
5. 后续接飞书 / 企业微信 / 定时任务骨架

## 一句话介绍

> 把仓库链接发给你自己的 AI 助手，让它安装 `class-assistant`，然后直接帮你处理班主任日常工作。
