#!/usr/bin/env python3
"""
清理重复的 data-zh 和 data-en 属性
"""

import re
import os

def fix_duplicate_attributes(filepath):
    """修复重复属性"""
    print(f"Cleaning: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 修复模式：data-zh="A" data-en="B" data-zh="A" data-en="C" -> data-zh="A" data-en="C"
    # 找到所有重复的 data-zh 和 data-en
    pattern = r'(\s+data-zh="[^"]+?"\s+data-en="[^"]+?")\s+data-zh="[^"]+?"\s+data-en="[^"]+?"\s*>'
    
    def replace_duplicate(match):
        # 保留第一组
        first_group = match.group(1)
        # 找到第二个 data-en 的值
        second_match = re.search(r'data-en="([^"]+?)"\s*$', match.group(0))
        if second_match:
            return f'{first_group} data-en="{second_match.group(1)}" >'
        return match.group(0)
    
    content = re.sub(pattern, replace_duplicate, content)
    
    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    changes = content != original_content
    print(f"  {'✓ Fixed' if changes else '✗ No changes'}\n")
    return changes


def main():
    """主函数"""
    pages_dir = 'pages'
    files = [
        'about.html',
        'events.html',
        'programs.html',
        'experts.html',
        'partnership.html',
        'contact.html',
    ]
    
    print("="*70)
    print("  Cleaning Duplicate Attributes")
    print("="*70)
    print()
    
    for filename in files:
        filepath = os.path.join(pages_dir, filename)
        if os.path.exists(filepath):
            fix_duplicate_attributes(filepath)
        else:
            print(f"  ✗ File not found: {filepath}\n")


if __name__ == '__main__':
    main()
