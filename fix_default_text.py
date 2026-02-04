#!/usr/bin/env python3
"""
批量修复所有HTML文件的默认文本为英文
"""

import re

# 定义所有页面的翻译映射
translations = {
    # index.html
    '协会简介': 'About Us',
    '玩学用三部曲': 'Play-Learn-Apply Trilogy',
    '合作伙伴': 'Our Partners',
    '联系我们': 'Contact Us',
    '我们致力于打造一个多元共创的社区，赋能港科广的每一位学子积极参与创新竞赛、跨学科合作与应用落地，推动科技与社会的深度融合。': 'We are committed to building a diverse and collaborative community, empowering every student at HKUST(GZ) to actively participate in innovation competitions, interdisciplinary collaboration, and application implementation, promoting the deep integration of technology and society.',
    '玩学用三部曲，从入门到进阶，契合会员情况与实践需求，助力学生在技术探索过程中，实现快速升级。': 'The Play-Learn-Apply Trilogy progresses from introductory to advanced levels, aligning with members\' situations and practical needs, helping students achieve rapid upgrades during their technical exploration journey.',
    '玩': 'Play',
    '通过沉浸式的XR体验，激发学生对技术的兴趣，在游戏中感受科技魅力。': 'Spark students\' interest in technology through immersive XR experiences and feel the charm of technology while gaming.',
    '学': 'Learn',
    '系统学习XR、AI等前沿技术，掌握理论基础和实践技能。': 'Systematically learn cutting-edge technologies such as XR and AI, mastering theoretical foundations and practical skills.',
    '用': 'Apply',
    '将所学知识应用于实际项目，参与竞赛和活动，实现创新突破。': 'Apply learned knowledge to actual projects, participate in competitions and events, and achieve innovative breakthroughs.',
    '查看所有专家': 'View All Experts',
    '查看活动': 'View Events',
    '了解更多': 'Learn More',
    '查看历史活动': 'View Past Events',
    '查看活动策划': 'View Programs',
    '行业合作': 'Partnership',
    '专家预览': 'Featured Experts',
    '张康教授 - 计算机媒体与艺术学域主任': 'Kang Zhang - Head of CMA',
    '许彬教授 - 信息枢纽副院长': 'Bin Xu - Vice Dean of IHub',
    '梁海宁教授 - 计算机媒体与艺术副教授': 'Haining Liang - Associate Professor of CMA',
    '王宇阳教授': 'Prof. Yuyang Wang',
    'Rachel Franz': 'Rachel Franz',
    '罗越': 'Luo Yue',
    '陈俊楠': 'Chen Junnan',
    '加入我们': 'Join Us',
    '欢迎每一位有志之士加入我们！': 'We welcome every like-minded individual to join us!',
    '香港科技大学（广州）': 'HKUST(GZ)',
    '科技造梦 · 探索未知 · 突破极限': 'Technology Dreams · Exploring the Unknown · Breaking Boundaries',
}


def fix_file(filepath):
    """修复单个文件"""
    print(f"\n=== Processing: {filepath} ===")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = 0

    # 替换所有中文默认文本为英文
    for zh_text, en_text in translations.items():
        # 查找 >中文< 模式
        pattern = f'>{zh_text}<'
        if pattern in content:
            replacement = f'>{en_text}<'
            content = content.replace(pattern, replacement)
            changes += 1
            print(f"  ✓ Replaced: {zh_text[:50]}...")

        # 查找 data-zh="..." data-en="...">中文< 模式
        # 这种情况下，保留 attributes，只替换结束标签前的文本
        pattern_with_attrs = f'data-zh="{zh_text}" data-en="{en_text}">{zh_text}<'
        if pattern_with_attrs in content:
            replacement_with_attrs = f'data-zh="{zh_text}" data-en="{en_text}">{en_text}<'
            content = content.replace(pattern_with_attrs, replacement_with_attrs)
            changes += 1
            print(f"  ✓ Replaced (with attrs): {zh_text[:50]}...")

    # 保存文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Total changes: {changes}")
    return changes


def main():
    """主函数"""
    files = [
        'index.html',
        'pages/about.html',
        'pages/events.html',
        'pages/programs.html',
        'pages/experts.html',
        'pages/partnership.html',
        'pages/contact.html',
    ]

    print("="*70)
    print("  Fixing Default Text to English")
    print("="*70)

    total_changes = 0

    for filepath in files:
        if filepath in ['index.html']:
            # index.html 在根目录
            full_path = filepath
        else:
            full_path = filepath

        try:
            total_changes += fix_file(full_path)
        except Exception as e:
            print(f"  ✗ Error: {e}")

    print("\n" + "="*70)
    print(f"  Total changes across all files: {total_changes}")
    print("="*70)


if __name__ == '__main__':
    main()
