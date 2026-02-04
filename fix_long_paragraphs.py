#!/usr/bin/env python3
"""
修复 long paragraph 默认文本为英文
"""

# events.html 翻译
events_translations = {
    # Event 1
    '香港科技大学（广州）"Rokid: AI+AR双核驱动--重新定义多模态空间计算"线下工作坊圆满举办，信息枢纽计算媒体与艺术（CMA）学域副教授梁海宁邀请到Rokid全球开发者生态负责人赵维奇老师，分享如何通过AI与AR的双核驱动，推动开发者实现更智能的应用场景与商业化机遇。':
        'The Hong Kong University of Science and Technology (Guangzhou) successfully hosted the offline workshop "Rokid: AI+AR Dual-Core Drive - Redefining Multimodal Spatial Computing." Associate Professor Haining Liang from the Information Hub\'s Thrust of Computational Media and Arts (CMA) invited Mr. Zhao Weiqi, Rokid\'s Global Developer Ecology Head, to share how AI and AR dual-core drive empowers developers to achieve smarter application scenarios and commercialization opportunities.',

    '赵维奇老师（Rokid全球开发者生态负责人）在活动中深入分享了扩展现实（Extended Reality）的核心技术和应用案例。从XR基本概念、理解空间、双目渲染、虚实交互、到空间计算产品要素等角度，赵维奇老师以其丰富的行业经验为同学们揭开了XR技术的神秘面纱，提供了XR领域的更全面、深刻的见解。':
        'Mr. Zhao Weiqi (Rokid\'s Global Developer Ecology Head) deeply shared the core technologies and application cases of Extended Reality during the event. From perspectives such as XR basic concepts, understanding space, binocular rendering, virtual-real interaction, to spatial computing product elements, Mr. Zhao Weiqi, with his rich industry experience, unveiled the mysterious veil of XR technology for students, providing more comprehensive and profound insights into the XR field.',

    '在工作坊现场，同学们体验到了Rokid的三款AR眼镜，在多样化的交互方式中与虚拟内容进行感知、交互、协同，直观地感受到XR技术的魅力，不仅碰撞出许多天马行空的创意体验灵感，也与赵维奇老师展开交流了不同实现方案的技术性探讨。':
        'At the workshop site, students experienced Rokid\'s three AR glasses, perceiving, interacting, and collaborating with virtual content through diverse interaction methods, intuitively feeling the charm of XR technology. They not only sparked many imaginative creative experience inspirations but also engaged in technical discussions with Mr. Zhao Weiqi about different implementation solutions.',

    # Event 2
    '港科广XR+AI协会Game Day+Lab Tour探索之旅吸引了超过100名同学与师生报名参与。在实验室导览环节，大家分批走进元宇宙联合创新实验室与动态建模与应用元实验室，聆听导师讲解XR+AI技术的研发日常，零距离感受创新科技的魅力。更有Vision Pro、Quest 3、Pico 4等XR设备可供体验，让大家切身体会XR技术的无限可能！':
        'HKUST(GZ) XR+AI Association Game Day + Lab Tour exploration journey attracted over 100 students and faculty to sign up and participate. During the lab tour session, everyone visited the Metaverse Co-Innovation Lab and Dynamic Modeling and Application Meta-Lab in batches, listening to mentors explain the daily research and development of XR+AI technology, experiencing the charm of innovative technology up close. There are also XR devices such as Vision Pro, Quest 3, Pico 4 available for experience, allowing everyone to personally experience the infinite possibilities of XR technology!',

    '随后的XR游戏派对中，参与者可以自由体验四大类型的沉浸式游戏，包括射击、音乐、观影、模拟等热门玩法。经典游戏如《Super Hot》《Beat Saber》《Robo Recall》等，让大家在虚拟世界里尽情畅游，感受XR的沉浸式魅力！':
        'In the subsequent XR game party, participants can freely experience four types of immersive games, including shooting, music, watching, simulation, and other popular gameplay styles. Classic games such as "Super Hot", "Beat Saber", "Robo Recall", etc., allow everyone to roam freely in the virtual world and experience the immersive charm of XR!',

    '活动最后，大家在轻松愉悦的氛围中自由交流，结识志同道合的XR爱好者。许多同学表示，通过本次活动不仅开拓了视野，还找到了科研合作的潜在伙伴，为未来的科技探索之路奠定了基础。':
        'At the end of the event, everyone freely communicated in a relaxed and pleasant atmosphere, meeting like-minded XR enthusiasts. Many students stated that through this event, they not only broadened their horizons but also found potential partners for research cooperation, laying the foundation for future technology exploration.',

    # Event 3
    '香港科技大学（广州）XR+AI协会、动态重建及应用元实验室DREAMS Lab等代表人选，受邀参与了由香港中文大学（深圳）逸夫书院主办的"逸界·光影未来 AI超感嘉年华"2025 Shaw College AI Cultural Festival活动，与现场众多高校、师生团队一起探索AI与XR（扩展现实）融合下的无限可能！':
        'Representatives from the Hong Kong University of Science and Technology (Guangzhou) XR+AI Association, the Dynamic Reconstruction and Application Meta-Lab (DREAMS Lab), and others were invited to participate in the "Ethereal Realm · Light & Shadow Future AI Super-Sensing Carnival" 2025 Shaw College AI Cultural Festival hosted by Shaw College of The Chinese University of Hong Kong, Shenzhen, exploring the infinite possibilities of AI and XR (Extended Reality) fusion together with numerous universities, faculty, and student teams on site!',

    '本次"逸界·光影未来"文化节以AI科技为核心，涵盖主题论坛、未来脱口秀、光影表演、AI沉浸展厅等，旨在引发关于AI科技赋能生活、未来应用伦理等的广泛讨论。':
        'This "Ethereal Realm · Light & Shadow Future" cultural festival takes AI technology as the core, covering themed forums, future talk shows, light and shadow performances, AI immersive exhibition halls, etc., aiming to trigger extensive discussions on AI technology empowering life, future application ethics, and more.',

    '在活动现场的"虚实视界体验馆"展区，我们分享了多款由VR/AR设备打造的沉浸式互动体验，包括非遗主题的体积视频、3D镜框、AR互动产品等。吸引现场港中深本科、博士等同学们踊跃排队进行体验，佩戴设备亲身感受虚拟与显示融合的未来交互形式。':
        'At the "Virtual and Real Visual Experience Hall" exhibition area on site, we shared multiple immersive interactive experiences created by VR/AR devices, including intangible cultural heritage-themed volumetric videos, 3D frames, AR interactive products, etc. It attracted undergraduate and doctoral students from CUHK-Shenzhen to line up enthusiastically for experiences, wearing devices to personally feel the future interaction form of virtual and reality fusion.',

    '活动期间，港科广XR+AI协会代表成员与师生热情交流，详细介绍了XR技术与AI赋能教育、文化体验的前沿应用，现场讨论气氛十分踊跃。交流中，港中深逸夫书院院长及指导老师等都对未来跨校联动交流合作的可能性充满了热情与期待。':
        'During the event, HKUST(GZ) XR+AI Association representative members enthusiastically communicated with faculty and students, introducing in detail the frontier applications of XR technology and AI empowering education and cultural experiences. The on-site discussion atmosphere was very active. During the exchange, the Shaw College Dean and instructors of CUHK-Shenzhen were full of enthusiasm and expectation for the possibility of future cross-school linkage and exchange cooperation.',

    # Event 4
    '本次展览以"SURREALITY｜幻实之境"为题，展出的作品涵盖多种由人工智能参与创作的数字艺术形式，并融合扩展现实技术，使虚拟艺术品与真实校园场域深度叠加、无缝融合，营造出一场身临其境的科技艺术盛宴。':
        'This exhibition takes "SURREALITY | Realm of Illusion and Reality" as the theme, and the exhibited works cover various digital art forms created with artificial intelligence participation, integrating extended reality technology, deeply superimposing and seamlessly fusing virtual artworks with the real campus field, creating an immersive technology-art feast.',

    '在观展过程中，观众将亲历现实与虚拟、空间与数据之间错综复杂而富有灵理锚定与实时跟踪，为大规模混合现实场景提供精准的空间感知能力。此外，展览还搭载基于大语言模型的智能导览系统，并结合由动态知识图谱构建的叙事引擎，实动性的交互体验。':
        'During the viewing process, the audience will personally experience the intricate and spiritually anchored and real-time tracking between reality and virtuality, space and data, providing precise spatial perception capabilities for large-scale mixed reality scenes. In addition, the exhibition is equipped with an intelligent guide system based on large language models, combined with a narrative engine built from dynamic knowledge graphs, realizing dynamic interactive experiences.',

    '本次展览依托元宇宙与计算创意研究中心（MC2）自主研发的核心系统与技术平台得以实现。展览通过构建混合现实的人机交互体系，支持多种交互方式，实现虚拟与现实空间的动态联动，带来突破传统空间与功能限制的交互新维度。同时，借助多传感器融合的 SLAM（同步定位与地图构建）算法，实现数字内容与物理空间的高精度配准，支持虚拟物体的物现智能问答、语境化展示与个性化叙事生成，进一步拓展人机互动的智能性与情感表达的深度，为观众开启一场沉浸式、交互性与智能性兼具的感知之旅。':
        'This exhibition is realized relying on the core systems and technical platforms independently developed by the Metaverse and Computational Creativity Research Center (MC2). The exhibition realizes the dynamic linkage between virtual and real spaces by building a mixed reality human-computer interaction system, supporting multiple interaction methods, bringing a new dimension of interaction that breaks through traditional space and functional limitations. At the same time, with the help of multi-sensor fusion SLAM (Simultaneous Localization and Mapping) algorithms, high-precision registration between digital content and physical space is achieved, supporting virtual object-based intelligent Q&A, contextual display, and personalized narrative generation, further expanding the intelligence and emotional expression depth of human-computer interaction, opening an immersive, interactive, and intelligent perceptual journey for the audience.',

    # Event 5
    '本次活动走进三百年前"失落"的皇家花园，戴上 VR设备，可以瞬间穿越到太阳王路易十四的传奇园林。在皇家园林设计师安德烈·勒诺特尔的旁白引导下，漫步于皇家动物园，与火烈鸟、非洲象和孟加拉虎近距离相遇，甚至能与它们进行互动;迷失于迷宫林地，在每一个转角与静穆的雕塑不期而遇;最后登上水塔，看夕阳为整个花园镀上金边，欣赏细细的水柱萦绕的阿波罗与美人鱼雕像，感受历史与美学在虚拟世界中完美复活。':
        'This event steps into the "lost" royal garden from 300 years ago. Wearing VR devices, you can instantly travel back to the legendary gardens of the Sun King Louis XIV. Under the narration guide of royal garden designer André Le Nôtre, stroll through the royal zoo, have close encounters with flamingos, African elephants, and Bengal tigers, and even interact with them; get lost in the maze woodland, unexpectedly meeting solemn sculptures at every corner; finally climb the water tower, watch the sunset gild the entire garden in gold, admire the Apollo and mermaid statues surrounded by fine water columns, feeling history and aesthetics perfectly revived in the virtual world.',

    '"建模逼真生动，仿佛身临其境。"——这是体验者们最一致的感受。':
        '"The modeling is vivid and lifelike, as if being there in person." — This is the most consistent feedback from participants.',

    '"VR技术让历史变得触手可及，这种沉浸式体验令人震撼！"':
        '"VR technology makes history tangible, this immersive experience is stunning!"',

    '"不仅有视觉上的震撼，更有情感上的共鸣。"':
        '"Not only visual shock, but also emotional resonance."',

    # programs.html
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
    print("  Fixing Long Paragraphs")
    print("="*70)

    total_changes = 0
    # 只处理 events.html
    total_changes += fix_file('pages/events.html', events_translations)

    print("\n" + "="*70)
    print(f"  Total changes: {total_changes}")
    print("="*70)


if __name__ == '__main__':
    main()
