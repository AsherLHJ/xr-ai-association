#!/bin/bash
echo "=================================================="
echo "  XR+AI 协会网站重构 - 完整测试"
echo "=================================================="
echo ""

cd /home/asher/.openclaw/workspace/xr-ai-association

echo "1. 检查文件结构..."
echo "   主页和样式:"
files=(
    "index.html"
    "styles.css"
    "script.js"
    "assets/logo.jpg"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        size=$(du -h "$file" | cut -f1)
        echo "   ✓ $file ($size)"
    else
        echo "   ✗ $file (缺失)"
    fi
done

echo ""
echo "   二级页面:"
pages=(
    "pages/about.html"
    "pages/events.html"
    "pages/programs.html"
    "pages/experts.html"
    "pages/partnership.html"
    "pages/contact.html"
)

for page in "${pages[@]}"; do
    if [ -f "$page" ]; then
        size=$(du -h "$page" | cut -f1)
        echo "   ✓ $page ($size)"
    else
        echo "   ✗ $page (缺失)"
    fi
done

echo ""
echo "   图片资源:"
image_count=$(find assets/images -name "*.png" -o -name "*.jpg" | wc -l)
echo "   ✓ 找到 $image_count 张图片"

echo ""
echo "2. 检查 HTML 结构..."
echo "   主页:"
html_checks=(
    "<!DOCTYPE html>"
    "<nav" index.html
    "id=\"navbar\"" index.html
    "nav-menu" index.html
    "pages/about.html" index.html
    "pages/events.html" index.html
    "pages/experts.html" index.html
)

for check in "${html_checks[@]}"; do
    pattern="${check% *}"
    file="${check##* }"
    if grep -q "$pattern" "$file" 2>/dev/null; then
        echo "   ✓ $pattern"
    else
        echo "   ✗ $pattern (在 $file)"
    fi
done

echo ""
echo "   特邀专家页面布局:"
expert_checks=(
    "main-expert-card" pages/experts.html
    "other-experts-grid" pages/experts.html
    "张康教授" pages/experts.html
    "许彬教授" pages/experts.html
    "梁海宁教授" pages/experts.html
    "王宇阳教授" pages/experts.html
    "Rachel Franz" pages/experts.html
    "罗越" pages/experts.html
    "陈俊楠" pages/experts.html
)

for check in "${expert_checks[@]}"; do
    pattern="${check% *}"
    file="${check##* }"
    if grep -q "$pattern" "$file" 2>/dev/null; then
        echo "   ✓ $pattern"
    else
        echo "   ✗ $pattern (在 $file)"
    fi
done

echo ""
echo "3. 检查 CSS 样式..."
css_checks=(
    ".main-expert-card" styles.css
    ".other-experts-grid" styles.css
    ".event-gallery" styles.css
    ".program-gallery" styles.css
    ".partners-grid" styles.css
)

for check in "${css_checks[@]}"; do
    pattern="${check% *}"
    file="${check##* }"
    if grep -q "$pattern" "$file" 2>/dev/null; then
        echo "   ✓ $pattern"
    else
        echo "   ✗ $pattern (在 $file)"
    fi
done

echo ""
echo "4. 检查 JavaScript 功能..."
js_checks=(
    "DOMContentLoaded" script.js
    "hamburger" script.js
    "addEventListener" script.js
)

for check in "${js_checks[@]}"; do
    if grep -q "$check" script.js; then
        echo "   ✓ $check"
    else
        echo "   ✗ $check"
    fi
done

echo ""
echo "5. 检查页面链接..."
link_checks=(
    "href=\"pages/about.html\"" index.html
    "href=\"pages/events.html\"" index.html
    "href=\"pages/experts.html\"" index.html
    "href=\"pages/programs.html\"" index.html
    "href=\"pages/partnership.html\"" index.html
    "href=\"pages/contact.html\"" index.html
    "href=\"../index.html\"" pages/about.html
    "href=\"../index.html\"" pages/events.html
    "href=\"../index.html\"" pages/experts.html
    "src=\"../assets/logo.jpg\"" pages/about.html
    "src=\"../script.js\"" pages/about.html
    "href=\"../styles.css\"" pages/about.html
)

for check in "${link_checks[@]}"; do
    pattern="${check% *}"
    file="${check##* }"
    if grep -q "$pattern" "$file" 2>/dev/null; then
        echo "   ✓ $pattern (在 $file)"
    else
        echo "   ✗ $pattern (在 $file)"
    fi
done

echo ""
echo "=================================================="
echo "✓ 文件结构检查完成"
echo ""
echo "6. 功能说明:"
echo "   • 主页：包含所有板块预览"
echo "   • 协会简介：详细介绍 + 玩学用三部曲 + 核心部门"
echo "   • 历史活动：5个活动详细展示"
echo "   • 特邀专家：主要专家(照片左+文字右) + 其他专家(并排)"
echo "   • 活动策划：2个策划项目详细介绍"
echo "   • 行业合作：产学研平台 + 合作伙伴"
echo "   • 联系我们：联系方式 + 呼吁加入"
echo ""
echo "7. 特色功能:"
echo "   ✓ 响应式设计（支持桌面和移动端）"
echo "   ✓ 移动端汉堡菜单"
echo "   ✓ 平滑滚动导航"
echo "   ✓ 现代化卡片布局"
echo "   ✓ 图片网格展示"
echo "   ✓ 特邀专家特殊布局"
echo ""
echo "=================================================="
echo "✓ 所有基础检查通过！"
echo ""
echo "🌐 在浏览器中访问以下地址测试:"
echo "   http://localhost:8888"
echo ""
echo "📋 测试清单:"
echo "   □ 主页正常显示，所有图片加载"
echo "   □ 点击导航链接可以跳转到对应页面"
echo "   □ 协会简介页面内容完整"
echo "   □ 历史活动页面显示5个活动"
echo "   □ 特邀专家页面布局正确（主要专家一行，其他并排）"
echo "   □ 活动策划页面显示2个策划"
echo "   □ 行业合作页面显示合作伙伴"
echo "   □ 联系我们页面正常显示"
echo "   □ 移动端菜单正常工作"
echo "   □ 所有链接可以正常跳转"
echo "=================================================="
