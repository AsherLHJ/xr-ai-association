#!/usr/bin/env python3
"""
全面检查并修复所有遗漏的中文默认文本
"""

import re

# 读取文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# 查找所有 pattern: >中文<
# 检查是否有 data-zh/data-en 属性
chinese_pattern = r'>[\u4e00-\u9fff]+<'

# 查找所有匹配
matches = re.findall(chinese_pattern, content)

print(f"Found {len(matches)} Chinese text segments to check")
print("="*70)

# 需要检查的常见中文文本
need_check = [
    '用',
    '实践应用与创新创造',
    '核心部门',
    '研究开发部',
    '教育培训部',
    '项目管理部',
    '宣传运营部',
    '伙伴关系部',
    '历史活动',
    'Rokid 线下工作坊',
    'XR 探索之旅',
    'AI 超感嘉年华，探索无限可能',
    '活动策划',
    '特邀专家',
    '合作伙伴',
    '联系我们',
    '我们致力于打造一个多元共创的社区',
]

for zh_text in need_check:
    pattern = f'>{zh_text}<'
    if pattern in content:
        # 检查这个位置附近是否有 data-zh/data-en
        pos = content.find(pattern)
        check_around = content[max(0, pos - 100):min(pos + 50, len(content))]
        
        # 如果附近没有 data-zh 或 data-en，则需要添加
        if 'data-zh' not in check_around and 'data-en' not in check_around:
            # 需要翻译的映射
            translations_map = {
                '用': 'Apply',
                '实践应用与创新创造': 'Practice, apply, and innovate',
                '核心部门': 'Core Departments',
                '研究开发部': 'R&D Department',
                '教育培训部': 'Education Department',
                '项目管理部': 'Project Management',
                '宣传运营部': 'Marketing Department',
                '伙伴关系部': 'Partnership Department',
                '历史活动': 'Past Events',
                'Rokid 线下工作坊': 'Rokid Offline Workshop',
                'XR 探索之旅': 'XR Exploration Journey',
                'AI 超感嘉年华': 'AI Super-Sensing Carnival',
                '活动策划': 'Upcoming Programs',
                '特邀专家': 'Featured Experts',
                '合作伙伴': 'Our Partners',
                '联系我们': 'Contact Us',
            }
            
            if zh_text in translations_map:
                en_text = translations_map[zh_text]
                # 添加翻译属性
                new_pattern = f' data-zh="{zh_text}" data-en="{en_text}">{zh_text}<'
                content = content.replace(pattern, new_pattern)
                changes += 1
                print(f"  ✓ Fixed: {zh_text}")

# 保存
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal changes: {changes}")
