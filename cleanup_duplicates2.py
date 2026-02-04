#!/usr/bin/env python3
"""
修复重复的 data-zh 和 data-en 属性
保留最后一组属性值
"""

import re
import os

def fix_duplicate_attributes(filepath):
    """修复重复属性"""
    print(f"Cleaning: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = 0
    
    # 查找所有重复的属性
    # 模式：data-zh="X" data-en="Y" data-zh="X" data-en="Z"
    pattern = r'(data-zh="[^"]+?"\s+data-en="[^"]+?")\s+data-zh="[^"]+?"\s+data-en="[^"]+?"\s*'
    
    def replace_duplicate(match):
        nonlocal changes
        first_group = match.group(1)  # 第一组 data-zh="X" data-en="Y"
        rest = match.group(0)  # 完整匹配
        
        # 找到第二个 data-en 的值
        second_en_match = re.search(r'data-en="([^"]+?)"\s*$', rest)
        if second_en_match:
            changes += 1
            # 返回：第一组的 data-zh + 第二组的 data-en
            return first_group.replace(r'data-en="[^"]+?"', f'data-en="{second_en_match.group(1)}"')
        return rest
    
    content = re.sub(pattern, replace_duplicate, content)
    
    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Fixed {changes} duplicate(s)\n")
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
    
    total_changes = 0
    
    for filename in files:
        filepath = os.path.join(pages_dir, filename)
        if os.path.exists(filepath):
            total_changes += fix_duplicate_attributes(filepath)
        else:
            print(f"  ✗ File not found: {filepath}\n")
    
    print("="*70)
    print(f"  Total duplicates fixed: {total_changes}")
    print("="*70)
    print()


if __name__ == '__main__':
    main()
