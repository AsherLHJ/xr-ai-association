#!/usr/bin/env python3
import re

# 修复导航栏重复问题
def fix_page(filename, active_link_text):
    print(f"Fixing {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 查找正确的导航栏部分（在navbar中，第一个nav-menu）
    # 首先找到navbar的开始
    navbar_start = content.find('<nav class="navbar"')
    if navbar_start == -1:
        print(f"  ERROR: navbar not found")
        return
    
    # 找到navbar的结束
    navbar_end = content.find('</nav>', navbar_start)
    if navbar_end == -1:
        print(f"  ERROR: </nav> not found")
        return
    navbar_end += 6
    
    navbar_content = content[navbar_start:navbar_end]
    
    # 2. 清理navbar内容中多余的nav-controls
    # 保留第一个nav-controls（在nav-menu之后），删除所有其他的
    lines = navbar_content.split('\n')
    cleaned_lines = []
    nav_controls_found = False
    
    for i, line in enumerate(lines):
        # 检查是否是nav-controls
        if '<div class="nav-controls">' in line:
            if not nav_controls_found:
                # 保留第一个
                cleaned_lines.append(line)
                nav_controls_found = True
            else:
                # 删除后续的nav-controls及其内容（多行）
                pass
        elif nav_controls_found and line.strip() and not line.strip().startswith('<') and not '</div>' in line:
            # 如果在删除nav-controls后的内容，也跳过
            pass
        elif nav_controls_found and line.strip().startswith('<'):
            # 检查是否是其他div的开始
            if '<div class="' in line:
                pass
            else:
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
    
    # 3. 更新navbar内容
    # 使用更简单的方法：找到nav-menu后，nav-controls前，删除中间所有多余的ul和div
    
    # 找到nav-controls（第一个）
    nav_controls_pos = navbar_content.find('<div class="nav-controls">')
    if nav_controls_pos == -1:
        print(f"  ERROR: nav-controls not found in navbar")
        return
    
    # 检查nav-controls之前是否有重复的</ul>
    before_controls = navbar_content[:nav_controls_pos]
    
    # 找到最后一个</ul>
    last_ul_pos = before_controls.rfind('</ul>')
    if last_ul_pos == -1:
        print(f"  ERROR: </ul> not found before nav-controls")
        return
    
    # 删除last_ul_pos之后，nav_controls_pos之前的所有内容（应该是空的或多余的）
    cleaned_navbar = navbar_content[:last_ul_pos+6] + navbar_content[nav_controls_pos:]
    
    # 4. 找到hamburger并确保它在正确的位置
    # hamburger应该在nav-controls之后，navbar结束之前
    hamburger_pos = cleaned_navbar.find('<div class="hamburger"')
    if hamburger_pos != -1:
        # 检查hamburger后面是否有</div>和</nav>
        hamburger_end = cleaned_navbar.find('</div>', hamburger_pos)
        if hamburger_end != -1:
            hamburger_end += 6
            # 检查之后是否有</nav>
            after_hamburger = cleaned_navbar[hamburger_end:]
            if '</nav>' in after_hamburger:
                nav_end_pos = hamburger_end + after_hamburger.find('</nav>') + 6
                # 提取完整的navbar
                final_navbar = cleaned_navbar[:nav_end_pos]
            else:
                final_navbar = cleaned_navbar
        else:
            final_navbar = cleaned_navbar
    else:
        final_navbar = cleaned_navbar
    
    # 5. 使用正则表达式删除navbar之外的重复nav-controls
    # 找到navbar结束后的内容
    after_navbar = content[navbar_end:]
    
    # 删除所有navbar之外的nav-controls（这些是误插入的）
    pattern = r'\s*<div class="nav-controls">.*?</div>\s*'
    after_navbar_cleaned = re.sub(pattern, '', after_navbar, flags=re.DOTALL)
    
    # 同样删除多余的</ul>标签
    pattern_ul = r'\s*</ul>\s*</div>\s*</div>\s*'
    after_navbar_cleaned = re.sub(pattern_ul, '', after_navbar_cleaned, flags=re.DOTALL)
    
    # 6. 拼接最终内容
    final_content = content[:navbar_start] + final_navbar + after_navbar_cleaned
    
    # 7. 写回文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"  ✓ Fixed {filename}")

# 修复所有四个页面
for page in ['programs.html', 'experts.html', 'partnership.html', 'contact.html']:
    fix_page(page, page)

print("\nAll files fixed!")
