# Class Teacher Skills

这是一套面向班主任 / 教师助手场景的本地 skill 库。

当前重点不是“做一个会聊天的 AI”，而是把班主任高频、重复、容易漏的工作，整理成：
- 可复用模板
- 可运行脚本
- 可解释的工作流说明
- 可继续接平台自动化的能力骨架

## 当前包含

### 1. `skills/class-assistant/`
执行型班主任 skill。

覆盖：
- 家长通知
- 评语 / 发言稿
- 成绩分析
- 考勤统计
- 学生跟踪
- 家长会与班务模板
- 主动工作流路线图

### 2. `skills/class-teacher-market-scan/`
背景扫描 skill。

用于说明：
- 本机已有能力
- 市场上有没有成熟班主任 skill
- 当前系统状态与下一步方向

## 适合谁

- 班主任 / 年级组长 / 教师助手
- 在做教育 agent / school workflow / 家校沟通产品的人
- 想把“教师工作碎片”整理成结构化技能包的人

## 使用方式

### 方式 A：在支持 skill 的 agent 里调用
加载 `class-assistant`，然后直接提任务。

### 方式 B：当模板库 + 脚本工具包用
直接使用：
- `references/`
- `scripts/`
- `examples/`
- `SKILL.md`

更多见：
- `skills/class-assistant/README.md`
- `HOW_TO_USE_SKILLS.md`

## 安全边界

这个仓库**不应**包含真实学生隐私数据。

不要提交：
- 成绩明细
- 联系方式
- 谈话原文
- 家庭信息
- token / cookie / sessionKey / 平台密钥

默认约定：
- `skills/**/data/` 为本地私有目录
- 可公开内容应放在 `references/`、`scripts/`、`examples/`

## 安装依赖

```bash
pip install -r requirements.txt
```

## 下一阶段

下一步不是继续堆 prompt，而是把这套技能接进：
- 飞书
- 钉钉
- 企业微信
- cron / 调度器
- 考勤 / 作业 / 校历 / 天气等数据源

这样它才会从“数字助理”变成“主动工作流系统”。
