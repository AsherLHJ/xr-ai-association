#!/usr/bin/env python3
"""
全面修复 index.html - 自动检测并翻译所有中文文本
"""

import re

# 完整的翻译映射
translations = {
    '用': 'Apply',
    '实践应用与创新创造': 'Practice, Apply, and Innovate',
    '核心部门': 'Core Departments',
    '研究开发部': 'R&D Department',
    '教育培训部': 'Education Department',
    '项目管理部': 'Project Management',
    '宣传运营部': 'Marketing Department',
    '伙伴关系部': 'Partnership Department',
    '历史活动': 'Past Events',
    'Rokid 线下工作坊': 'Rokid Offline Workshop',
    'XR 探索之旅': 'XR Exploration Journey',
    'AI 超感嘉年华，探索无限可能': 'AI Super-Sensing Carnival, Explore Infinite Possibilities',
    '活动策划': 'Upcoming Programs',
    '特邀专家': 'Featured Experts',
    '合作伙伴': 'Our Partners',
    '联系我们': 'Contact Us',
    '我们致力于打造一个多元共创的社区，赋能港科广的每一位学子积极参与创新竞赛、跨学科合作与应用落地，推动科技与社会的深度融合。': 'We are committed to building a diverse and collaborative community, empowering every student at HKUST(GZ) to actively participate in innovation competitions, interdisciplinary collaboration, and application implementation, promoting the deep integration of technology and society.',
}

def fix_file(filepath):
    """修复单个文件"""
    print(f"\n=== Processing: {filepath} ===")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = 0

    # 查找所有 >中文<
    for zh_text, en_text in translations.items():
        pattern = f'>{zh_text}<'
        if pattern in content:
            # 检查附近是否有 data-zh/data-en
            pos = content.find(pattern)
            check_around = content[max(0, pos - 50):min(pos + 50, len(content))]
            
            # 如果附近没有 data-zh/data-en，则添加
            if 'data-zh' not in check_around or 'data-en' not in check_around:
                new_pattern = f' data-zh="{zh_text}" data-en="{en_text}">{zh_text}<'
                content = content.replace(pattern, new_pattern)
                changes += 1
                print(f"  ✓ Added translation for: {zh_text[:50]}...")

    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Total changes: {changes}")
    return changes


def main():
    """主函数"""
    print("="*70)
    print("  Fixing index.html - Adding All Missing Translations")
    print("="*70)

    changes = fix_file('index.html')

    print("\n" + "="*70)
    print(f"  Total changes: {changes}")
    print("="*70)


if __name__ == '__main__':
    main()
