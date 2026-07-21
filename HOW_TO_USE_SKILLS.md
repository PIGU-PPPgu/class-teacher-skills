# 如何使用这套班主任技能

> 覆盖家校沟通、学生记录、班务台账、数据汇总与确认后外发工作流。

这个文档给两类人看：
1. **想直接拿去用的老师** — 不需要懂代码，照着抄就行
2. **想把它接进自己系统开发者** — 飞书 / 钉钉 / 企业微信 / 自建 Agent

---

## 📦 仓库里有什么

### 核心技能

| 技能 | 类型 | 干什么的 |
|------|------|----------|
| **class-assistant** | 执行型 | 干活的 — 起草通知、写评语、分析成绩、考勤汇总、学生跟踪 |
| **class-teacher-market-scan** | 说明型 | 摸底的 — 本机有什么能力、市面上有没有现成方案 |

### class-assistant 覆盖 43 个班主任场景

**家校沟通（场景 01-09）**
- 家长群日常通知 / 一对一消息 / 学生评语 / 成绩分析通知
- 家长会提纲 / 周计划 / 谈话记录 / 突发事件报告
- 作业未交汇总

**班务台账（场景 10-25）**
- 班会提纲 / 活动手册 / 值日表 / 日报周报月报
- 请假记录 / 家访记录 / 纪律记录 / 表扬鼓励
- 考试提醒 / 重点学生跟踪 / 家长会后续跟进

**班务管理（场景 26-38）**
- 家校沟通台账 / 作业跟踪台账 / 请假返校跟踪
- 重点学生观察卡 / 班级任务清单 / 周月指标
- 座位编排 / 分组分配 / 班委分配 / 值日轮换
- 同伴互助配对

**进阶场景（场景 39-43）**
- 积分奖惩系统 / 班级编排 / 课题申报书
- 游戏化班级管理 / 智能座位分组

---

## 🚀 快速上手

### 方式 A：你有 Hermes / Claude Code / 任何支持 skill 的 Agent

```bash
# 1. 克隆仓库
git clone https://github.com/PIGU-PPPgu/class-teacher-skills.git

# 2. 把 skills/class-assistant 放进你的 skill 目录
cp -r class-teacher-skills/skills/class-assistant ~/.hermes/skills/

# 3. 直接用自然语言下任务
```

示例任务：
```
帮我写一个明天春游的家长通知
分析这次成绩，找出需要重点关注的学生
记录一下今天和李四的谈话
给我出一个家长会提纲
帮我把这次月考成绩做一个班级分析报告
```

### 方式 B：你没有 Agent 平台，只想用模板和脚本

```bash
git clone https://github.com/PIGU-PPPgu/class-teacher-skills.git
cd class-teacher-skills
```

**当模板包用：**
- 看 `skills/class-assistant/SKILL.md` 了解整体能力
- 从 `skills/class-assistant/references/` 里拿模板（通知模板、家长会指南、学生记录模板、班级日程）
- 用 `skills/class-assistant/examples/` 看数据格式

**当脚本工具用：**

```bash
# 成绩分析
python skills/class-assistant/scripts/analyze_grades.py \
  --file your_scores.xlsx --output report.md

# 考勤汇总
python skills/class-assistant/scripts/attendance_report.py \
  --file attendance.csv --month 2026-02

# 学生跟踪
python skills/class-assistant/scripts/student_tracker.py list
python skills/class-assistant/scripts/student_tracker.py add 张三 --issue 注意力 --desc "上课分心"
python skills/class-assistant/scripts/student_tracker.py report 张三
```

### 方式 C：你想看看某个具体场景怎么用

每个场景目录结构一致，照着改就行：

```
skills/class-assistant/scenarios/01-parent-daily-notice/
├── SCENARIO.md          # 这个场景的说明
├── templates.md         # 模板（可直接复制改）
├── examples/
│   ├── input.sample.md  # 输入示例（脱敏）
│   └── output.sample.md # 输出示例（脱敏）
```

直接看 `examples/` 里的输入输出样例，照着填你的数据就行。

---

## 🔧 接入自己的系统

如果你要把它接进飞书 / 钉钉 / 企业微信 / 自建 Agent，建议分三层：

### 第一层：数据层（输入）
- 成绩表（Excel / CSV）
- 考勤数据（CSV）
- 作业未交名单
- 校历
- 班级观察记录

### 第二层：决策层（skill 调用）
把 `class-assistant` 当成四样东西：
1. **规则库** — 什么场景该提醒、该分析、该起草
2. **模板库** — 通知、评语、家长会、学生记录模板
3. **脚本工具** — 成绩分析、考勤汇总、学生跟踪
4. **输入输出约定** — 示例数据、目录结构、边界说明

### 第三层：执行层（输出 + 人工确认）
- 飞书 / 钉钉 / 企业微信消息
- 定时任务 / cron
- **建议保留人工确认环节**，避免直接外发

---

## ⚠️ 安全规则

### ✅ 可以公开的
- `skills/class-assistant/SKILL.md`
- `skills/class-assistant/README.md`
- `skills/class-assistant/references/`（通用模板）
- `skills/class-assistant/scripts/`（分析脚本）
- `skills/class-assistant/examples/`（脱敏样例）
- `skills/class-assistant/scenarios/`（场景模板）
- `skills/class-teacher-market-scan/`

### ❌ 绝对不能提交的
- `data/` 下的真实学生数据
- 真实姓名、联系方式、家庭信息
- 家校沟通原文
- token、cookie、sessionKey、平台密钥

---

## 📋 当前能力 vs 路线图

### ✅ 已具备
- 43 个场景模板 + 脱敏示例
- 文案生成（通知、评语、发言稿）
- 成绩分析脚本
- 考勤统计脚本
- 学生跟踪脚本
- GitHub 可发布结构

### 🚧 还没完全打通
- 自动定时推群
- 自动读取平台考勤 / 作业系统
- 自动识别群争执
- 全自动闭环发送
- 无人确认直接外发

> 现在更像一套扎实的地基，不是全自动班主任机器人。别吹过头。

---

## 💬 一句话对外介绍

> 面向班主任场景的 AI 技能仓库。覆盖 43 个高频班主任任务，从家长通知到成绩分析，从学生跟踪到班务台账。可以直接当模板用，也可以接入消息平台升级成主动工作流。
