#!/usr/bin/env python3
"""
修复 programs.html 的长段落
"""

programs_translations = {
    '动态重建及应用元实验室（DREAMS），作为学校中央实验室之一，为全校师生提供体积视频、三维重建、数字人、VR/AR等方向研究与应用的服务与支持。实验室配备全栈自主研发的光场重建系统和其他开发设备，为我校师生提供先进的设备支持，同时将向其他高校与业界开放，成为国内，乃至全世界范围内，首批将体积视频应用在各领域的单位，为学校在大湾区乃至全球的产学研合作提供助力。':
        'The Dynamic Reconstruction and Application Meta-Lab (DREAMS), as one of the school\'s central laboratories, provides services and support for faculty and students in areas such as volumetric video, 3D reconstruction, digital humans, VR/AR research and application. The lab is equipped with a full stack of independently developed light field reconstruction systems and other development equipment, providing advanced equipment support for faculty and students, while opening up to other universities and industry, becoming one of the first units to apply volumetric video technology in various fields domestically and worldwide, providing assistance for the school\'s industry-academia-research cooperation in the Greater Bay Area and globally.',

    '实验室核心设备为全栈自主研发的光场重建系统。该系统使用球形部署的上百台超高精度工业相机及红外发射器构成数据采集矩阵，对阵列中的人/物进行环绕式同步数据采集(例如颜色、深度信息)，并基于布置在云端的算法进行自动化三维重建，从而生成连续三维立体模型组成的动态模型序列，也就是体积视频。':
        'The lab\'s core equipment is a full stack of independently developed light field reconstruction system. This system uses hundreds of ultra-high-precision industrial cameras and infrared emitters arranged in a spherical deployment to form a data acquisition matrix, performing surround synchronous data acquisition (e.g., color, depth information) on people/objects in the scene, and based on algorithms deployed in the cloud, automatically performs 3D reconstruction, thereby generating dynamic model sequences composed of continuous 3D stereoscopic models, which is volumetric video.',

    'DREAMS Lab 为全校师生提供先进的XR+AI设备支持，包括光场重建系统、VR/AR设备、三维建模工作站等。实验室支持学生、教师和研究人员开展创新性研究项目，推动XR技术在教育、科研和产业应用的发展。':
        'DREAMS Lab provides advanced XR+AI equipment support for faculty and students, including light field reconstruction systems, VR/AR devices, 3D modeling workstations, etc. The lab supports students, teachers, and researchers in conducting innovative research projects, promoting the development of XR technology in education, research, and industrial applications.',

    '我们欢迎全校师生预约使用实验室设备，共同探索XR+AI的无限可能。设备使用指南和预约流程详见实验室官网或联系我们获取更多信息。':
        'We welcome faculty and students to make appointments to use lab equipment and jointly explore the infinite possibilities of XR+AI. For equipment usage guidelines and appointment procedures, please visit the lab\'s official website or contact us for more information.',
}


def fix_file(filepath, translations):
    """修复单个文件"""
    print(f"\n=== Processing: {filepath} ===")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = 0

    # 替换长段落
    for zh_text, en_text in translations.items():
        if zh_text in content:
            content = content.replace(zh_text, en_text)
            changes += 1
            print(f"  ✓ Replaced: {zh_text[:80]}...")

    # 保存文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Total changes: {changes}")
    return changes


def main():
    """主函数"""
    print("="*70)
    print("  Fixing programs.html Long Paragraphs")
    print("="*70)

    total_changes = fix_file('pages/programs.html', programs_translations)

    print("\n" + "="*70)
    print(f"  Total changes: {total_changes}")
    print("="*70)


if __name__ == '__main__':
    main()
