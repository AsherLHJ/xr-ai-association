#!/usr/bin/env python3
"""
补充翻译：events.html的活动标题和描述
"""

import os

events_translations = {
    # 活动标题
    '活动一：Rokid 线下工作坊': 'Event 1: Rokid Offline Workshop',
    '活动二：XR 探索之旅（Game Day+Lab Tour）': 'Event 2: XR Exploration Journey (Game Day + Lab Tour)',
    '活动三："逸界·光影未来"2025 AI 文化节': 'Event 3: "Ethereal Realm · Light & Shadow Future" 2025 AI Cultural Festival',
    '活动四：Surreality 扩展现实 AI 艺术展': 'Event 4: Surreality Extended Reality AI Art Exhibition',
    '活动五：香港 Visionairs 公司 VR 大空间互动叙事展览集体参观活动': 'Event 5: Hong Kong Visionairs VR Large-Scale Interactive Narrative Exhibition Group Visit',

    # 活动地点
    '元宇宙联合创新实验室 | 动态建模与应用元实验室': 'Metaverse Co-Innovation Lab | Dynamic Modeling and Application Meta-Lab',
    '香港中文大学（深圳）逸夫书院': 'Shaw College, The Chinese University of Hong Kong, Shenzhen',
    '香港': 'Hong Kong',

    # 活动引用
    '"建模逼真生动，仿佛身临其境。"——这是体验者们最一致的感受。': '"The modeling is vivid and lifelike, as if being there in person." — This is the most consistent feedback from participants.',

    # 页面副标题
    'Past Events': 'Our Events History',
}


def add_events_translations(filepath):
    """为events.html添加翻译"""
    print(f"Processing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = 0
    
    for zh, en in events_translations.items():
        # 查找 >中文文本< 或 >中文文本</
        patterns = [
            f'>{zh}<',
            f'>{zh}</',
        ]
        
        for pattern in patterns:
            if pattern in content and f'data-en="{en}"' not in content[max(0, content.find(pattern)-100):content.find(pattern)+100]:
                # 替换
                if pattern.endswith('</'):
                    tag_end = content[content.find(pattern)+len(pattern):content.find(pattern)+len(pattern)+3]  # 获取标签名
                    replacement = f' data-zh="{zh}" data-en="{en}">{zh}</{tag_end}'
                else:
                    replacement = f' data-zh="{zh}" data-en="{en}">{zh}<'
                
                content = content.replace(pattern, replacement, 1)
                changes += 1
                print(f"  ✓ Added: {zh[:60]}...")
    
    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Total changes: {changes}\n")
    return changes


if __name__ == '__main__':
    filepath = 'pages/events.html'
    if os.path.exists(filepath):
        print("="*70)
        print("  Adding Events Translations")
        print("="*70)
        print()
        add_events_translations(filepath)
    else:
        print(f"File not found: {filepath}")
