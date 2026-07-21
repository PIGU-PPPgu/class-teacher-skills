---
name: class-teacher-market-scan
description: 调研"班主任/教师助手"相关 skill 生态，并沉淀本机现状、市场结论、可复用方向与配置验证记录。适用于想判断是否已有成熟班主任 skill、梳理本地已有能力，或保存 memtensor/记忆系统验收结果时。
---

# 班主任 Skill 市场与本机能力扫描

用于回答三类问题：
1. **本机有没有现成班主任 skill**
2. **市面上有没有成熟、标准化的班主任 skill**
3. **本地记忆/配置（如 memtensor）是否已验证正常**

## 结论模板

### 1. 本机现状
如果需要先判断本机是否已有班主任 skill，优先检查本地 skill 库命名与描述，而不是先猜。

当前已确认：
- 本机**没有**明确命名为 `班主任` / `teacher` / `homeroom` / `student` / `school` 的成熟通用独立 skill（以早期扫描结论为准）
- 但存在若干**邻近能力**，可拼装成班主任工作流：
  - `google-workspace`
  - `notion`
  - `ocr-and-documents`
  - `plan-my-day`
  - `task`
  - `obsidian`
  - `visual-cognition-slides`
- 当前工作区另外还发现了一个本地班主任技能原型：`clawd/skills/class-assistant/`
  - 含 `SKILL.md`
  - 含脚本：成绩分析、考勤报告、学生跟踪
  - 含参考资料：通知模板、家长会指南、学生记录模板、班级日程模板

### 2. 市面结论
对外部生态的保守结论应写清楚：

- **没有看到现成、成熟、明确叫"班主任 skill"的通用标准成品**
- 但存在很多**相邻形态**：
  - 教师助手 GPT / Agent
  - 家校沟通模板
  - 成绩分析工具
  - 班级管理 SaaS
  - 通用办公自动化 skill
- 结论别吹太满：更准确的说法是 **"没有发现统一标准产品，但相关能力碎片很多，适合组合成班主任专用 skill"**

### 3. 已验证配置（记忆系统）
如果用户是在确认记忆系统/技能基础设施是否可用，可直接记录以下验收项：

- `memtensor` provider 能正常加载
- 后台 daemon 在跑：
  - viewer: `0.0.0.0:18901`
  - bridge: `127.0.0.1:18992`
- 数据目录已创建：`/root/.hermes/memos-state/`
- 数据库已落盘：`/root/.hermes/memos-state/memos-local/memos.db`
- viewer 页面可打开，标题是 `Hermes 记忆`
- `~/.hermes/config.yaml` 已是 `memory.provider: memtensor`
- 日志关键字正常：
  - `Plugin ready. DB: /root/.hermes/memos-state/memos-local/memos.db, Embedding: local`
  - `Viewer started at http://127.0.0.1:18901`
  - `Bridge daemon listening on 127.0.0.1:18992`

## 推荐回答结构

当用户问"有没有班主任 skill"时，优先按这个顺序回答：

1. **先给结论**：没有看到成熟标准品
2. **再分两层**：
   - 本机有没有
   - 市面上有没有
3. **最后给建议**：
   - 若要真正可用，别等"现成神技"，直接把通知、成绩、考勤、学生跟踪、月度清单拼成一个专用 skill
   - 优先沉淀成可维护的本地 skill，而不是散落在聊天记录里

## 本机已知材料

- `clawd/skills/class-assistant/SKILL.md`
- `clawd/skills/class-assistant/scripts/attendance_report.py`
- `clawd/skills/class-assistant/scripts/analyze_grades.py`
- `clawd/skills/class-assistant/scripts/student_tracker.py`
- `clawd/memory/teacher_checklist_2026-02.md`
- `clawd/memory/class_teacher_checklist_2026-03.md`
- `clawd/HEARTBEAT.md`
- `clawd/MEMORY.md`

## 使用建议

- 想做成可上传 GitHub 的版本时，把"市场扫描"与"真正执行型班主任 skill"分开：
  - 这个 skill 负责**背景结论与基础设施验收**
  - `class-assistant` 负责**实际班主任工作流**
- 不要把敏感账号、token、邮箱密码、sessionKey 之类写进 skill。
