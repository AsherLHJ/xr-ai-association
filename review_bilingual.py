#!/usr/bin/env python3
"""
完整的双语支持Review脚本
验证所有页面的默认语言和翻译覆盖
"""

import os
import re

def review_page(filepath, page_name):
    """审查单个页面"""
    print(f"\n{'='*70}")
    print(f"  Review: {page_name}")
    print('='*70)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 检查默认语言
    lang_match = re.search(r'<html\s+lang="([^"]+)"', content)
    default_lang = lang_match.group(1) if lang_match else "Not found"
    lang_ok = default_lang == 'en'
    print(f"\n1. Default Language: {'✓' if lang_ok else '✗'} {default_lang}")
    
    # 2. 检查语言和主题切换按钮
    has_lang_toggle = 'lang-toggle' in content
    has_theme_toggle = 'theme-toggle' in content
    print(f"2. Language Toggle Button: {'✓' if has_lang_toggle else '✗'} {'Present' if has_lang_toggle else 'Missing'}")
    print(f"3. Theme Toggle Button:   {'✓' if has_theme_toggle else '✗'} {'Present' if has_theme_toggle else 'Missing'}")
    
    # 3. 检查翻译数量
    zh_count = content.count('data-zh=')
    en_count = content.count('data-en=')
    print(f"\n4. Translation Coverage:")
    print(f"   - data-zh attributes: {zh_count}")
    print(f"   - data-en attributes: {en_count}")
    print(f"   - Consistent: {'✓' if zh_count == en_count else '✗'} ({zh_count} vs {en_count})")
    
    # 4. 检查重复属性
    duplicate_pattern = re.compile(r'data-zh="[^"]+?"\s+data-en="[^"]+?"\s+data-zh=')
    duplicates = len(duplicate_pattern.findall(content))
    print(f"\n5. Duplicate Attributes: {'✓' if duplicates == 0 else '✗'} {duplicates} found")
    
    # 5. 检查导航栏active类
    active_match = re.search(r'<li><a href="[^"]+"\s+class="active"[^>]*>([^<]+)</a></li>', content)
    if active_match:
        active_text = active_match.group(1)
        print(f"\n6. Active Navigation Link: ✓ '{active_text}'")
    else:
        print(f"\n6. Active Navigation Link: ✗ Not found")
    
    # 6. 检查关键内容是否已翻译
    untranslated = []
    key_elements = [
        ('<h1', 'Page Title'),
        ('<h2', 'Section Title'),
        ('<h3', 'Subsection Title'),
    ]
    
    print("\n7. Key Elements Translation Status:")
    for tag, desc in key_elements:
        # 查找该标签的所有元素
        matches = re.findall(f'{tag}[^>]*>([^<]+)</{tag[1:]}', content)
        untranslated_count = sum(1 for m in matches if 'data-zh=' not in content[max(0, content.find(m)-100):content.find(m)+100])
        status = '✓' if untranslated_count == 0 else '⚠'
        print(f"   {status} {desc}: {len(matches)} total, {untranslated_count} untranslated")
        if untranslated_count > 0:
            for m in matches:
                m_pos = content.find(m)
                if 'data-zh=' not in content[max(0, m_pos-100):m_pos+100]:
                    untranslated.append(f"   - {tag}: {m[:40]}...")
    
    # 总结
    print("\n" + "="*70)
    issues = []
    if not lang_ok:
        issues.append("Default language is not English")
    if not has_lang_toggle:
        issues.append("Language toggle button missing")
    if not has_theme_toggle:
        issues.append("Theme toggle button missing")
    if zh_count != en_count:
        issues.append(f"Translation count mismatch: {zh_count} vs {en_count}")
    if duplicates > 0:
        issues.append(f"Duplicate attributes found: {duplicates}")
    
    if issues:
        print(f"⚠ Issues Found: {len(issues)}")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✓ All checks passed!")
    print("="*70)
    
    return len(issues) == 0


def main():
    """主函数"""
    pages = [
        ('about.html', '协会简介 | About Us'),
        ('events.html', '历史活动 | Events'),
        ('programs.html', '活动策划 | Programs'),
        ('experts.html', '特邀专家 | Featured Experts'),
        ('partnership.html', '行业合作 | Partnership'),
        ('contact.html', '联系我们 | Contact'),
    ]
    
    print("\n" + "="*70)
    print("  COMPLETE BILINGUAL SUPPORT REVIEW")
    print("="*70)
    
    all_passed = True
    for filename, display_name in pages:
        filepath = os.path.join('pages', filename)
        if os.path.exists(filepath):
            passed = review_page(filepath, display_name)
            all_passed = all_passed and passed
        else:
            print(f"\n✗ File not found: {filepath}\n")
            all_passed = False
    
    print("\n" + "="*70)
    print("  OVERALL SUMMARY")
    print("="*70)
    print(f"\nStatus: {'✓ ALL PAGES READY' if all_passed else '⚠ SOME ISSUES FOUND'}")
    print()


if __name__ == '__main__':
    main()
