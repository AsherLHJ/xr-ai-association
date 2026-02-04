#!/usr/bin/env python3
"""
完整的双语支持脚本
为所有二级页面添加完整的中英文翻译
"""

import re
import os

# 完整的翻译字典
translations = {
    # 页面标题和副标题
    '协会简介': 'About Us',
    'About Us': 'Association Introduction',
    '历史活动': 'Events',
    'Historical Activities': 'Our Events',
    '活动策划': 'Programs',
    'Events & Projects': 'Our Programs',
    '特邀专家': 'Featured Experts',
    'Expert Advisory': 'Our Experts',
    '行业合作': 'Partnership',
    'Industry Collaboration': 'Our Partners',
    '联系我们': 'Contact Us',
    'Get in Touch': 'Contact Information',

    # about.html - 协会简介
    '协会愿景': 'Association Vision',
    '我们致力于打造一个多元共创的社区，赋能港科广的每一位学子积极参与创新竞赛、跨学科合作与应用落地，推动科技与社会的深度融合。无论是虚拟世界的构建，还是现实世界的革新，这个平台将诞生属于港科广的引领未来科技先驱者。': 
        'We are committed to building a diverse and collaborative community, empowering every student at HKUST(GZ) to actively participate in innovation competitions, interdisciplinary collaboration, and application implementation, promoting the deep integration of technology and society. Whether it is building the virtual world or innovating in the real world, this platform will give birth to future technology pioneers belonging to HKUST(GZ).',

    # about.html - 玩学用三部曲
    '玩学用三部曲': 'Play-Learn-Apply Trilogy',
    '协会采用玩学用三部曲，从入门到进阶，契合会员情况与实践需求，助力学生在技术探索过程中，实现快速升级。': 
        'The association adopts the Play-Learn-Apply Trilogy, from entry to advanced, aligning with member situations and practical needs, helping students achieve rapid upgrades during their technology exploration journey.',
    
    '玩': 'Play',
    '通过沉浸式的XR体验，激发学生对技术的兴趣，在游戏中感受科技魅力。': 
        'Through immersive XR experiences, ignite students\' interest in technology and feel the charm of technology in games.',
    
    '学': 'Learn',
    '系统学习XR、AI等前沿技术，掌握理论基础和实践技能。': 
        'Systematically learn frontier technologies such as XR and AI, mastering theoretical foundations and practical skills.',
    
    '用': 'Apply',
    '将所学知识应用于实际项目，参与竞赛和活动，实现创新突破。': 
        'Apply learned knowledge to actual projects, participate in competitions and activities, and achieve innovative breakthroughs.',

    # about.html - 核心部门
    '核心部门': 'Core Departments',
    
    '学术/技术部': 'Academic/Technology Department',
    '与学术界或工业界的专家建立联系，共同组织学术讲座、技术培训': 
        'Establish connections with experts from academia or industry, jointly organize academic lectures and technical training.',
    
    '活动策划部': 'Event Planning Department',
    '策划和组织协会的各类活动，协调活动参与者，确保活动的顺利进行': 
        'Plan and organize various association activities, coordinate participants, and ensure smooth event execution.',
    
    '宣传运营部': 'Marketing Department',
    '负责协会的宣传，推广协会的活动和项目、维护协会共建形象': 
        'Responsible for association promotion, marketing activities and projects, and maintaining association image.',
    
    '伙伴关系部': 'Partnership Department',
    '与外部合作伙伴联系，为活动和项目提供支持，参加外部活动和会议': 
        'Connect with external partners, provide support for activities and projects, and participate in external events and conferences.',

    # about.html - 其他
    '成员合影': 'Team Photo',
    '联系我们': 'Contact Us',
    '欢迎有志之士加入我们，共同探索XR+AI的无限可能！': 
        'We welcome like-minded individuals to join us and explore the infinite possibilities of XR+AI!',

    # events.html - 历史活动
    'AI文化节': 'AI Culture Festival',
    '香港科技大学（广州）': 'HKUST(GZ)',
    '探索人工智能与文化的深度融合': 
        'Exploring the Deep Integration of Artificial Intelligence and Culture',
    
    'XR技术沙龙': 'XR Technology Salon',
    '港科广信息枢纽': 'HKUST(GZ) Information Hub',
    '分享XR领域的最新技术进展与应用案例': 
        'Sharing the Latest Technical Progress and Application Cases in the XR Field',
    
    '元宇宙工作坊': 'Metaverse Workshop',
    '港科广元宇宙与计算创意中心': 'HKUST(GZ) Metaverse and Computational Creativity Center',
    '学习元宇宙概念与开发技术': 
        'Learning Metaverse Concepts and Development Technologies',
    
    'VR设计挑战赛': 'VR Design Challenge',
    '港科广计算机媒体与艺术学域': 'HKUST(GZ) Computational Media and Arts',
    '激发创新设计思维': 
        'Inspiring Innovative Design Thinking',
    
    'AI与XR融合研讨会': 'AI and XR Integration Symposium',
    '港科广人工智能学域': 'HKUST(GZ) Artificial Intelligence Thrust',
    '探讨AI与XR技术融合的未来发展': 
        'Discussing the Future Development of AI and XR Technology Integration',

    # programs.html - 活动策划
    'XR创业孵化': 'XR Startup Incubation',
    '为XR领域创业者提供全方位支持，包括技术指导、资源对接、投资机会等，帮助初创团队快速成长。': 
        'Providing comprehensive support for XR entrepreneurs, including technical guidance, resource matching, investment opportunities, and helping startup teams grow quickly.',
    
    '产学研合作项目': 'Industry-Academia-Research Collaboration Projects',
    '与港科广的教授和实验室合作，开展前沿技术研究与开发，推动科技成果转化。': 
        'Collaborating with HKUST(GZ) professors and laboratories to conduct frontier technology research and development, promoting technology transfer.',

    # experts.html - 特邀专家
    '张康教授': 'Prof. Kang Zhang',
    '计算机媒体与艺术学域主任': 'Head of CMA',
    '• Fulbright 杰出学者，入选斯坦福全球前2%科学家（1960-2022）': 
        '• Fulbright Distinguished Scholar, Stanford World\'s Top 2% Scientist (1960-2022)',
    '• 聚焦视觉语言、美学计算、生成艺术等跨学科研究': 
        '• Focus on interdisciplinary research in visual languages, aesthetic computing, and generative art',
    '• 出版8本学术专著，发表100余篇论文，作品多次获国际艺术设计奖项': 
        '• Published 8 academic monographs, over 100 papers, works won multiple international art and design awards',
    
    '许彬教授': 'Prof. Bin Xu',
    '信息枢纽副院长': 'Vice Dean of Information Hub',
    '• 元宇宙与沉浸计算权威，香港科大元宇宙与计算创意中心主任': 
        '• Authority on metaverse and immersive computing, Director of Metaverse and Computational Creativity Center at HKUST',
    '• IEEE Fellow、英国皇家工程院国际院士、Academia Europaea 院士': 
        '• IEEE Fellow, International Fellow of the Royal Academy of Engineering, Academia Europaea Fellow',
    '• 发表450余篇论文，拥有30项欧盟及美国产业专利': 
        '• Published over 450 papers, holds 30 EU and US industry patents',
    
    '梁海宁教授': 'Prof. Haining Liang',
    '计算机媒体与艺术副教授': 'Associate Professor of CMA',
    '• 图形学专家，ACM SIGGRAPH Asia 论文委员会成员': 
        '• Graphics expert, member of ACM SIGGRAPH Asia Paper Committee',
    '• 致力于计算机图形、视觉计算、虚拟现实研究': 
        '• Dedicated to research in computer graphics, visual computing, and virtual reality',
    '• 发表多篇顶级会议论文，在图形学领域有重要影响力': 
        '• Published multiple top conference papers, has significant influence in the graphics field',
    
    '王宇阳教授': 'Prof. Yuyang Wang',
    '• 动态重建与几何处理专家': 
        '• Expert in dynamic reconstruction and geometric processing',
    '• 专注于3D视觉与虚拟现实技术': 
        '• Focus on 3D vision and virtual reality technologies',
    '• 在国际顶级会议发表多篇论文': 
        '• Published multiple papers at international top conferences',
    
    'Rachel Franz': 'Rachel Franz',
    '• 教育技术与交互设计专家': 
        '• Expert in educational technology and interaction design',
    '• 致力于XR技术在教育中的应用研究': 
        '• Dedicated to research on applications of XR technology in education',
    '• 拥有丰富的跨文化项目经验': 
        '• Rich cross-cultural project experience',
    
    '罗越': 'Luo Yue',
    '• XR创业先锋，创办多个VR/AR项目': 
        '• XR entrepreneurship pioneer, founded multiple VR/AR projects',
    '• 致力于将前沿技术转化为实际产品': 
        '• Dedicated to translating cutting-edge technologies into practical products',
    '• 拥有丰富的产业界经验': 
        '• Rich industry experience',
    
    '陈俊楠': 'Chen Junnan',
    '• 人工智能与机器学习专家': 
        '• Expert in artificial intelligence and machine learning',
    '• 专注于AI技术在XR领域的应用': 
        '• Focus on applications of AI technology in the XR field',
    '• 参与多个国家级科研项目': 
        '• Participated in multiple national-level scientific research projects',

    # partnership.html - 行业合作
    '一个连接XR+AI技术的产学研平台': 'An Industry-Academia-Research Platform Connecting XR+AI Technologies',
    '多元融合、开放协同，支持从短期共创项目到长期战略合作的多样合作模式，共同拓展科技的可能性，欢迎与我们沟通！': 
        'Diverse integration and open collaboration, supporting diverse cooperation models from short-term co-creation projects to long-term strategic partnerships, jointly expanding technological possibilities. We welcome communication with you!',
    
    '专业人才基础': 'Professional Talent Foundation',
    '港科广XR+AI协会成员具备扎实的前沿技术背景，涵盖计算机媒体与艺术、人工智能、计算机科学、数据科学等背景的本科生、硕士、博士、及创业团队。': 
        'HKUST(GZ) XR+AI Association members have solid frontier technology backgrounds, covering undergraduates, masters, PhDs, and entrepreneurial teams from fields such as Computational Media and Arts, Artificial Intelligence, Computer Science, Data Science, and more.',
    
    '跨领域实践能力': 'Cross-Disciplinary Practice Capabilities',
    '港科广独有的交叉学科结构，打破传统学院壁垒，鼓励跨专业联合实践，促进学生在项目中形成复合型能力。港科广XR+AI协会联动学生、教授、实验室、及行业资源，打造从技术探索到落地实践的产学研协作机制。': 
        'HKUST(GZ)\'s unique interdisciplinary structure breaks down traditional academic barriers, encourages cross-professional joint practice, and promotes the formation of composite capabilities in students during projects. The HKUST(GZ) XR+AI Association links students, professors, laboratories, and industry resources to create an industry-academia-research collaboration mechanism from technology exploration to practical application.',
    
    '多元合作形式': 'Diverse Cooperation Forms',
    
    '技术共创': 'Co-Creation',
    '讲座协办': 'Co-Organized Lectures',
    '实习推荐': 'Internship Recommendations',
    '项目对接': 'Project Matching',
    '竞赛合作': 'Competition Cooperation',
    
    '合作伙伴': 'Partners',
    '我们正在持续拓展国内外XR+AI领域的行业优秀合作伙伴，为港科广学子构建一个融合创意、技术、与产业的创新生态。': 
        'We are continuously expanding excellent industry partners in the domestic and international XR+AI fields, building an innovative ecosystem integrating creativity, technology, and industry for HKUST(GZ) students.',
    
    '港科广XR+AI协会于2025年加入ICXR组织，ICXR是全球领先的高校XR学生组织联盟，致力于推动扩展现实(XR)领域的多元会作与知识共享。联盟汇聚全球40余所高校XR社团，联合Meta、Google、NVIDIA等行业伙伴，举办丰富的线上线下活动，助力青年学者成长与创新。': 
        'HKUST(GZ) XR+AI Association joined the ICXR organization in 2025. ICXR is the world\'s leading alliance of university XR student organizations, committed to promoting diverse cooperation and knowledge sharing in the Extended Reality (XR) field. The alliance brings together XR clubs from over 40 universities worldwide, joining industry partners such as Meta, Google, and NVIDIA to hold rich online and offline activities, helping young scholars grow and innovate.',
    
    '期待与您合作': 'Looking Forward to Cooperating with You',
    '欢迎与 XR+AI 协会建立合作关系，共同探索 XR+AI 技术的无限可能！': 
        'We welcome establishing cooperative relationships with XR+AI Association to jointly explore the infinite possibilities of XR+AI technologies!',

    # contact.html - 联系我们
    '加入我们': 'Join Us',
    '无论你是对 XR 和 AI 技术充满热情的探索者，还是想要在实践中提升能力的求学者，XR+AI 协会都欢迎你的加入！': 
        'Whether you are an explorer passionate about XR and AI technologies, or a scholar seeking to improve your capabilities through practice, XR+AI Association welcomes you to join!',
    
    '学校': 'School',
    '香港科技大学（广州）': 'HKUST(GZ)',
    
    '邮箱': 'Email',
    '联系我们获取更多信息': 'Contact us for more information',
    
    '网站': 'Website',
    '持续更新我们的活动信息': 'Continuously update our event information',
    
    '社交媒体': 'Social Media',
    '关注我们的最新动态': 'Follow our latest updates',

    # 页脚
    '科技造梦 · 探索未知 · 突破极限': 'Technology Dreams · Exploring the Unknown · Breaking Boundaries',
}


def add_translations_to_file(filepath):
    """为文件添加翻译"""
    print(f"Processing: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 统计修改
    changes = 0
    
    # 处理每个翻译对
    for zh, en in translations.items():
        # 查找模式
        # 1. >中文文本<
        if f'>{zh}<' in content and f'data-en="{en}"' not in content[:content.find(f'>{zh}<')+200]:
            # 确保这不是已经翻译过的内容
            pattern = re.escape(f'>{zh}<')
            replacement = f' data-zh="{zh}" data-en="{en}">{zh}<'
            content = re.sub(pattern, replacement, content, count=1)
            changes += 1
            print(f"  ✓ Added: {zh[:50]}...")
        
        # 2. h2/h3/p 标签内的纯文本
        elif f'>{zh}</' in content:
            # 检查标签类型（h2, h3, p, span等）
            for tag in ['h2>', 'h3>', 'p>', 'span>']:
                if f'>{zh}</{tag}' in content:
                    # 检查是否已经翻译
                    pattern = f'>{zh}</{tag}'
                    if f'data-en="{en}"' not in content[max(0, content.find(pattern)-200):content.find(pattern)+200]:
                        replacement = f' data-zh="{zh}" data-en="{en}">{zh}</{tag}'
                        content = re.sub(re.escape(pattern), replacement, content, count=1)
                        changes += 1
                        print(f"  ✓ Added ({tag[:-1]}): {zh[:50]}...")
                        break
    
    # 保存文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Total changes: {changes}\n")
    return changes


def main():
    """主函数"""
    pages_dir = 'pages'
    files = [
        'about.html',
        'events.html',
        'programs.html',
        'experts.html',
        'partnership.html',
        'contact.html',
    ]
    
    print("="*70)
    print("  Adding Complete Bilingual Support to All Secondary Pages")
    print("="*70)
    print()
    
    total_changes = 0
    
    for filename in files:
        filepath = os.path.join(pages_dir, filename)
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
