# Class Teacher Skills

给老师一套能直接干活的班主任 skill。

它不是产品说明书，也不是概念秀。
它就是把班主任那些高频、重复、容易漏的工作，整理成可复用的：

- skill
- 模板
- 脚本
- 目录约定
- 后续自动化接口位

## 这仓库能干嘛

现在这套东西，主要解决 5 类事：

- 家长通知起草
- 学生评语 / 寄语整理
- 班会 / 家长会材料准备
- 成绩与考勤分析
- 学生成长跟踪与班务汇总

## 怎么用

### 1. 直接交给你的 AI
把仓库链接发给你的 AI，让它加载 `class-assistant`，然后直接下任务。

例如：
- 帮我写一个明天升旗穿校服的家长群通知
- 分析这次月考，找出重点关注学生
- 记一下今天和小明的谈话，放进学生跟踪
- 给我出一份家长会发言提纲

### 2. 自己拿模板和脚本直接用
你也可以直接看这些内容：
- `skills/class-assistant/SKILL.md`
- `skills/class-assistant/references/`
- `skills/class-assistant/scripts/`
- `skills/class-assistant/examples/`

## 当前状态

已经能用：
- 通知 / 评语 / 发言稿生成
- 成绩分析
- 考勤统计
- 学生跟踪记录
- 模板复用
- 脱敏示例演示

还没完全打通：
- 自动定时发群
- 自动读取平台考勤 / 作业系统
- 群消息自动外发闭环
- 无人确认直接发送
- 全自动班主任操作系统

别吹过头。现在是扎实地基，不是全自动神机。

## 快速开始

```bash
pip install -r requirements.txt
```

看这里：
- `HOW_TO_USE_SKILLS.md`
- `skills/class-assistant/README.md`

跑脚本：

```bash
python skills/class-assistant/scripts/analyze_grades.py --file your_scores.xlsx --output report.md
python skills/class-assistant/scripts/attendance_report.py --file attendance.csv --month 2026-02
python skills/class-assistant/scripts/student_tracker.py list
```

## 安全边界

这个仓库不要放真实学生隐私数据。

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

最实用的一句话：

> 把仓库链接发给你自己的 AI 助手，让它安装 `class-assistant`，然后直接用自然语言帮你处理班主任日常工作。

## 下一步最值钱的方向

优先做这 5 个闭环：

1. 家长群消息润色 + 确认发送
2. 每日 / 每周提醒自动生成
3. 评语平时采集，期末批量生成
4. 作业未交 / 迟到异常提醒
5. 班级日报 / 班务月报自动汇总
