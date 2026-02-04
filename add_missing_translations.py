#!/usr/bin/env python3
"""
完整翻译脚本 - 修复所有未翻译的内容
"""

import os
import re

translations = {
    # programs.html - 策划描述
    '动态重建及应用元实验室（DREAMS），作为学校中央实验室之一，为全校师生提供体积视频、三维重建、数字人、VR/AR等方向研究与应用的服务与支持。': 
        'The Dynamic Reconstruction and Application Meta-Lab (DREAMS), as one of the school\'s central laboratories, provides services and support for faculty and students in areas such as volumetric video, 3D reconstruction, digital humans, VR/AR research and application.',
    
    '实验室配备全栈自主研发的光场重建系统和其他开发设备，为我校师生提供先进的设备支持，同时将向其他高校与业界开放，成为国内，乃至全世界范围内，首批将体积视频应用在各领域的单位，为学校在大湾区乃至全球的产学研合作提供助力。': 
        'The lab is equipped with a full stack of independently developed light field reconstruction systems and other development equipment, providing advanced equipment support for faculty and students, while opening up to other universities and industry, becoming one of the first units to apply volumetric video technology in various fields domestically and worldwide, providing assistance for the school\'s industry-academia-research cooperation in the Greater Bay Area and globally.',
    
    '实验室核心设备为全栈自主研发的光场重建系统。': 
        'The lab\'s core equipment is a full stack of independently developed light field reconstruction system.',
    
    '该系统使用球形部署的上百台超高精度工业相机及红外发射器构成数据采集矩阵，对阵列中的人/物进行环绕式同步数据采集(例如颜色、深度信息)，并基于布置在云端的算法进行自动化三维重建，从而生成连续三维立体模型组成的动态模型序列，也就是体积视频。': 
        'This system uses hundreds of ultra-high-precision industrial cameras and infrared emitters arranged in a spherical deployment to form a data acquisition matrix, performing surround synchronous data acquisition (e.g., color, depth information) on the people/objects in the scene, and based on algorithms deployed in the cloud, automatically performs 3D reconstruction, thereby generating dynamic model sequences composed of continuous 3D stereoscopic models, which is volumetric video.',
    
    'DREAMS Lab 为全校师生提供先进的XR+AI设备支持，包括光场重建系统、VR/AR设备、三维建模工作站等。': 
        'DREAMS Lab provides advanced XR+AI equipment support for faculty and students, including light field reconstruction systems, VR/AR devices, 3D modeling workstations, etc.',
    
    '实验室支持学生、教师和研究人员开展创新性研究项目，推动XR技术在教育、科研和产业应用的发展。': 
        'The lab supports students, teachers, and researchers in conducting innovative research projects, promoting the development of XR technology in education, research, and industrial applications.',
    
    '我们欢迎全校师生预约使用实验室设备，共同探索XR+AI的无限可能。': 
        'We welcome faculty and students to make appointments to use lab equipment and jointly explore the infinite possibilities of XR+AI.',
    
    '设备使用指南和预约流程详见实验室官网或联系我们获取更多信息。': 
        'For equipment usage guidelines and appointment procedures, please visit the lab\'s official website or contact us for more information.',
    
    # events.html - 活动描述（如果有遗漏）
    '港科广XR+AI协会Game Day+Lab Tour探索之旅吸引了超过100名同学与师生报名参与。': 
        'HKUST(GZ) XR+AI Association Game Day + Lab Tour exploration journey attracted over 100 students and faculty to sign up and participate.',
    
    '在实验室导览环节，大家分批走进元宇宙联合创新实验室与动态建模与应用元实验室，聆听导师讲解XR+AI技术的研发日常，零距离感受创新科技的魅力。': 
        'During the lab tour session, everyone visited the Metaverse Co-Innovation Lab and Dynamic Modeling and Application Meta-Lab in batches, listening to mentors explain the daily research and development of XR+AI technology, experiencing the charm of innovative technology up close.',
    
    '更有Vision Pro、Quest 3、Pico 4等XR设备可供体验，让大家切身体会XR技术的无限可能！': 
        'There are also XR devices such as Vision Pro, Quest 3, Pico 4 available for experience, allowing everyone to personally experience the infinite possibilities of XR technology!',
    
    '随后的XR游戏派对中，参与者可以自由体验四大类型的沉浸式游戏，包括射击、音乐、观影、模拟等热门玩法。': 
        'In the subsequent XR game party, participants can freely experience four types of immersive games, including shooting, music, watching, simulation, and other popular gameplay styles.',
    
    '经典游戏如《Super Hot》《Beat Saber》《Robo Recall》等，让大家在虚拟世界里尽情畅游，感受XR的沉浸式魅力！': 
        'Classic games such as "Super Hot", "Beat Saber", "Robo Recall" etc., allow everyone to roam freely in the virtual world and experience the immersive charm of XR!',
    
    '活动最后，大家在轻松愉悦的氛围中自由交流，结识志同道合的XR爱好者。': 
        'At the end of the event, everyone freely communicated in a relaxed and pleasant atmosphere, meeting like-minded XR enthusiasts.',
    
    '许多同学表示，通过本次活动不仅开拓了视野，还找到了科研合作的潜在伙伴，为未来的科技探索之路奠定了基础。': 
        'Many students stated that through this event, they not only broadened their horizons, but also found potential partners for research cooperation, laying the foundation for future technology exploration.',
}


def add_translations_to_file(filepath):
    """为文件添加翻译"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = 0
    
    for zh, en in translations.items():
        # 查找模式：>中文< 或 >中文</tag
        patterns = [
            f'>{zh}<',
        ]
        
        for pattern in patterns:
            if pattern in content:
                # 检查附近是否已经有 data-en 属性
                pattern_pos = content.find(pattern)
                check_before = content[max(0, pattern_pos - 50):pattern_pos + 100]
                
                if f'data-en="{en}"' not in check_before:
                    # 替换
                    replacement = pattern.replace('>', f' data-zh="{zh}" data-en="{en}">')
                    content = content.replace(pattern, replacement, 1)
                    changes += 1
                    print(f"  ✓ Added: {zh[:60]}...")
    
    # 保存
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Total changes: {changes}\n")
    return changes


def main():
    """主函数"""
    pages = [
        'pages/programs.html',
        'pages/events.html',
    ]
    
    print("="*70)
    print("  Adding Missing Translations")
    print("="*70)
    print()
    
    total_changes = 0
    
    for filepath in pages:
        if os.path.exists(filepath):
            total_changes += add_translations_to_file(filepath)
        else:
            print(f"  ✗ File not found: {filepath}\n")
    
    print("="*70)
    print(f"  Total translations added: {total_changes}")
    print("="*70)
    print()


if __name__ == '__main__':
    main()
