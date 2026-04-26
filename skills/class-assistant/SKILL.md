---
name: class-assistant
description: 给老师直接干活的班主任 skill。用于通知、评语、成绩分析、考勤汇总、学生跟踪、班务材料整理，并为后续提醒与自动化闭环预留接口。
---

# 班主任助理

给老师直接干活的班主任 skill。

它主要处理这些事：
- 家长通知起草
- 学生评语 / 寄语整理
- 班会 / 家长会材料准备
- 成绩分析
- 考勤汇总
- 学生成长跟踪
- 班务阶段总结

## 怎么用

### 1. 直接给任务
常见说法：
- 帮我起草一个关于明天升旗穿校服的家长群通知
- 为小明写一段期末评语，优点是积极、热心，缺点是上课容易分心
- 分析这次月考，找出重点关注学生和进步最大的学生
- 记录一下今天和小红的谈话，放进学生跟踪
- 给我整理一份下周家长会发言提纲

### 2. 有结构化数据就跑脚本

成绩分析：
```bash
python scripts/analyze_grades.py --file 成绩表.xlsx --output 分析报告.md
```

考勤汇总：
```bash
python scripts/attendance_report.py --file 考勤数据.csv --month 2026-02
```

学生跟踪：
```bash
python scripts/student_tracker.py add 学生姓名 --issue 问题类型 --desc 情况描述
python scripts/student_tracker.py update 学生姓名 --note 新进展 --type 谈话记录
python scripts/student_tracker.py report 学生姓名
python scripts/student_tracker.py list
```

## 当前能做什么

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

## 目录约定

- `SKILL.md`：主说明
- `README.md`：使用说明
- `references/`：可公开模板与流程材料
- `scripts/`：本地分析脚本
- `examples/`：脱敏样例
- `scenarios/`：按单一班主任任务拆分的标准场景目录
- `scenarios/INDEX.md`：已落地场景入口
- `SCENARIOS_INDEX.md`：完整场景规划总表
- `data/`：本地私有目录，默认不公开

## 下一步优先做什么

优先做这 5 个闭环：

1. 家长群消息润色 + 确认发送
2. 每日 / 每周提醒自动生成
3. 评语平时采集，期末批量生成
4. 作业未交 / 迟到异常提醒
5. 班级日报 / 班务月报自动汇总

## 安全边界

不要提交真实学生隐私数据。

不要提交：
- 成绩明细
- 联系方式
- 家校沟通原文
- 家庭信息
- token / cookie / sessionKey / 平台密钥

默认约定：
- `data/` 只放本地私有数据
- 可公开内容放在 `references/`、`scripts/`、`examples/`

## 参考资料

- `references/notification_templates.md`
- `references/parent_meeting_guide.md`
- `references/student_record_template.md`
- `references/class_calendar.md`
- `references/emergency_procedures.md`

## 最后

直接给任务，不用先学提示词。
