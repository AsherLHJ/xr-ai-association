#!/usr/bin/env python3
"""
本地测试脚本 - 验证所有功能
"""

import os
import subprocess
import urllib.request

def start_local_server():
    """启动本地服务器"""
    print("="*70)
    print("  Starting Local Server")
    print("="*70)
    print()

    os.chdir('/home/asher/.openclaw/workspace/xr-ai-association')

    # 启动服务器（后台）
    print("Starting HTTP server on port 8888...")
    print("Press Ctrl+C to stop the server")
    print()

    subprocess.Popen(['python3', '-m', 'http.server', '8888'],
                  stdout=subprocess.DEVNULL,
                  stderr=subprocess.DEVNULL)

    # 等待服务器启动
    import time
    time.sleep(2)

    print("✓ Server started on http://localhost:8888")
    print()

    return True


def test_pages():
    """测试所有页面"""
    print("="*70)
    print("  Testing All Pages")
    print("="*70)
    print()

    urls = [
        ('主页', 'http://localhost:8888/'),
        ('协会简介', 'http://localhost:8888/pages/about.html'),
        ('历史活动', 'http://localhost:8888/pages/events.html'),
        ('活动策划', 'http://localhost:8888/pages/programs.html'),
        ('特邀专家', 'http://localhost:8888/pages/experts.html'),
        ('行业合作', 'http://localhost:8888/pages/partnership.html'),
        ('联系我们', 'http://localhost:8888/pages/contact.html'),
    ]

    all_ok = True

    for name, url in urls:
        try:
            response = urllib.request.urlopen(url, timeout=5)
            status = response.status

            content = response.read().decode('utf-8')

            # 检查
            has_en = '<html lang="en">' in content
            has_zh = 'data-zh=' in content
            has_en_data = 'data-en=' in content
            has_lang_toggle = 'lang-toggle' in content
            has_theme_toggle = 'theme-toggle' in content

            checks = {
                'lang=en': has_en,
                'data-zh': has_zh,
                'data-en': has_en_data,
                'lang-toggle': has_lang_toggle,
                'theme-toggle': has_theme_toggle,
            }

            if all(checks.values()):
                print(f"✓ {name:8s} | All features OK")
            else:
                print(f"✗ {name:8s} | Some issues")
                for k, v in checks.items():
                    if not v:
                        print(f"  - Missing: {k}")
                all_ok = False

        except Exception as e:
            print(f"✗ {name:8s} | Error: {e}")
            all_ok = False

    print()
    print("="*70)
    if all_ok:
        print("✓✓✓ All tests passed!")
    else:
        print("✗ Some tests failed")
    print("="*70)
    print()

    return all_ok


def main():
    """主函数"""
    print("\n" + "="*70)
    print("  LOCAL TESTING & DEPLOYMENT GUIDE")
    print("="*70)
    print()

    print("This script will:")
    print("  1. Start a local web server")
    print("  2. Test all pages for bilingual support")
    print("  3. Provide deployment instructions")
    print()

    # 启动服务器
    start_local_server()

    # 测试页面
    test_ok = test_pages()

    # 部署指南
    print("\n" + "="*70)
    print("  DEPLOYMENT INSTRUCTIONS")
    print("="*70)
    print()

    print("Step 1: Create GitHub Repository")
    print("  1. Visit: https://github.com/new")
    print("  2. Repository name: xr-ai-association")
    print("  3. Click 'Create repository'")
    print()

    print("Step 2: Push to GitHub")
    print("  Run these commands:")
    print()
    print("  cd /home/asher/.openclaw/workspace/xr-ai-association")
    print("  git remote set-url origin https://YOUR_TOKEN@github.com/AsherLHJ/xr-ai-association.git")
    print("  git push -u origin main")
    print()

    print("Step 3: Deploy to Cloudflare Pages")
    print("  1. Visit: https://dash.cloudflare.com/pages")
    print("  2. Click 'Create a project'")
    print("  3. Click 'Connect to Git'")
    print("  4. Select xr-ai-association repository")
    print("  5. Leave all build settings empty (static site)")
    print("  6. Click 'Save and Deploy'")
    print()

    print("Step 4: Access Your Site")
    print("  Wait 1-2 minutes, then visit:")
    print("  https://xr-ai-association.pages.dev")
    print()

    print("="*70)
    print("  STATUS: " + ("✓ Ready to deploy" if test_ok else "⚠ Fix issues first"))
    print("="*70)
    print()

    if test_ok:
        print("✓ All tests passed! Ready to deploy to Cloudflare Pages.")
    else:
        print("✗ Some tests failed. Please fix issues before deploying.")
    print()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✓ Stopped by user")
    except Exception as e:
        print(f"\n\n✗ Error: {e}")
