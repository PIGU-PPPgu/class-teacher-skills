# Class Teacher Skills

> 最后更新：2026-04-27 / 当前场景数：34

面向班主任的 AI 技能仓库，不是泛教育 prompt 集，而是围绕真实班务工作拆出来的一套可复用工作台。

它聚焦的不是“聊两句教育”，而是班主任每天反复会遇到的几类事：

- 家校沟通
- 学生记录
- 成绩与考勤分析
- 班级日报 / 周报 / 月报
- 台账、跟进表、清单、统计
- 发送前确认的工作流骨架

## 这是个什么仓库

这套仓库现在已经不是单纯“帮老师写文案”。

它更接近一个 **班主任专属 AI 工作台**，把高频、重复、容易漏的事务拆成可以直接复用的：

- 标准场景
- 固定模板
- 脱敏示例
- 本地脚本
- 面向 agent 的目录结构

一句话说：

> 它是给班主任用的，不是给所有教育场景都硬套的通用仓库。

## 班主任专属特性

### 1. 场景不是泛化的，是班主任高频任务直拆
覆盖重点围绕：
- 家长群通知
- 一对一家长沟通
- 学生评语与观察记录
- 谈话、请假、家访、违纪留痕
- 作业催交、返校补课、重点学生跟踪
- 班级日报 / 周报 / 月报
- 班级事务待办、周统计、月统计

### 2. 不只会写，还强调记录、汇总、跟进
很多“教师助手”最后只剩文案生成。

这套仓库专门补的是班主任真正累的地方：
- 台账
- 表格
- 跟进表
- 周期汇总
- 数据统计
- 后续动作收口

### 3. 默认按真实工作流设计
不是一句 prompt 结束，而是尽量贴近班主任实际流程：

**输入信息 → 生成草稿 → 结构化留痕 → 人工确认 → 再决定是否外发**

### 4. 公开仓库可用，但保留隐私边界
仓库结构默认适合公开发布与二次复用，同时明确避免提交：
- 真实学生隐私
- 家校沟通原文
- 内部敏感记录
- token / cookie / sessionKey / 平台密钥

## 产品入口

如果你只想快速理解这个仓库，按这个顺序看：

1. `README.md`
2. `skills/class-assistant/README.md`
3. `skills/class-assistant/SKILL.md`
4. `skills/class-assistant/scenarios/INDEX.md`
5. `skills/class-assistant/SCENARIOS_INDEX.md`
6. `skills/SCENARIO_STYLE_GUIDE.md`

## 已落地的 34 个标准场景

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
33. 座位编排 / 调座方案
34. 分组编排 / 学习小组分配

## 适合谁用

适合这些人：

- 想把班主任日常事务交给 AI 协助处理的老师
- 想做班主任助手 / 教师助手产品的人
- 想把教育场景拆成 agent-friendly 工作流的人
- 想搭一个“班主任专属”而不是“泛教育空壳”的公开仓库的人

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
