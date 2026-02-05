#!/usr/bin/env python3
"""
修复所有带 data-zh/data-en 属性的默认文本为英文
"""

import re

def fix_file(filepath):
    """修复单个文件"""
    print(f"\n=== Processing: {filepath} ===")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = 0

    # 查找所有 data-zh="..." data-en="...">中文< 的模式
    pattern = r' data-zh="([^"]+)" data-en="([^"]+)">([^<]+)<'

    matches = re.findall(pattern, content)

    for match in matches:
        zh_text = match[0]
        en_text = match[1]
        current_text = match[2].strip()

        # 如果当前文本是中文（包含中文字符），则替换为英文
        if any('\u4e00' <= char <= '\u9fff' for char in current_text):
            # 替换为英文
            old_str = f' data-zh="{zh_text}" data-en="{en_text}">{current_text}<'
            new_str = f' data-zh="{zh_text}" data-en="{en_text}">{en_text}<'

            content = content.replace(old_str, new_str)
            changes += 1
            print(f"  ✓ Fixed: {current_text[:60]}...")

    # 保存文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Total changes: {changes}")
    return changes


def main():
    """主函数"""
    print("="*70)
    print("  Fixing Default Text in data-zh/data-en Tags")
    print("="*70)

    files = [
        'pages/about.html',
        'pages/events.html',
        'pages/programs.html',
        'pages/experts.html',
        'pages/partnership.html',
        'pages/contact.html',
    ]

    total_changes = 0

    for filepath in files:
        try:
            total_changes += fix_file(filepath)
        except Exception as e:
            print(f"  ✗ Error: {e}")

    print("\n" + "="*70)
    print(f"  Total changes: {total_changes}")
    print("="*70)


if __name__ == '__main__':
    main()
