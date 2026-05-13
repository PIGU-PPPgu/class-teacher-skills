#!/usr/bin/env python3
"""
智能座位编排脚本

用途：根据学生多维评分 CSV 文件，自动生成组内异质互补、组间实力均衡的
     分组方案，输出 Markdown 格式的分组表、编排理由和座位图。

用法：
    python smart_seat_arrangement.py --input scores.csv --output result.md

输入格式（CSV）：
    姓名,性别,学业排名段,偏科程度,外向话多,自控力,领导力,情绪稳定性,备注

学业排名段说明：
    1 = 前12名, 2 = 13-24名, 3 = 25-36名, 4 = 37名及以后

依赖：仅使用 Python 标准库（csv, argparse, random, math）
"""

import csv
import argparse
import random
import math
from collections import defaultdict


# ============================================================
# 数据读取
# ============================================================

def read_students(filepath):
    """读取 CSV 评分表，返回学生字典列表。"""
    students = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = {
                'name': row['姓名'].strip(),
                'gender': row.get('性别', '').strip(),
                'rank_tier': int(row['学业排名段']),
                'subject_bias': float(row['偏科程度']),
                'talkativeness': float(row['外向话多']),
                'self_control': float(row['自控力']),
                'leadership': float(row['领导力']),
                'emotion_stability': float(row['情绪稳定性']),
                'note': row.get('备注', '').strip(),
            }
            students.append(student)
    return students


# ============================================================
# 分层与分组
# ============================================================

def split_by_tier(students):
    """按学业排名段分层，返回 {1: [...], 2: [...], 3: [...], 4: [...]}"""
    tiers = defaultdict(list)
    for s in students:
        tiers[s['rank_tier']].append(s)
    # 每层内随机打乱，避免每次结果完全相同
    for tier in tiers:
        random.shuffle(tiers[tier])
    return tiers


def compute_compatibility(s1, s2):
    """
    计算两个学生的性格互补得分（越高越互补）。
    - 话多 vs 安静
    - 领导力强 vs 被动
    - 偏科互补（偏科程度差异大时加分）
    - 情绪不稳定 vs 稳定
    """
    score = 0.0

    # 话多(>0.6) 与 安静(<0.4) 互补
    talk_diff = abs(s1['talkativeness'] - s2['talkativeness'])
    if (s1['talkativeness'] > 0.6 and s2['talkativeness'] < 0.4) or \
       (s2['talkativeness'] > 0.6 and s1['talkativeness'] < 0.4):
        score += 3.0  # 强互补
    elif talk_diff > 0.2:
        score += talk_diff * 2  # 一般互补

    # 领导力强(>0.6) 与 被动(<0.4) 互补
    lead_diff = abs(s1['leadership'] - s2['leadership'])
    if (s1['leadership'] > 0.6 and s2['leadership'] < 0.4) or \
       (s2['leadership'] > 0.6 and s1['leadership'] < 0.4):
        score += 3.0
    elif lead_diff > 0.2:
        score += lead_diff * 2

    # 偏科互补（偏科方向不同，差异大时加分）
    bias_diff = abs(s1['subject_bias'] - s2['subject_bias'])
    if bias_diff > 0.3:
        score += bias_diff * 2

    # 情绪不稳定(<0.4) 与 稳定(>0.6) 互补
    emo_diff = abs(s1['emotion_stability'] - s2['emotion_stability'])
    if (s1['emotion_stability'] < 0.4 and s2['emotion_stability'] > 0.6) or \
       (s2['emotion_stability'] < 0.4 and s1['emotion_stability'] > 0.6):
        score += 3.0
    elif emo_diff > 0.2:
        score += emo_diff * 2

    return score


def greedy_pair(list_a, list_b):
    """
    贪心配对：从 list_a 和 list_b 中按互补得分最大化进行配对。
    返回 [(a, b), ...] 配对列表，以及两个列表中未配对的剩余元素。
    """
    pairs = []
    used_b = set()

    for a in list_a:
        best_score = -1
        best_b = None
        best_idx = -1
        for idx, b in enumerate(list_b):
            if idx in used_b:
                continue
            score = compute_compatibility(a, b)
            if score > best_score:
                best_score = score
                best_b = b
                best_idx = idx
        if best_b is not None:
            pairs.append((a, best_b))
            used_b.add(best_idx)

    remaining_b = [b for idx, b in enumerate(list_b) if idx not in used_b]
    return pairs, remaining_b


def form_groups(tiers):
    """
    核心分组逻辑：
    1. 1号段 + 4号段 贪心配对
    2. 2号段 + 3号段 贪心配对
    3. 将 (1+4) 对与 (2+3) 对合并为 4 人组
    """
    tier1 = list(tiers.get(1, []))
    tier2 = list(tiers.get(2, []))
    tier3 = list(tiers.get(3, []))
    tier4 = list(tiers.get(4, []))

    # 1+4 配对
    pairs_14, remaining_4 = greedy_pair(tier1, tier4)
    # 2+3 配对
    pairs_23, remaining_3 = greedy_pair(tier2, tier3)

    # 如果有未配对的剩余学生，尝试补充配对
    # 剩余 4 号段可以和剩余 3 号段配对（降级处理）
    extra_pairs = []
    for s4 in remaining_4:
        if remaining_3:
            best_s3 = max(remaining_3, key=lambda s: compute_compatibility(s4, s))
            extra_pairs.append((s4, best_s3, 'extra_4_3'))
            remaining_3.remove(best_s3)
        else:
            extra_pairs.append((s4, None, 'extra_4'))

    for s3 in remaining_3:
        extra_pairs.append((s3, None, 'extra_3'))

    # 合并成 4 人组
    groups = []
    num_main_groups = max(len(pairs_14), len(pairs_23))

    # 扩展较短的列表
    while len(pairs_14) < num_main_groups:
        pairs_14.append((None, None))
    while len(pairs_23) < num_main_groups:
        pairs_23.append((None, None))

    for i in range(num_main_groups):
        p14 = pairs_14[i]
        p23 = pairs_23[i]
        members = []
        if p14[0] is not None:
            members.append(p14[0])
        if p23[0] is not None:
            members.append(p23[0])
        if p23[1] is not None:
            members.append(p23[1])
        if p14[1] is not None:
            members.append(p14[1])
        if members:
            groups.append(members)

    # 处理额外配对（如果有未归组的学生）
    for ep in extra_pairs:
        if ep[1] is not None:
            # 找一个人数不足 4 人的组加入
            placed = False
            for g in groups:
                if len(g) < 4:
                    g.append(ep[0])
                    g.append(ep[1])
                    placed = True
                    break
            if not placed:
                groups.append([ep[0], ep[1]])
        else:
            # 单人，找人数不足的组
            placed = False
            for g in groups:
                if len(g) < 4:
                    g.append(ep[0])
                    placed = True
                    break
            if not placed:
                groups.append([ep[0]])

    return groups


# ============================================================
# 分析与输出
# ============================================================

def analyze_group(group, group_idx):
    """分析一个组的编排理由，返回理由文本。"""
    reasons = []

    # 按排名段排序便于描述
    tier_names = {1: '1号段', 2: '2号段', 3: '3号段', 4: '4号段'}
    sorted_members = sorted(group, key=lambda s: s['rank_tier'])

    # 学业搭配
    tier_counts = defaultdict(list)
    for s in sorted_members:
        tier_counts[s['rank_tier']].append(s['name'])
    tier_desc = '、'.join(
        f"{tier_names[t]}: {', '.join(names)}"
        for t, names in sorted(tier_counts.items())
    )
    reasons.append(f"学业搭配：{tier_desc}")

    # 性格分析
    talkative = [s for s in group if s['talkativeness'] > 0.6]
    quiet = [s for s in group if s['talkativeness'] < 0.4]
    if talkative and quiet:
        talk_names = ', '.join(s['name'] for s in talkative)
        quiet_names = ', '.join(s['name'] for s in quiet)
        reasons.append(f"性格对冲：{talk_names}(偏外向) 与 {quiet_names}(偏安静) 互补")
    elif talkative:
        reasons.append("注意：本组偏外向同学较多，日常需关注互动节奏")

    # 领导力
    leaders = [s for s in group if s['leadership'] > 0.6]
    followers = [s for s in group if s['leadership'] < 0.4]
    if leaders and followers:
        leader_names = ', '.join(s['name'] for s in leaders)
        follower_names = ', '.join(s['name'] for s in followers)
        reasons.append(f"领导力互补：{leader_names}(主动型) 与 {follower_names}(配合型)")

    # 偏科互补
    high_bias = [s for s in group if s['subject_bias'] > 0.5]
    low_bias = [s for s in group if s['subject_bias'] < 0.3]
    if high_bias and low_bias:
        hb_names = ', '.join(s['name'] for s in high_bias)
        lb_names = ', '.join(s['name'] for s in low_bias)
        reasons.append(f"偏科互补：{hb_names}(有偏科) 与 {lb_names}(较均衡) 可互相帮助")

    # 情绪稳定性
    unstable = [s for s in group if s['emotion_stability'] < 0.4]
    stable = [s for s in group if s['emotion_stability'] > 0.6]
    if unstable and stable:
        unstable_names = ', '.join(s['name'] for s in unstable)
        stable_names = ', '.join(s['name'] for s in stable)
        reasons.append(f"情绪互补：{stable_names}(情绪稳定) 可帮助稳定 {unstable_names}")

    # 特殊备注
    noted = [s for s in group if s['note']]
    if noted:
        for s in noted:
            reasons.append(f"备注：{s['name']} - {s['note']}")

    return reasons


def compute_stats(groups):
    """计算编排统计指标。"""
    total = sum(len(g) for g in groups)

    # 配对率统计
    pair_14_count = 0
    pair_23_count = 0
    talk_match = 0
    lead_match = 0
    bias_match = 0
    emo_match = 0

    for g in groups:
        tier1 = [s for s in g if s['rank_tier'] == 1]
        tier4 = [s for s in g if s['rank_tier'] == 4]
        tier2 = [s for s in g if s['rank_tier'] == 2]
        tier3 = [s for s in g if s['rank_tier'] == 3]

        if tier1 and tier4:
            pair_14_count += 1
        if tier2 and tier3:
            pair_23_count += 1

        # 话多+安静
        talkative = any(s['talkativeness'] > 0.6 for s in g)
        quiet = any(s['talkativeness'] < 0.4 for s in g)
        if talkative and quiet:
            talk_match += 1

        # 领导力互补
        leader = any(s['leadership'] > 0.6 for s in g)
        follower = any(s['leadership'] < 0.4 for s in g)
        if leader and follower:
            lead_match += 1

        # 偏科互补
        high_bias = any(s['subject_bias'] > 0.5 for s in g)
        low_bias = any(s['subject_bias'] < 0.3 for s in g)
        if high_bias and low_bias:
            bias_match += 1

        # 情绪互补
        unstable = any(s['emotion_stability'] < 0.4 for s in g)
        stable = any(s['emotion_stability'] > 0.6 for s in g)
        if unstable and stable:
            emo_match += 1

    num_groups = len(groups)
    return {
        'total': total,
        'num_groups': num_groups,
        'group_size': round(total / num_groups, 1) if num_groups else 0,
        'pair_14_rate': f"{pair_14_count / num_groups * 100:.0f}%" if num_groups else "0%",
        'pair_23_rate': f"{pair_23_count / num_groups * 100:.0f}%" if num_groups else "0%",
        'talk_match_rate': f"{talk_match / num_groups * 100:.0f}%" if num_groups else "0%",
        'lead_match_rate': f"{lead_match / num_groups * 100:.0f}%" if num_groups else "0%",
        'bias_match_rate': f"{bias_match / num_groups * 100:.0f}%" if num_groups else "0%",
        'emo_match_rate': f"{emo_match / num_groups * 100:.0f}%" if num_groups else "0%",
    }


def generate_seat_map(groups):
    """生成座位图文本，每行排 4 个小组。"""
    lines = []
    lines.append("讲台")
    lines.append("═" * 60)
    lines.append("")

    cols = 4

    for row_start in range(0, len(groups), cols):
        row_gs = groups[row_start:row_start + cols]
        # 补齐到 4 列
        while len(row_gs) < cols:
            row_gs.append([])

        # 组名行
        header_parts = []
        for i in range(len(row_gs)):
            group_num = row_start + i + 1
            if row_gs[i]:
                header_parts.append(f"  第{group_num}组")
            else:
                header_parts.append("")
        lines.append("  ".join(f"{h:^14}" for h in header_parts).rstrip())

        # 上排（1号段 + 4号段）
        top_line = ""
        for g in row_gs:
            t1 = [s['name'] for s in g if s['rank_tier'] == 1]
            t4 = [s['name'] for s in g if s['rank_tier'] == 4]
            left = t1[0] if t1 else '—'
            right = t4[0] if t4 else '—'
            top_line += f"│ {left:^5} {right:^5} │"
        lines.append(top_line)

        # 下排（2号段 + 3号段）
        bot_line = ""
        for g in row_gs:
            t2 = [s['name'] for s in g if s['rank_tier'] == 2]
            t3 = [s['name'] for s in g if s['rank_tier'] == 3]
            left = t2[0] if t2 else '—'
            right = t3[0] if t3 else '—'
            bot_line += f"│ {left:^5} {right:^5} │"
        lines.append(bot_line)
        lines.append("")

    lines.append("═" * 60)
    lines.append("                    后门")

    return '\n'.join(lines)


def format_groups_table(groups):
    """生成分组表 Markdown。"""
    lines = []
    lines.append("| 组别 | 成员1(1号段) | 成员2(2号段) | 成员3(3号段) | 成员4(4号段) |")
    lines.append("|------|-------------|-------------|-------------|-------------|")

    for i, g in enumerate(groups):
        tier1 = [s['name'] for s in g if s['rank_tier'] == 1]
        tier2 = [s['name'] for s in g if s['rank_tier'] == 2]
        tier3 = [s['name'] for s in g if s['rank_tier'] == 3]
        tier4 = [s['name'] for s in g if s['rank_tier'] == 4]

        t1 = tier1[0] if tier1 else '-'
        t2 = tier2[0] if tier2 else '-'
        t3 = tier3[0] if tier3 else '-'
        t4 = tier4[0] if tier4 else '-'

        lines.append(f"| 第{i+1}组 | {t1} | {t2} | {t3} | {t4} |")

    return '\n'.join(lines)


def generate_markdown(groups, stats):
    """生成完整 Markdown 输出。"""
    lines = []
    lines.append("# 智能座位编排方案")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 一、分组方案总览")
    lines.append("")
    lines.append(format_groups_table(groups))
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 二、编排理由")
    lines.append("")

    for i, g in enumerate(groups):
        reasons = analyze_group(g, i)
        lines.append(f"### 第{i+1}组")
        for r in reasons:
            lines.append(f"- {r}")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 三、座位图")
    lines.append("")
    lines.append("```")
    lines.append(generate_seat_map(groups))
    lines.append("```")
    lines.append("")
    lines.append("**座位说明：**")
    lines.append("- 左上角为 1 号段同学，右上角为 4 号段同学（1+4 配对）")
    lines.append("- 左下角为 2 号段同学，右下角为 3 号段同学（2+3 配对）")
    lines.append("- 实际座位方向可根据教室布局调整")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 四、编排统计")
    lines.append("")
    lines.append("| 指标 | 数值 |")
    lines.append("|------|------|")
    lines.append(f"| 总人数 | {stats['total']} 人 |")
    lines.append(f"| 分组数 | {stats['num_groups']} 组 |")
    lines.append(f"| 每组人数 | {stats['group_size']} 人 |")
    lines.append(f"| 1+4 配对完成率 | {stats['pair_14_rate']} |")
    lines.append(f"| 2+3 配对完成率 | {stats['pair_23_rate']} |")
    lines.append(f"| 话多+安静配对率 | {stats['talk_match_rate']} |")
    lines.append(f"| 领导力互补配对率 | {stats['lead_match_rate']} |")
    lines.append(f"| 偏科互补配对率 | {stats['bias_match_rate']} |")
    lines.append(f"| 情绪互补配对率 | {stats['emo_match_rate']} |")

    return '\n'.join(lines)


# ============================================================
# 主程序
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='智能座位编排脚本：基于多维评分生成分组方案'
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help='输入 CSV 文件路径（学生多维评分表）'
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='输出 Markdown 文件路径'
    )
    parser.add_argument(
        '--seed',
        type=int,
        default=None,
        help='随机种子（可选，用于复现结果）'
    )

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    # 读取数据
    print(f"正在读取评分表：{args.input}")
    students = read_students(args.input)
    print(f"共读取 {len(students)} 名学生")

    # 按学业排名段分层
    tiers = split_by_tier(students)
    for tier in sorted(tiers.keys()):
        print(f"  {tier} 号段：{len(tiers[tier])} 人")

    # 分组编排
    print("正在进行智能编排...")
    groups = form_groups(tiers)
    print(f"共生成 {len(groups)} 个小组")

    # 计算统计
    stats = compute_stats(groups)

    # 生成输出
    markdown = generate_markdown(groups, stats)

    # 写入文件
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(markdown)

    print(f"编排完成，结果已保存至：{args.output}")
    print()
    print("=== 编排统计 ===")
    for key, value in stats.items():
        print(f"  {key}: {value}")


if __name__ == '__main__':
    main()
