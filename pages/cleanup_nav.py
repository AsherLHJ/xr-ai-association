#!/usr/bin/env python3
import re

def remove_duplicate_nav_controls(filename):
    print(f"Cleaning {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到navbar的开始和结束
    nav_start = content.find('<nav class="navbar"')
    if nav_start == -1:
        print(f"  ERROR: navbar not found")
        return
    
    nav_end = content.find('</nav>', nav_start)
    if nav_end == -1:
        print(f"  ERROR: </nav> not found")
        return
    nav_end += 6
    
    # 分离：navbar内容 + navbar之后的内容
    navbar_part = content[nav_start:nav_end]
    after_navbar = content[nav_end:]
    
    # 在navbar之后的内容中，删除所有nav-controls块
    # 匹配：<div class="nav-controls">...buttons...</div>
    pattern = r'\s*<div class="nav-controls">.*?</div>\s*'
    after_navbar_cleaned = re.sub(pattern, '', after_navbar, flags=re.DOTALL)
    
    # 拼接回去
    new_content = content[:nav_start] + navbar_part + after_navbar_cleaned
    
    # 写回文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Cleaned {filename}")

# 清理所有四个页面
for filename in ['programs.html', 'experts.html', 'partnership.html', 'contact.html']:
    remove_duplicate_nav_controls(filename)

print("\nAll files cleaned!")
