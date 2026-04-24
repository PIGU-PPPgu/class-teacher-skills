# How to Use These Class-Teacher Skills

这个文档给两类人看：
1. 想直接拿去用的人
2. 想把它接进自己 agent / 自动化系统的人

## 1. 现在仓库里有什么

当前重点是两个 skill：

### `class-assistant`
执行型 skill。

覆盖：
- 家长通知文案
- 评语 / 发言稿
- 成绩分析
- 考勤汇总
- 学生跟踪
- 家长会与班务模板
- 主动工作流路线图

### `class-teacher-market-scan`
说明型 skill。

用于回答：
- 本机有什么相关能力
- 市面上有没有成熟班主任 skill
- 当前系统已经做到哪一步
- 还缺哪些基础设施

## 2. 最简单的调用方式

### 方式 A：直接加载 skill
如果你的 agent 支持本地 skill：

1. 把 skill 放进 skill 库
2. 加载 `class-assistant`
3. 用自然语言直接下任务

示例任务：
- `帮我写一个明天春游的家长通知`
- `分析这次成绩，找出需要重点关注的学生`
- `记录一下今天和李四的谈话`
- `给我出一个家长会提纲`

## 3. 没有 agent 平台时怎么用

即使没有 Hermes，也能用这个仓库。

### 当模板包用
- 读 `skills/class-assistant/SKILL.md`
- 从 `skills/class-assistant/references/` 里拿模板
- 用 `skills/class-assistant/examples/` 看数据格式

### 当脚本包用
运行下面脚本：

```bash
python skills/class-assistant/scripts/analyze_grades.py --file your_scores.xlsx --output report.md
python skills/class-assistant/scripts/attendance_report.py --file attendance.csv --month 2026-02
python skills/class-assistant/scripts/student_tracker.py list
```

## 4. 接入自己的系统时，skill 提供什么

如果你要把它接进飞书 / 钉钉 / 企业微信 / 自己的 agent，建议把 skill 当成四样东西：

1. **规则库**：什么场景该提醒、该分析、该起草
2. **模板库**：通知、评语、家长会、学生记录模板
3. **脚本工具**：成绩分析、考勤汇总、学生跟踪
4. **输入输出约定**：示例数据、目录结构、边界说明

也就是说，skill 不只是 prompt，而是一个结构化工作包。

## 5. 推荐接入架构

建议分三层：

### 第一层：数据层
输入数据例子：
- 成绩表
- 考勤 CSV
- 作业未交名单
- 校历
- 天气信息
- 班级观察记录

### 第二层：决策层
这里调用 `class-assistant` 的：
- 模板
- 规则
- 文案逻辑
- 脚本

### 第三层：执行层
把结果发出去，但建议保留人工确认：
- 飞书消息
- 钉钉消息
- 企业微信消息
- 定时任务 / cron
- 待审核发送

## 6. 当前真实能力 vs 路线图

### 已具备
- 文案生成
- 模板复用
- 成绩分析
- 考勤统计
- 学生跟踪
- 脱敏示例
- GitHub 可发布结构

### 还没完全打通
- 自动定时推群
- 自动读取平台考勤 / 作业系统
- 自动识别群争执
- 全自动闭环发送
- 无人确认直接外发

别把现在包装成已经是完整产品。现在更像一套扎实的地基。

## 7. GitHub 准备与安全规则

公开仓库只建议保留：
- `skills/class-assistant/SKILL.md`
- `skills/class-assistant/README.md`
- `skills/class-assistant/references/`
- `skills/class-assistant/scripts/`
- `skills/class-assistant/examples/`
- `skills/class-teacher-market-scan/`

不要提交：
- `data/` 下真实学生和教师数据
- 联系方式、谈话原文、家庭信息
- token、cookie、sessionKey、平台密钥

## 8. 一句话对外介绍

> 这是一个面向班主任场景的 skill 体系。现在能做通知、分析、记录和模板支持；接入消息平台与调度后，可以升级成真正的主动工作流系统。
