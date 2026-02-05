#!/usr/bin/env python3
"""
快速修复 index.html 导航栏默认文本
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# 修复导航栏链接
nav_fixes = [
    ('>首页<', ' data-zh="首页" data-en="Home">Home<'),
    ('>历史活动<', ' data-zh="历史活动" data-en="Events">Events<'),
    ('>活动策划<', ' data-zh="活动策划" data-en="Programs">Programs<'),
    ('>特邀专家<', ' data-zh="特邀专家" data-en="Experts">Experts<'),
    ('>行业合作<', ' data-zh="行业合作" data-en="Partnership">Partnership<'),
    ('>联系我们<', ' data-zh="联系我们" data-en="Contact">Contact<'),
]

for old, new in nav_fixes:
    if old in content:
        content = content.replace(old, new)
        changes += 1

# 保存
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Total changes: {changes}")
