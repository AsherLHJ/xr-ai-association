#!/usr/bin/env python3
"""
为 events.html 添加活动五的翻译
"""

import re

# 读取文件
with open('pages/events.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 活动五的翻译
activity5_translations = [
    ('<p>本次活动走进三百年前"失落"的皇家花园，戴上 VR设备，可以瞬间穿越到太阳王路易十四的传奇园林。在皇家园林设计师安德烈·勒诺特尔的旁白引导下，漫步于皇家动物园，与火烈鸟、非洲象和孟加拉虎近距离相遇，甚至能与它们进行互动;迷失于迷宫林地，在每一个转角与静穆的雕塑不期而遇;最后登上水塔，看夕阳为整个花园镀上金边，欣赏细细的水柱萦绕的阿波罗与美人鱼雕像，感受历史与美学在虚拟世界中完美复活。</p>',
     '<p data-zh="本次活动走进三百年前"失落"的皇家花园，戴上 VR设备，可以瞬间穿越到太阳王路易十四的传奇园林。在皇家园林设计师安德烈·勒诺特尔的旁白引导下，漫步于皇家动物园，与火烈鸟、非洲象和孟加拉虎近距离相遇，甚至能与它们进行互动;迷失于迷宫林地，在每一个转角与静穆的雕塑不期而遇;最后登上水塔，看夕阳为整个花园镀上金边，欣赏细细的水柱萦绕的阿波罗与美人鱼雕像，感受历史与美学在虚拟世界中完美复活。" data-en="This event steps into the "lost" royal garden from 300 years ago. Wearing VR devices, you can instantly travel back to the legendary gardens of the Sun King Louis XIV. Under the narration guide of royal garden designer André Le Nôtre, stroll through the royal zoo, have close encounters with flamingos, African elephants, and Bengal tigers, and even interact with them; get lost in the maze woodland, unexpectedly meeting solemn sculptures at every corner; finally climb the water tower, watch the sunset gild the entire garden in gold, admire the Apollo and mermaid statues surrounded by fine water columns, feeling history and aesthetics perfectly revived in the virtual world.">本次活动走进三百年前"失落"的皇家花园，戴上 VR设备，可以瞬间穿越到太阳王路易十四的传奇园林。在皇家园林设计师安德烈·勒诺特尔的旁白引导下，漫步于皇家动物园，与火烈鸟、非洲象和孟加拉虎近距离相遇，甚至能与它们进行互动;迷失于迷宫林地，在每一个转角与静穆的雕塑不期而遇;最后登上水塔，看夕阳为整个花园镀上金边，欣赏细细的水柱萦绕的阿波罗与美人鱼雕像，感受历史与美学在虚拟世界中完美复活。</p>')
]

# 替换
for old, new in activity5_translations:
    if old in content:
        content = content.replace(old, new, 1)
        print(f"✓ Applied translation for Event 5")

# 保存
with open('pages/events.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ events.html updated successfully")
