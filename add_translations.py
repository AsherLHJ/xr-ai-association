#!/usr/bin/env python3
import re

# 翻译映射
translations = {
    # 通用
    '协会愿景': 'Association Vision',
    '我们致力于打造一个多元共创的社区，赋能港科广的每一位学子积极参与创新竞赛、跨学科合作与应用落地，推动科技与社会的深度融合。无论是虚拟世界的构建，还是现实世界的革新，这个平台将诞生属于港科广的引领未来科技先驱者。': 
        'We are committed to building a diverse and collaborative community, empowering every student at HKUST(GZ) to actively participate in innovation competitions, interdisciplinary collaboration, and application implementation, promoting the deep integration of technology and society. Whether it is building the virtual world or innovating in the real world, this platform will give birth to future technology pioneers belonging to HKUST(GZ).',
    
    # 玩学用三部曲
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
    
    # 核心部门
    '核心部门': 'Core Departments',
    
    '学术/技术部': 'Academic/Technology Department',
    '与学术界或工业界的专家建立联系，共同组织学术讲座、技术培训': 
        'Establish connections with experts from academia or industry, jointly organize academic lectures and technical training',
    
    '活动策划部': 'Event Planning Department',
    '策划和组织各类XR+AI相关活动，包括技术沙龙、工作坊、黑客松等': 
        'Plan and organize various XR+AI related activities, including technical salons, workshops, hackathons, etc.',
    
    '研究开发部': 'R&D Department',
    '负责XR+AI技术的研究与开发，推动技术创新': 
        'Responsible for research and development of XR+AI technologies, driving technological innovation',
    
    '教育培训部': 'Education Department',
    '组织技术讲座、工作坊，提升成员技术能力': 
        'Organize technical lectures and workshops to enhance members\' technical capabilities',
    
    '宣传运营部': 'Marketing Department',
    '负责协会的宣传，推广协会的活动和项目、维护协会共建形象': 
        'Responsible for association promotion, marketing activities and projects, maintaining association image',
    
    '项目管理部': 'Project Management',
    '管理协会项目，协调跨部门合作': 
        'Manage association projects and coordinate cross-department collaboration',
    
    '伙伴关系部': 'Partnership Department',
    '与外部合作伙伴联系，为活动和项目提供支持，参加外部活动和会议': 
        'Connect with external partners, provide support for activities and projects, participate in external events and conferences',
    
    # 联系信息
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
    
    # 行业合作
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
    
    # 特邀专家
    '特邀专家': 'Featured Experts',
    
    '张康教授': 'Prof. Kang Zhang',
    '计算机媒体与艺术学域主任': 'Head of CMA',
    '• Fulbright 杰出学者，入选斯坦福全球前2%科学家（1960-2022）': 
        '• Fulbright Distinguished Scholar, Stanford World\'s Top 2% Scientist (1960-2022)',
    '• 聚焦视觉语言、美学计算、生成艺术等跨学科研究': 
        '• Focus on interdisciplinary research in visual languages, aesthetic computing, and generative art',
    '• 出版8本学术专著，发表100余篇论文，作品多次获国际艺术设计奖项': 
        '• Published 8 academic monographs, over 100 papers, works won multiple international art and design awards',
    
    '许彬教授': 'Prof. Bin Xu',
    '信息枢纽副院长': 'Vice Dean of IHub',
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
}

def add_translations_to_file(filename):
    print(f"Adding translations to {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = 0
    
    # 为每个中文字符串查找并添加英文翻译
    for zh, en in translations.items():
        # 查找模式：>中文字符串< 或 >中文字符串" 或 data-zh="中文字符串"
        patterns = [
            (f'>{zh}<', f' data-zh="{zh}" data-en="{en}">{zh}<'),
            (f'"{zh}"', f' data-zh="{zh}" data-en="{en}">{zh}"'),
        ]
        
        for old, new in patterns:
            if old in content and f'data-en="{en}"' not in content[:content.find(old)+len(old)+100]:
                # 替换
                content = content.replace(old, new, 1)
                changes += 1
    
    # 保存
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Added {changes} translations to {filename}")
    return changes

# 处理所有二级页面
total_changes = 0
for filename in ['about.html', 'events.html', 'programs.html', 'experts.html', 'partnership.html', 'contact.html']:
    total_changes += add_translations_to_file(filename)

print(f"\n✓ Total translations added: {total_changes}")
