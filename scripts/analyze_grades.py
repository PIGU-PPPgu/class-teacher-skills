#!/usr/bin/env python3
"""
成绩分析工具 - 生成班级成绩分析报告
"""

import pandas as pd
import sys
import argparse
from datetime import datetime

def analyze_grades(file_path, output_path=None):
    """分析成绩数据并生成报告"""
    
    # 读取数据
    df = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)
    
    # 自动识别学生姓名列和成绩列
    name_col = None
    score_cols = []
    
    for col in df.columns:
        col_str = str(col).lower()
        if any(keyword in col_str for keyword in ['姓名', '名字', 'name', '学生']):
            name_col = col
        elif any(keyword in col_str for keyword in ['成绩', '分数', 'score', '总分']):
            score_cols.append(col)
    
    if not name_col:
        name_col = df.columns[0]  # 默认第一列为姓名
    if not score_cols:
        # 尝试找出数值列作为成绩
        for col in df.columns:
            if df[col].dtype in ['int64', 'float64'] and col != name_col:
                score_cols.append(col)
    
    report = []
    report.append("# 班级成绩分析报告")
    report.append(f"\n生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append(f"数据来源：{file_path}")
    report.append(f"\n## 数据概览")
    report.append(f"- 学生人数：{len(df)}")
    report.append(f"- 分析科目：{len(score_cols)} 科")
    
    for score_col in score_cols:
        scores = df[score_col]
        report.append(f"\n### {score_col}")
        report.append(f"- 平均分：{scores.mean():.2f}")
        report.append(f"- 最高分：{scores.max():.2f}")
        report.append(f"- 最低分：{scores.min():.2f}")
        report.append(f"- 中位数：{scores.median():.2f}")
        report.append(f"- 标准差：{scores.std():.2f}")
        
        # 分数段分布
        report.append(f"\n**分数段分布：**")
        excellent = len(scores[scores >= 90])
        good = len(scores[(scores >= 80) & (scores < 90)])
        medium = len(scores[(scores >= 60) & (scores < 80)])
        poor = len(scores[scores < 60])
        
        report.append(f"- 优秀(≥90)：{excellent}人 ({excellent/len(scores)*100:.1f}%)")
        report.append(f"- 良好(80-89)：{good}人 ({good/len(scores)*100:.1f}%)")
        report.append(f"- 中等(60-79)：{medium}人 ({medium/len(scores)*100:.1f}%)")
        report.append(f"- 需努力(<60)：{poor}人 ({poor/len(scores)*100:.1f}%)")
        
        # 重点关注学生
        report.append(f"\n**需要关注的学生：**")
        low_scorers = df[scores < 60][[name_col, score_col]].sort_values(score_col)
        for _, row in low_scorers.head(5).iterrows():
            report.append(f"- {row[name_col]}：{row[score_col]:.1f}分")
    
    # 偏科分析（如果有多个科目）
    if len(score_cols) >= 2:
        report.append(f"\n## 偏科分析")
        df['avg'] = df[score_cols].mean(axis=1)
        df['std'] = df[score_cols].std(axis=1)
        
        report.append(f"\n**偏科较严重的学生（标准差>15）：**")
        biased = df[df['std'] > 15].sort_values('std', ascending=False)
        for _, row in biased.head(5).iterrows():
            report.append(f"- {row[name_col]}：标准差 {row['std']:.2f}")
    
    report_text = '\n'.join(report)
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"✅ 分析报告已保存：{output_path}")
    else:
        print(report_text)
    
    return report_text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='班级成绩分析工具')
    parser.add_argument('--file', '-f', required=True, help='成绩文件路径 (xlsx 或 csv)')
    parser.add_argument('--output', '-o', help='输出报告路径 (默认输出到控制台)')
    
    args = parser.parse_args()
    analyze_grades(args.file, args.output)
