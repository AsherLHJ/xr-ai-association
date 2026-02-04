// 等待 DOM 加载完成
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM Content Loaded');

    // 导航栏滚动效果
    const navbar = document.getElementById('navbar');
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.querySelector('.nav-menu');

    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // 移动端菜单切换
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }

    // 点击菜单项后关闭移动端菜单
    const menuItems = document.querySelectorAll('.nav-menu a');
    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            if (hamburger) hamburger.classList.remove('active');
            if (navMenu) navMenu.classList.remove('active');
        });
    });

    // 平滑滚动到锚点
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                const offsetTop = target.offsetTop - 70;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // 主题切换功能
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    
    // 从 localStorage 读取主题设置，默认为 light
    let currentTheme = localStorage.getItem('theme') || 'light';
    document.body.className = `${currentTheme}-mode`;
    updateThemeIcon(currentTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            if (currentTheme === 'light') {
                currentTheme = 'dark';
            } else {
                currentTheme = 'light';
            }
            
            document.body.className = `${currentTheme}-mode`;
            localStorage.setItem('theme', currentTheme);
            updateThemeIcon(currentTheme);
            
            console.log('Theme switched to:', currentTheme);
        });
    }

    function updateThemeIcon(theme) {
        if (themeIcon) {
            if (theme === 'light') {
                themeIcon.textContent = '☀️';
            } else {
                themeIcon.textContent = '🌙';
            }
        }
    }

    // 中英文切换功能
    const langToggle = document.getElementById('lang-toggle');
    const langText = document.getElementById('lang-text');
    
    // 从 localStorage 读取语言设置，默认为英文
    let currentLang = localStorage.getItem('language') || 'en';
    setLanguage(currentLang);

    if (langToggle) {
        langToggle.addEventListener('click', function() {
            currentLang = currentLang === 'zh' ? 'en' : 'zh';
            setLanguage(currentLang);
            localStorage.setItem('language', currentLang);
            
            console.log('Language switched to:', currentLang);
        });
    }

    function setLanguage(lang) {
        // 更新所有带有 data-zh 和 data-en 属性的元素
        const elements = document.querySelectorAll('[data-zh][data-en]');
        elements.forEach(element => {
            if (lang === 'zh') {
                element.textContent = element.dataset.zh;
            } else {
                element.textContent = element.dataset.en;
            }
        });

        // 更新按钮文本
        if (langText) {
            langText.textContent = lang === 'zh' ? 'EN' : '中';
        }

        // 更新 HTML lang 属性
        document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    }

    // 图片懒加载
    const lazyImages = document.querySelectorAll('img[data-src]');
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });

        lazyImages.forEach(function(img) {
            imageObserver.observe(img);
        });
    } else {
        lazyImages.forEach(function(img) {
            img.src = img.dataset.src;
        });
    }

    // 页面加载完成
    window.addEventListener('load', function() {
        console.log('Page loaded successfully');
        console.log('Current language:', currentLang);
        console.log('Current theme:', currentTheme);
    });

    // 导航栏活动状态
    const sections = document.querySelectorAll('section[id]');
    if (sections.length > 0) {
        window.addEventListener('scroll', function() {
            const scrollY = window.pageYOffset;

            sections.forEach(section => {
                const sectionHeight = section.offsetHeight;
                const sectionTop = section.offsetTop - 100;
                const sectionId = section.getAttribute('id');
                const navLink = document.querySelector(`.nav-menu a[href="${sectionId}"]`) ||
                                  document.querySelector(`.nav-menu a[href="../index.html${sectionId}"]`) ||
                                  document.querySelector(`.nav-menu a[href="#${sectionId}"]`);

                if (navLink) {
                    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                        navLink.classList.add('active');
                    } else {
                        navLink.classList.remove('active');
                    }
                }
            });
        });
    }

    console.log('✓ XR+AI Association website initialized!');
});

// 全局错误处理
window.addEventListener('error', function(event) {
    console.error('Global error:', event.error);
});
