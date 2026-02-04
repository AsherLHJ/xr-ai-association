#!/usr/bin/env python3
"""
修复页面标题和副标题的翻译
"""

import re

pages = {
    'programs.html': {
        'title': ('活动策划', 'Programs'),
        'subtitle': ('Events & Projects', 'Our Programs'),
    },
    'experts.html': {
        'title': ('特邀专家', 'Featured Experts'),
        'subtitle': ('Expert Advisory', 'Our Experts'),
    },
    'partnership.html': {
        'title': ('行业合作', 'Partnership'),
        'subtitle': ('Industry Collaboration', 'Our Partners'),
    },
    'contact.html': {
        'title': ('联系我们', 'Contact Us'),
        'subtitle': ('Get in Touch', 'Contact Information'),
    },
}

for page, translations in pages.items():
    print(f"Processing {page}...")
    
    filepath = f'pages/{page}'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 修复标题
    title_zh, title_en = translations['title']
    old_title = f'<h1 class="page-title">{title_zh}</h1>'
    new_title = f'<h1 class="page-title" data-zh="{title_zh}" data-en="{title_en}">{title_zh}</h1>'
    
    if old_title in content:
        content = content.replace(old_title, new_title)
        print(f"  ✓ Added title translation: {title_zh}")
    
    # 修复副标题
    subtitle_zh, subtitle_en = translations['subtitle']
    old_subtitle = f'<p class="page-subtitle">{subtitle_zh}</p>'
    new_subtitle = f'<p class="page-subtitle" data-zh="{subtitle_zh}" data-en="{subtitle_en}">{subtitle_zh}</p>'
    
    if old_subtitle in content:
        content = content.replace(old_subtitle, new_subtitle)
        print(f"  ✓ Added subtitle translation: {subtitle_zh}")
    
    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print()

print("Done!")
