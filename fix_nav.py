#!/usr/bin/env python3
import re

# 定义正确的导航栏菜单（通用）
base_nav_menu = '''            <ul class="nav-menu">
                <li><a href="../index.html" data-zh="首页" data-en="Home">首页</a></li>
                <li><a href="about.html" data-zh="协会简介" data-en="About">协会简介</a></li>
                <li><a href="events.html" data-zh="历史活动" data-en="Events">历史活动</a></li>
                <li><a href="programs.html" data-zh="活动策划" data-en="Programs">活动策划</a></li>
                <li><a href="experts.html" data-zh="特邀专家" data-en="Experts">特邀专家</a></li>
                <li><a href="partnership.html" data-zh="行业合作" data-en="Partnership">行业合作</a></li>
                <li><a href="contact.html" data-zh="联系我们" data-en="Contact">联系我们</a></li>
            </ul>
            <div class="nav-controls">
                <button class="lang-toggle" id="lang-toggle" title="切换语言 / Switch Language">
                    <span class="lang-icon">🌐</span>
                    <span class="lang-text" id="lang-text">中</span>
                </button>
                <button class="theme-toggle" id="theme-toggle" title="切换主题 / Switch Theme">
                    <span class="theme-icon" id="theme-icon">☀️</span>
                </button>
            </div>'''

# 定义每个页面的active类位置
active_config = {
    'programs.html': ('<a href="programs.html"', '<a href="programs.html" class="active"'),
    'experts.html': ('<a href="experts.html"', '<a href="experts.html" class="active"'),
    'partnership.html': ('<a href="partnership.html"', '<a href="partnership.html" class="active"'),
    'contact.html': ('<a href="contact.html"', '<a href="contact.html" class="active"'),
}

# 修复每个文件
for filename in ['programs.html', 'experts.html', 'partnership.html', 'contact.html']:
    print(f"Fixing {filename}...")
    
    # 读取文件
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到导航栏的开始和结束
    nav_start = content.find('<ul class="nav-menu">')
    if nav_start == -1:
        print(f"  ERROR: nav-menu not found in {filename}")
        continue
    
    # 找到对应的 </ul> 后面跟着 </div> nav-controls
    # 我们需要找到整个混乱的导航部分
    nav_menu_match = re.search(r'<ul class="nav-menu">.*?</ul>', content, re.DOTALL)
    
    if not nav_menu_match:
        print(f"  ERROR: nav-menu pattern not found in {filename}")
        continue
    
    nav_menu_end = nav_menu_match.end()
    
    # 查找 nav-controls（可能在错误的位置）
    nav_controls_start = content.find('<div class="nav-controls">')
    if nav_controls_start == -1:
        nav_controls_start = content.find('<div class="nav-controls"', nav_menu_end)
    
    if nav_controls_start != -1:
        nav_controls_end = content.find('</div>', nav_controls_start + 100)
        if nav_controls_end != -1:
            nav_controls_end += 6  # 包含 </div>
    
    # 找到 hamburger 的位置
    hamburger_pos = content.find('<div class="hamburger"')
    
    # 计算需要替换的部分
    replace_start = nav_start
    replace_end = hamburger_pos if hamburger_pos != -1 else nav_menu_end + 20
    
    # 创建正确的导航菜单
    nav_menu = base_nav_menu
    
    # 为当前页面添加 active class
    if filename in active_config:
        old_link, new_link = active_config[filename]
        nav_menu = nav_menu.replace(old_link, new_link)
    
    # 执行替换
    new_content = content[:replace_start] + nav_menu + '\n' + content[replace_end:]
    
    # 写回文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✓ Fixed {filename}")

print("\nAll files fixed!")
