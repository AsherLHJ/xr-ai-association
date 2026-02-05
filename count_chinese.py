#!/usr/bin/env python3
"""
统计 index.html 中还有多少中文
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 查找所有 >中文字符<
chinese_pattern = r'>[\u4e00-\u9fff]+<'

matches = re.findall(chinese_pattern, content)

print(f"Total Chinese text segments: {len(matches)}")
print("\nFirst 20 examples:")
for i, match in enumerate(matches[:20]):
    print(f"{i+1}. {match[1:50]}<")

# 查找 >用<
specific_pattern = '>用<'
count = content.count(specific_pattern)
print(f"\nSpecific '用' count: {count}")
