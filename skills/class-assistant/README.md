# class-assistant

班主任工作流 skill，覆盖通知文案、成绩分析、考勤统计、学生跟踪、家长会准备等常见场景。

它现在不是“全自动班主任 AI”。

它更准确的定位是：
- **现在**：班主任数字助理 / 模板与脚本工具包
- **下一步**：接入定时任务和消息平台后的主动工作流系统

## 目录

- `SKILL.md`：技能主说明
- `references/`：可公开的模板与流程材料
- `scripts/`：本地分析脚本
- `examples/`：脱敏后的示例数据，供演示和测试
- `data/`：本地私有数据目录（默认不应提交到 GitHub）

## 这个 skill 现在能做什么

### 1. 文案与材料
- 家长群通知
- 学生评语 / 寄语
- 班会发言稿
- 家长会材料
- 常见班务模板

### 2. 数据与分析
- 成绩分析：`scripts/analyze_grades.py`
- 考勤统计：`scripts/attendance_report.py`
- 学生成长跟踪：`scripts/student_tracker.py`

### 3. 工作流底座
- 班务模板库
- 学生记录模板
- 脱敏样例数据
- 主动工作流路线图

## 别人如何调用这个 skill

### 用法 A：在 Hermes / 支持 skill 的 agent 环境里直接调用
直接加载 `class-assistant`，然后自然语言下任务。

示例：
- `帮我起草一个关于春游安全事项的家长群通知`
- `分析这次月考成绩，找出进步最大的 5 名学生`
- `记录一下今天和小明的谈话，要写进学生跟踪`
- `给我准备一份下周家长会发言提纲`

### 用法 B：把它当成模板包和脚本工具包
如果别人没有完整 agent 平台，也能这样用：

1. 阅读 `SKILL.md` 了解适用场景
2. 从 `references/` 复制模板
3. 用 `examples/` 理解输入格式
4. 运行 `scripts/` 做分析和汇总

### 用法 C：接成主动工作流
后续可以把它接到：
- 飞书
- 钉钉
- 企业微信
- cron / 调度系统
- 考勤 / 作业 / 校历 / 天气等数据源

那时这个 skill 提供的是：
- 规则
- 模板
- 输入输出格式
- 文案生成与分析逻辑

## 主动工作流路线图

已经沉淀进 skill 的下一阶段方向包括：
- 每周任务清单自动推送
- 每日提醒 / 天气提醒
- 评语平时采集、期末批量生成
- 作业未交 / 迟到异常提醒
- 班级日报 / 月报自动汇总
- 家长群消息润色 + 确认发送

## GitHub 发布规则

这个 skill 可以公开，但前提是别把真实学生和教师数据一起扔上去。

### 应公开的
- `SKILL.md`
- `references/`
- `scripts/`
- `examples/`

### 不应公开的
- `data/` 下真实姓名、学号、班级、成绩、教师信息
- 任意包含家校沟通记录、谈话原文、联系方式的文件
- token、cookie、sessionKey、邮箱密码、平台密钥

## 依赖

当前脚本至少依赖：
- Python 3.9+
- `pandas`
- `openpyxl`（用于读取 `.xlsx` 成绩表）

安装：

```bash
pip install -r requirements.txt
```

## 脚本示例

### 成绩分析
```bash
python scripts/analyze_grades.py --file examples/students.sample.csv --output report.md
```

### 考勤统计
```bash
python scripts/attendance_report.py --file your_attendance.csv --month 2026-02
```

### 学生成长跟踪
```bash
python scripts/student_tracker.py add 张三 --issue 行为波动 --desc "最近上课注意力不稳定"
python scripts/student_tracker.py update 张三 --note "今天谈话后情绪平稳" --type 谈话记录
python scripts/student_tracker.py report 张三
```

## 最低发布标准

1. 脚本可以按 README 说明运行
2. 至少提供一份脱敏样例数据
3. 明确声明 `data/` 是本地私有目录
4. 不依赖写死的个人机器路径
5. 对外说法别吹成已经全自动闭环
