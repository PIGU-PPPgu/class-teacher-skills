# Class Teacher Skills

把班主任那些高频、重复、容易漏的工作，整理成一套**能复用、能迁移、能继续接自动化**的 skill 库。

这仓库不是花哨 prompt 展示墙。
它更像一套给班主任工作流打地基的公开包：

- 模板
- 脚本
- skill 文档
- 调用约定
- 主动工作流路线图

## 它现在是什么

**现在：** 班主任数字助理 / 结构化 skill + 模板 + 脚本包  
**下一步：** 接入飞书 / 企业微信 / 钉钉 / cron 后，长成主动工作流系统

## 适合谁

- 班主任
- 年级组长
- 教师助理
- 在做教育 agent / school workflow / 家校沟通产品的人
- 想把“教师经验”整理成可迁移 skill 的人

## 仓库里有什么

### 1) `skills/class-assistant/`
执行型班主任 skill。

覆盖：
- 家长通知起草
- 学生评语 / 寄语
- 班会 / 家长会材料
- 成绩分析
- 考勤统计
- 学生成长跟踪
- 主动工作流路线图

### 2) `skills/class-teacher-market-scan/`
背景扫描 skill。

用于回答：
- 本机现在已经有哪些能力
- 市面上有没有成熟的“班主任 skill”生态
- 当前该怎么定位这套系统
- 下一步最值得做什么

## 三种使用方式

### A. 在支持 skill 的 agent 里直接调用
把仓库链接发给 agent，让它安装 / 加载 `class-assistant`，然后直接下任务。

示例：
- `帮我起草一个明天春游的家长群通知`
- `分析这次月考成绩，找出要重点关注的学生`
- `记录一下今天和小明的谈话，写进学生跟踪`
- `给我准备一份家长会发言提纲`

### B. 当模板库 + 脚本工具包用
即使没有完整 agent 平台，也能直接用：
- `SKILL.md`
- `references/`
- `scripts/`
- `examples/`

### C. 接成主动工作流系统
后续把它接入：
- 飞书
- 企业微信
- 钉钉
- 定时调度器
- 作业 / 考勤 / 校历 / 天气等数据源

到那一步，skill 提供的是：
- 规则
- 模板
- 数据输入输出约定
- 分析逻辑
- 生成逻辑

## 当前真实能力

已经能做：
- 通知 / 评语 / 发言稿生成
- 成绩分析
- 考勤统计
- 学生跟踪记录
- 模板复用
- 脱敏样例演示
- GitHub 可发布结构

还没完全打通：
- 自动定时发群
- 自动读取平台考勤 / 作业系统
- 群消息自动外发闭环
- 无人确认直接发送
- 全自动班主任操作系统

别吹过头。现在是扎实地基，不是全自动神机。

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 看怎么接入
- `HOW_TO_USE_SKILLS.md`
- `skills/class-assistant/README.md`

### 跑脚本
```bash
python skills/class-assistant/scripts/analyze_grades.py --file your_scores.xlsx --output report.md
python skills/class-assistant/scripts/attendance_report.py --file attendance.csv --month 2026-02
python skills/class-assistant/scripts/student_tracker.py list
```

## 仓库结构

```text
.
├── README.md
├── HOW_TO_USE_SKILLS.md
├── requirements.txt
├── class-teacher-feishu-doc.md
└── skills/
    ├── class-assistant/
    └── class-teacher-market-scan/
```

## 安全边界

这个仓库**不应该**包含真实学生隐私数据。

不要提交：
- 成绩明细
- 联系方式
- 家校沟通原文
- 家庭信息
- token / cookie / sessionKey / 平台密钥

默认约定：
- `skills/**/data/` 是本地私有目录
- 可公开内容放在 `references/`、`scripts/`、`examples/`

## 推荐的传播方式

你不需要把这个仓库讲成复杂产品。

最实用的传播方式就一句话：

> 把仓库链接发给你自己的 AI 助手，让它安装 `class-assistant`，然后直接用自然语言帮你处理班主任日常工作。

## 下一步最值钱的方向

如果继续往前做，优先级最高的是这 5 个闭环：

1. 家长群消息润色 + 确认发送
2. 每日 / 每周提醒自动生成
3. 评语平时采集，期末批量生成
4. 作业未交 / 迟到异常提醒
5. 班级日报 / 班务月报自动汇总
