#!/usr/bin/env python3
import re

def fix_duplicate_ul_tags(filename):
    print(f"Fixing {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换所有的</ul></ul>为</ul>
    # 这通常是expert-achievements的ul结束标签后的残留
    content = re.sub(r'</ul>\s*</ul>', '</ul>', content)
    
    # 写回文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Fixed {filename}")

# 修复所有四个页面
for filename in ['programs.html', 'experts.html', 'partnership.html', 'contact.html']:
    fix_duplicate_ul_tags(filename)

print("\nAll files fixed!")
