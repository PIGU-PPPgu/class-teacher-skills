#!/usr/bin/env python3
"""
学生成长跟踪工具 - 记录和管理特殊学生情况
"""

import json
import os
import argparse
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/student_tracker.json')

def ensure_data_file():
    """确保数据文件存在"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)

def load_data():
    """加载学生数据"""
    ensure_data_file()
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    """保存学生数据"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_student(name, issue_type, description=""):
    """添加需要跟踪的学生"""
    data = load_data()
    
    if name not in data:
        data[name] = {
            'name': name,
            'issue_type': issue_type,
            'description': description,
            'created_at': datetime.now().isoformat(),
            'records': [],
            'status': '跟踪中'
        }
        save_data(data)
        print(f"✅ 已添加学生：{name} ({issue_type})")
    else:
        print(f"⚠️ 学生 {name} 已存在")

def add_record(name, note, record_type="谈话记录"):
    """添加跟踪记录"""
    data = load_data()
    
    if name not in data:
        print(f"❌ 学生 {name} 不存在，请先添加")
        return
    
    record = {
        'date': datetime.now().isoformat(),
        'type': record_type,
        'content': note
    }
    data[name]['records'].append(record)
    save_data(data)
    print(f"✅ 已为 {name} 添加记录")

def generate_report(name):
    """生成学生跟踪报告"""
    data = load_data()
    
    if name not in data:
        print(f"❌ 学生 {name} 不存在")
        return
    
    student = data[name]
    report = []
    report.append(f"# {name} - 成长跟踪报告")
    report.append(f"\n**问题类型：** {student['issue_type']}")
    report.append(f"**当前状态：** {student['status']}")
    report.append(f"**建档时间：** {student['created_at'][:10]}")
    
    if student['description']:
        report.append(f"\n**基本情况：**\n{student['description']}")
    
    report.append(f"\n## 跟踪记录 ({len(student['records'])} 条)")
    
    for record in student['records']:
        report.append(f"\n### {record['date'][:10]} - {record['type']}")
        report.append(record['content'])
    
    report_text = '\n'.join(report)
    print(report_text)
    return report_text

def list_students():
    """列出所有跟踪中的学生"""
    data = load_data()
    
    if not data:
        print("暂无跟踪记录")
        return
    
    print("\n# 学生跟踪列表\n")
    for name, info in data.items():
        status_icon = "🔴" if info['status'] == '跟踪中' else "🟢"
        record_count = len(info['records'])
        print(f"{status_icon} {name} | {info['issue_type']} | {record_count}条记录 | {info['status']}")

def update_status(name, new_status):
    """更新学生状态"""
    data = load_data()
    
    if name not in data:
        print(f"❌ 学生 {name} 不存在")
        return
    
    data[name]['status'] = new_status
    save_data(data)
    print(f"✅ {name} 的状态已更新为：{new_status}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='学生成长跟踪工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    # add
    add_parser = subparsers.add_parser('add', help='添加学生')
    add_parser.add_argument('name', help='学生姓名')
    add_parser.add_argument('--issue', required=True, help='问题类型')
    add_parser.add_argument('--desc', default='', help='情况描述')
    
    # update
    update_parser = subparsers.add_parser('update', help='添加跟踪记录')
    update_parser.add_argument('name', help='学生姓名')
    update_parser.add_argument('--note', required=True, help='记录内容')
    update_parser.add_argument('--type', default='谈话记录', help='记录类型')
    
    # report
    report_parser = subparsers.add_parser('report', help='生成报告')
    report_parser.add_argument('name', help='学生姓名')
    
    # list
    subparsers.add_parser('list', help='列出所有学生')
    
    # status
    status_parser = subparsers.add_parser('status', help='更新状态')
    status_parser.add_argument('name', help='学生姓名')
    status_parser.add_argument('new_status', help='新状态')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_student(args.name, args.issue, args.desc)
    elif args.command == 'update':
        add_record(args.name, args.note, args.type)
    elif args.command == 'report':
        generate_report(args.name)
    elif args.command == 'list':
        list_students()
    elif args.command == 'status':
        update_status(args.name, args.new_status)
    else:
        parser.print_help()
