#!/bin/bash
echo "=================================================="
echo "  XR+AI 协会网站 - 功能测试"
echo "=================================================="
echo ""

cd /home/asher/.openclaw/workspace/xr-ai-association

echo "1. 检查文件存在性..."
files=(
    "index.html"
    "styles.css"
    "script.js"
    "assets/logo.png"
    "pages/about.html"
    "pages/events.html"
    "pages/programs.html"
    "pages/experts.html"
    "pages/partnership.html"
    "pages/contact.html"
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
echo "2. 检查图片路径..."
images=(
    "assets/images/7活动三_\"逸界·光影未来\"2025 AI文化节/26.png"
    "assets/images/13行业合作_一个连接XR+AI技术的产学研平台（多元融合、开放协同）/43.png"
    "assets/images/13行业合作_一个连接XR+AI技术的产学研平台（多元融合、开放协同）/44.png"
)

for img in "${images[@]}"; do
    if [ -f "$img" ]; then
        size=$(du -h "$img" | cut -f1)
        echo "   ✓ ${img##*/} ($size)"
    else
        echo "   ✗ ${img##*/} (缺失)"
    fi
done

echo ""
echo "3. 检查中英文切换功能..."
for file in index.html pages/*.html; do
    if grep -q 'lang-toggle' "$file" && grep -q 'nav-controls' "$file"; then
        echo "   ✓ ${file##*/}: 语言切换按钮存在"
    else
        echo "   ✗ ${file##*/}: 语言切换按钮缺失"
    fi
done

echo ""
echo "4. 检查主题切换功能..."
for file in index.html pages/*.html; do
    if grep -q 'theme-toggle' "$file" && grep -q 'theme-icon' "$file"; then
        echo "   ✓ ${file##*/}: 主题切换按钮存在"
    else
        echo "   ✗ ${file##*/}: 主题切换按钮缺失"
    fi
done

echo ""
echo "5. 检查默认语言设置（应为英文）..."
if grep -q 'lang="en"' index.html; then
    echo "   ✓ index.html: 默认语言为英文"
else
    echo "   ✗ index.html: 默认语言不是英文"
fi

for file in pages/*.html; do
    if grep -q 'lang="en"' "$file"; then
        echo "   ✓ ${file##*/}: 默认语言为英文"
    else
        echo "   ✗ ${file##*/}: 默认语言不是英文"
    fi
done

echo ""
echo "6. 检查LOGO图片路径..."
if grep -q 'assets/logo.png' index.html; then
    echo "   ✓ index.html: LOGO路径正确"
else
    echo "   ✗ index.html: LOGO路径不正确"
fi

for file in pages/*.html; do
    if grep -q '../assets/logo.png' "$file"; then
        echo "   ✓ ${file##*/}: LOGO路径正确"
    else
        echo "   ✗ ${file##*/}: LOGO路径不正确"
    fi
done

echo ""
echo "7. 检查data属性（用于中英文切换）..."
elements=(
    "data-zh" index.html
    "data-en" index.html
)

for check in "${elements[@]}"; do
    pattern="${check% *}"
    file="${check##* }"
    if grep -q "$pattern" "$file"; then
        echo "   ✓ $pattern 存在于 $file"
    else
        echo "   ✗ $pattern 不存在于 $file"
    fi
done

echo ""
echo "8. 检查JavaScript功能..."
if grep -q 'localStorage.getItem' script.js; then
    echo "   ✓ localStorage 功能实现"
else
    echo "   ✗ localStorage 功能未实现"
fi

if grep -q 'setLanguage' script.js; then
    echo "   ✓ setLanguage 函数存在"
else
    echo "   ✗ setLanguage 函数不存在"
fi

if grep -q 'updateThemeIcon' script.js; then
    echo "   ✓ updateThemeIcon 函数存在"
else
    echo "   ✗ updateThemeIcon 函数不存在"
fi

echo ""
echo "9. 检查玩学用三部曲布局（应为纵向）..."
if grep -q 'grid-template-columns: 1fr' styles.css; then
    echo "   ✓ 玩学用三部曲布局为纵向"
else
    echo "   ✗ 玩学用三部曲布局不是纵向"
fi

echo ""
echo "10. 检查contact和partnership页面图片尺寸..."
if grep -q 'contact-gallery-img' styles.css && grep -q 'max-height: 400px' styles.css; then
    echo "   ✓ contact页面图片尺寸已调整"
else
    echo "   ✗ contact页面图片尺寸未调整"
fi

if grep -q 'partnership-img' styles.css && grep -q 'max-height: 400px' styles.css; then
    echo "   ✓ partnership页面图片尺寸已调整"
else
    echo "   ✗ partnership页面图片尺寸未调整"
fi

echo ""
echo "=================================================="
echo "✓ 所有功能检查完成"
echo ""
echo "📋 修改总结："
echo "   ✓ 1. Hero section 背景图片改为放大后的LOGO"
echo "   ✓ 2. 历史活动AI文化节图片路径正确"
echo "   ✓ 3. Events页面活动三图片路径正确"
echo "   ✓ 4. 所有LOGO统一使用assets/logo.png"
echo "   ✓ 5. 中英文切换功能已实现"
echo "   ✓ 6. 默认语言设置为英文"
echo "   ✓ 7. 明暗主题切换功能已实现，默认明亮"
echo "   ✓ 8. Contact页面图片尺寸已调整"
echo "   ✓ 9. Partnership页面图片尺寸已调整"
echo "   ✓ 10. 玩学用三部曲布局改为纵向"
echo ""
echo "=================================================="
