// ============================================
// CLI Products Collection - Custom JavaScript
// ============================================

(function() {
  'use strict';

  // ===== 主题切换 =====
  function initThemeToggle() {
    const toggle = document.getElementById('theme-toggle');
    if (!toggle) return;

    // 保存主题偏好
    function setTheme(theme) {
      document.documentElement.setAttribute('data-color-mode', theme);
      localStorage.setItem('theme', theme);
    }

    // 切换主题
    toggle.addEventListener('click', function() {
      const currentTheme = document.documentElement.getAttribute('data-color-mode');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      setTheme(newTheme);
    });

    // 监听系统主题变化
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
      if (!localStorage.getItem('theme')) {
        setTheme(e.matches ? 'dark' : 'light');
      }
    });
  }

  // ===== 平滑滚动 =====
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
      anchor.addEventListener('click', function(e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  // ===== 代码复制按钮 =====
  function initCopyButton() {
    document.querySelectorAll('.highlight').forEach(function(block) {
      const button = document.createElement('button');
      button.className = 'copy-button';
      button.textContent = '复制';
      button.setAttribute('aria-label', '复制代码');

      button.addEventListener('click', function() {
        const code = block.querySelector('code').textContent;
        navigator.clipboard.writeText(code).then(function() {
          button.textContent = '已复制!';
          setTimeout(function() {
            button.textContent = '复制';
          }, 2000);
        });
      });

      block.style.position = 'relative';
      block.appendChild(button);
    });
  }

  // ===== 搜索增强 =====
  function initSearch() {
    const searchInput = document.getElementById('search-input');
    if (!searchInput) return;

    let searchTimeout;
    searchInput.addEventListener('input', function() {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(function() {
        // 触发 just-the-docs 搜索
        const event = new Event('input');
        searchInput.dispatchEvent(event);
      }, 300);
    });
  }

  // ===== 动画观察器 =====
  function initAnimations() {
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate-fade-in-up');
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.1 });

      document.querySelectorAll('.category-card, .tool-card, .stat-card').forEach(function(el) {
        observer.observe(el);
      });
    }
  }

  // ===== 外部链接标记 =====
  function initExternalLinks() {
    document.querySelectorAll('a[href^="http"]').forEach(function(link) {
      if (!link.hostname.includes(window.location.hostname)) {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
        if (!link.classList.contains('no-icon')) {
          link.classList.add('external-link');
        }
      }
    });
  }

  // ===== 移动端菜单 =====
  function initMobileMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const sideBar = document.querySelector('.side-bar');

    if (menuToggle && sideBar) {
      menuToggle.addEventListener('click', function() {
        sideBar.classList.toggle('open');
        this.setAttribute('aria-expanded',
          this.getAttribute('aria-expanded') === 'true' ? 'false' : 'true'
        );
      });

      // 点击外部关闭菜单
      document.addEventListener('click', function(e) {
        if (!sideBar.contains(e.target) && !menuToggle.contains(e.target)) {
          sideBar.classList.remove('open');
          menuToggle.setAttribute('aria-expanded', 'false');
        }
      });
    }
  }

  // ===== 返回顶部按钮 =====
  function initBackToTop() {
    const button = document.createElement('button');
    button.className = 'back-to-top';
    button.setAttribute('aria-label', '返回顶部');
    button.innerHTML = `
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="18 15 12 9 6 15"></polyline>
      </svg>
    `;

    document.body.appendChild(button);

    function toggleButton() {
      if (window.scrollY > 300) {
        button.classList.add('visible');
      } else {
        button.classList.remove('visible');
      }
    }

    button.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', toggleButton);
    toggleButton();
  }

  // ===== 工具表格增强 =====
  function enhanceToolTables() {
    document.querySelectorAll('table').forEach(function(table) {
      const wrapper = document.createElement('div');
      wrapper.className = 'table-wrapper';
      table.parentNode.insertBefore(wrapper, table);
      wrapper.appendChild(table);
    });
  }

  // ===== 初始化所有功能 =====
  function init() {
    initThemeToggle();
    initSmoothScroll();
    initCopyButton();
    initSearch();
    initAnimations();
    initExternalLinks();
    initMobileMenu();
    initBackToTop();
    enhanceToolTables();

    // 页面加载完成后添加动画类
    document.body.classList.add('loaded');
  }

  // DOM 加载完成后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
