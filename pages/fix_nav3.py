#!/usr/bin/env python3
import re

# 读取导航栏模板
with open('navbar_template.html', 'r', encoding='utf-8') as f:
    navbar_template = f.read()

# 定义每个页面的active类
active_config = {
    'programs.html': '<a href="programs.html" data-zh="活动策划" data-en="Programs">活动策划</a>',
    'experts.html': '<a href="experts.html" data-zh="特邀专家" data-en="Experts">特邀专家</a>',
    'partnership.html': '<a href="partnership.html" data-zh="行业合作" data-en="Partnership">行业合作</a>',
    'contact.html': '<a href="contact.html" data-zh="联系我们" data-en="Contact">联系我们</a>',
}

# 为每个页面创建正确的导航栏
for filename, active_link in active_config.items():
    print(f"Fixing {filename}...")
    
    # 创建带有active class的导航栏
    navbar = navbar_template.replace(active_link, active_link.replace('">', '" class="active">'))
    
    # 读取文件
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找并替换<nav>部分
    nav_start = content.find('<nav class="navbar"')
    if nav_start == -1:
        print(f"  ERROR: <nav> not found")
        continue
    
    nav_end = content.find('</nav>', nav_start)
    if nav_end == -1:
        print(f"  ERROR: </nav> not found")
        continue
    nav_end += 6  # 包含</nav>
    
    # 替换导航栏
    new_content = content[:nav_start] + navbar + content[nav_end:]
    
    # 写回文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Fixed {filename}")

print("\nAll files fixed!")
