#!/usr/bin/env python3
"""
考勤报告生成工具
"""

import pandas as pd
import argparse
from datetime import datetime

def generate_attendance_report(file_path, month=None):
    """生成考勤报告"""
    
    df = pd.read_csv(file_path)
    
    # 自动识别列名
    name_col = None
    date_col = None
    status_col = None
    
    for col in df.columns:
        col_str = str(col).lower()
        if any(k in col_str for k in ['姓名', '名字', 'name']):
            name_col = col
        elif any(k in col_str for k in ['日期', 'date', '时间']):
            date_col = col
        elif any(k in col_str for k in ['状态', '类型', 'status', 'type']):
            status_col = col
    
    if not name_col:
        name_col = df.columns[0]
    if not status_col:
        status_col = df.columns[-1]
    
    report = []
    report.append("# 考勤统计报告")
    report.append(f"\n统计时间：{datetime.now().strftime('%Y-%m-%d')}")
    if month:
        report.append(f"统计月份：{month}")
    
    # 按学生统计
    report.append("\n## 学生考勤统计\n")
    
    for student in df[name_col].unique():
        student_data = df[df[name_col] == student]
        
        report.append(f"### {student}")
        
        # 统计各类状态
        status_counts = student_data[status_col].value_counts()
        for status, count in status_counts.items():
            report.append(f"- {status}：{count}次")
        
        report.append("")
    
    # 整体统计
    report.append("\n## 整体情况")
    total_counts = df[status_col].value_counts()
    for status, count in total_counts.items():
        report.append(f"- {status}：{count}人次")
    
    report_text = '\n'.join(report)
    print(report_text)
    return report_text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='考勤报告工具')
    parser.add_argument('--file', '-f', required=True, help='考勤数据文件 (csv)')
    parser.add_argument('--month', '-m', help='统计月份 (如：2026-02)')
    
    args = parser.parse_args()
    generate_attendance_report(args.file, args.month)
