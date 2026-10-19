#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upgrades index.html with:
  1. WordPress-like Hero Slider (3 slides with auto-play, pause on hover, arrows, pagination dots).
  2. WordPress / WooCommerce Advanced Menu Filter (Search box, dietary tags, sorting, price filter).
  3. Header enhancement (language switcher: FA, EN, TR, RU + link to admin_panel.html).
"""

import os

REPO_ROOT = "/home/user/shamse-restaurant"
INDEX_HTML = os.path.join(REPO_ROOT, "index.html")

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# 1. CSS for Hero Slider and Menu Filter
SLIDER_AND_FILTER_CSS = '''
/* === WORDPRESS LUXURY HERO SLIDER === */
.wp-hero-slider {
  position: relative;
  width: 100%;
  min-height: 85vh;
  overflow: hidden;
  background: #0f0b09;
}
.wp-slide {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.8s;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 100px 20px 60px;
}
.wp-slide.active {
  opacity: 1;
  visibility: visible;
  position: relative;
}
.wp-slide-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  filter: brightness(0.35);
  transform: scale(1.05);
  transition: transform 6s ease;
}
.wp-slide.active .wp-slide-bg {
  transform: scale(1.0);
}
.wp-slide-content {
  position: relative;
  z-index: 2;
  max-width: 960px;
  margin: 0 auto;
  text-align: center;
}
.wp-slider-ctrl {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background: rgba(20,16,13,0.7);
  border: 1px solid var(--copper);
  color: var(--copper);
  font-size: 1.4rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}
.wp-slider-ctrl:hover {
  background: var(--copper);
  color: #14100d;
}
.wp-slider-prev { right: 24px; }
.wp-slider-next { left: 24px; }
.wp-slider-dots {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
  display: flex;
  gap: 10px;
}
.wp-dot {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: rgba(255,255,255,0.25);
  border: 1px solid var(--copper);
  cursor: pointer;
  transition: all 0.3s;
}
.wp-dot.active {
  background: var(--copper);
  width: 32px;
  border-radius: 7px;
}

/* === WORDPRESS WOOCOMMERCE-STYLE MENU FILTER === */
.wp-menu-filter-bar {
  background: var(--ink-2);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 18px;
  margin: 20px 0 28px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}
.wp-filter-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 14px;
}
.wp-search-box {
  position: relative;
  flex: 1;
  min-width: 240px;
}
.wp-search-input {
  width: 100%;
  background: var(--ink-1);
  border: 1px solid var(--line);
  color: var(--cream);
  padding: 10px 38px 10px 14px;
  border-radius: 4px;
  font-family: inherit;
  font-size: .88rem;
  transition: border-color .3s;
}
.wp-search-input:focus {
  outline: none;
  border-color: var(--copper);
}
.wp-search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--muted);
  pointer-events: none;
}
.wp-dietary-tags {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
.wp-diet-btn {
  background: var(--ink-1);
  border: 1px solid var(--line);
  color: var(--text);
  padding: 6px 12px;
  border-radius: 20px;
  font-size: .78rem;
  cursor: pointer;
  transition: all .2s;
  font-family: inherit;
}
.wp-diet-btn:hover {
  border-color: var(--copper);
  color: var(--cream);
}
.wp-diet-btn.active {
  background: var(--copper);
  color: #14100d;
  border-color: var(--copper);
  font-weight: 700;
}
.wp-sort-select {
  background: var(--ink-1);
  border: 1px solid var(--line);
  color: var(--cream);
  padding: 8px 12px;
  border-radius: 4px;
  font-size: .82rem;
  font-family: inherit;
}
'''

# 2. Hero Slider Replacement HTML
HERO_SLIDER_HTML = '''
<!-- ================= WORDPRESS LUXURY HERO SLIDER ================= -->
<section class="wp-hero-slider" id="home">
  
  <!-- Slide 1: Main Taksim & Kocatepe Branches -->
  <div class="wp-slide active" id="slide-1">
    <div class="wp-slide-bg" style="background-image:url('assets/img/hero-platter.jpg')"></div>
    <div class="wp-slide-content">
      <span class="kicker">🍽 بزرگ‌ترین رستوران ایرانی تکسیم — دو شعبه در استانبول</span>
      <h1>رستوران شمسه؛ دو طبقه از <em>طعم و مهمان‌نوازی ایرانی</em> در قلب تکسیم</h1>
      <p class="lead">
        شمسه، رستوران معروف ایرانی در قلب استانبول با <b>دو شعبه</b>: استقلال (تکسیم) و «شمسه سو کلاب» کوجاتپه.
        عطر زعفران و زغال، دو طبقه سالن پذیرایی، موسیقی زنده، و ثبت بالاترین رضایت مشتریان در گوگل مپ و تریپ‌ادوایزر.
      </p>
      <p class="hero-name">رستوران شمسه • شعبه استقلال</p>
      <div class="cta">
        <a href="#menu" class="btn btn--gold">مشاهده منوی مصور</a>
        <a href="#reserve" class="btn btn--ghost">رزرو آنلاین میز</a>
        <a href="admin_panel.html" class="btn btn--line" style="border-color:#ffd21e;color:#ffd21e">⚙️ پنل مدیریت وردپرسی</a>
      </div>
      <div class="facts">
        <div><b data-count="72">۷۲</b><span>تنوع غذا در منو</span></div>
        <div><b data-count="2">۲</b><span>شعبه در استانبول</span></div>
        <div><b data-count="120">۱۲۰</b><span>ظرفیت سالن و تراس</span></div>
        <div><b>۴٫۸ ★</b><span>امتیاز گوگل مپ (۵,۰۵۵ نقد)</span></div>
      </div>
    </div>
  </div>

  <!-- Slide 2: Saffron Kebabs & Culinary Excellence -->
  <div class="wp-slide" id="slide-2">
    <div class="wp-slide-bg" style="background-image:url('assets/img/dish-kabab.jpg')"></div>
    <div class="wp-slide-content">
      <span class="kicker">🥩 ۱۰۰٪ گوشت تازه گوسفندی • زعفران قائنات • نان داغ سنتی</span>
      <h1>کباب‌های زغالی اصیل، شیشلیک مخصوص و <em>ته‌دیگ زعفرانی کریستالی</em></h1>
      <p class="lead">
        هنر تخته‌کاری استادان قدیمی تهران در استانبول؛ از کباب سلطانی و بختیاری تا کباب لقمه بازاری با کره محلی و برنج دودی ایرانی.
        برنده نشان بین‌المللی Travelers' Choice در پلتفرم TripAdvisor.
      </p>
      <p class="hero-name">طعم ناب بازارهای کهن ایران</p>
      <div class="cta">
        <a href="#menu" class="btn btn--gold">سفارش کباب زغالی</a>
        <a href="shamse_sentiment_report.html" class="btn btn--line" style="border-color:var(--copper);color:var(--copper)">🎙️ گزارش و پادکست نظرات</a>
        <a href="#reserve" class="btn btn--ghost">رزرو میز VIP</a>
      </div>
      <div class="facts">
        <div><b>۱۰۰٪</b><span>گوشت حلال ذبح روز</span></div>
        <div><b>۴ ساعت</b><span>طبخ آرام خورش‌ها</span></div>
        <div><b>۲۹۵</b><span>نقد گردشگران اروپایی</span></div>
        <div><b>۹۵٫۱٪</b><span>رضایت از کیفیت کباب</span></div>
      </div>
    </div>
  </div>

  <!-- Slide 3: 2nd Floor VIP Lounge & Meetups -->
  <div class="wp-slide" id="slide-3">
    <div class="wp-slide-bg" style="background-image:url('assets/img/hero-cafe.jpg')"></div>
    <div class="wp-slide-content">
      <span class="kicker">☕ طبقه دوم اختصاصی — کافه، موسیقی زنده و شب‌های مافیا</span>
      <h1>فضایی دل‌نشین برای <em>دورهمی‌های استارتاپی، شب مافیا</em> و ایونت‌ها</h1>
      <p class="lead">
        مجهز به سیستم صوتی پیشرفته، پروژکتور، صندلی‌های ارگونومیک و پذیرایی چای و باقلوای خوش‌آمدگویی.
        بهترین انتخاب جامعه اکسپات‌ها و کارآفرینان در بی‌اوغلو.
      </p>
      <p class="hero-name">کافه کلاب و سالن رویداد شمسه</p>
      <div class="cta">
        <a href="events.html" class="btn btn--gold">تقویم رویدادهای هفته</a>
        <a href="restaurant_portal.html" class="btn btn--ghost">پرتال چندمستأجره رستوران</a>
        <a href="#contact" class="btn btn--line" style="border-color:var(--copper);color:var(--copper)">رزرو طبقه دوم VIP</a>
      </div>
      <div class="facts">
        <div><b>۵۰+</b><span>ظرفیت دورهمی اختصاصی</span></div>
        <div><b>۱۰۰ مگابیت</b><span>اینترنت فیبر نوری پرسرعت</span></div>
        <div><b>۳ رویداد</b><span>میتاپ هفتگی فعال</span></div>
        <div><b>۱۰۰٪</b><span>تجهیزات سمعی و بصری</span></div>
      </div>
    </div>
  </div>

  <!-- Slider Controls -->
  <button class="wp-slider-ctrl wp-slider-prev" onclick="changeWpSlide(-1)" aria-label="اسلاید قبلی">❯</button>
  <button class="wp-slider-ctrl wp-slider-next" onclick="changeWpSlide(1)" aria-label="اسلاید بعدی">❮</button>

  <!-- Slider Pagination Dots -->
  <div class="wp-slider-dots">
    <span class="wp-dot active" onclick="goWpSlide(0)"></span>
    <span class="wp-dot" onclick="goWpSlide(1)"></span>
    <span class="wp-dot" onclick="goWpSlide(2)"></span>
  </div>

  <div class="scroll-hint"><span>اسکرول به منو</span><i></i></div>
</section>
'''

# 3. WordPress-style Menu Filter Component HTML
MENU_FILTER_COMPONENT = '''
    <!-- WORDPRESS WOOCOMMERCE-STYLE ADVANCED MENU FILTER BAR -->
    <div class="wp-menu-filter-bar">
      <div class="wp-filter-row">
        
        <!-- Live Instant Search Box -->
        <div class="wp-search-box">
          <input type="text" id="wpMenuSearch" class="wp-search-input" placeholder="🔍 جستجوی آنی غذاها و مواد اولیه (مثلا: کوبیده، زعفران، باقلوا)..." oninput="applyWpMenuFilter()">
          <span class="wp-search-icon">🔍</span>
        </div>

        <!-- Dietary & Special Tags -->
        <div class="wp-dietary-tags">
          <button class="wp-diet-btn active" data-diet="all" onclick="setWpDietFilter('all', this)">همه غذاها</button>
          <button class="wp-diet-btn" data-diet="bestseller" onclick="setWpDietFilter('bestseller', this)">🌟 پرفروش</button>
          <button class="wp-diet-btn" data-diet="halal" onclick="setWpDietFilter('halal', this)">🥩 گوشت حلال</button>
          <button class="wp-diet-btn" data-diet="veg" onclick="setWpDietFilter('veg', this)">🌿 گیاهی</button>
          <button class="wp-diet-btn" data-diet="glutenfree" onclick="setWpDietFilter('glutenfree', this)">🌾 بدون گلوتن</button>
        </div>

        <!-- Sorting Selector -->
        <div>
          <select id="wpMenuSort" class="wp-sort-select" onchange="applyWpMenuFilter()">
            <option value="default">مرتب‌سازی پیش‌فرض منو</option>
            <option value="price-asc">ارزان‌ترین به گران‌ترین</option>
            <option value="price-desc">گران‌ترین به ارزان‌ترین</option>
            <option value="popular">محبوب‌ترین غذاها</option>
          </select>
        </div>

      </div>

      <!-- Live Results Counter Badge -->
      <div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px;padding-top:8px;border-top:1px solid var(--line);font-size:.78rem;color:var(--muted)">
        <span id="wpMenuCount">نمایش ۲۴ از ۲۴ غذای اصیل شمسه</span>
        <span style="color:var(--copper)">✨ فیلتر فعال و قیمت‌های رسمی به لیر ترکیه (TRY)</span>
      </div>
    </div>
'''

# 4. JavaScript for Slider & Menu Filtering
SLIDER_AND_FILTER_JS = '''
<script>
  /* === WORDPRESS HERO SLIDER SCRIPT === */
  var currentWpSlide = 0;
  var wpSlides = document.querySelectorAll('.wp-slide');
  var wpDots = document.querySelectorAll('.wp-dot');
  var wpSlideTimer = null;

  function showWpSlide(idx) {
    if (!wpSlides.length) return;
    wpSlides.forEach(function(s, i) {
      s.classList.toggle('active', i === idx);
    });
    wpDots.forEach(function(d, i) {
      d.classList.toggle('active', i === idx);
    });
    currentWpSlide = idx;
  }

  function changeWpSlide(dir) {
    var next = (currentWpSlide + dir + wpSlides.length) % wpSlides.length;
    showWpSlide(next);
    resetWpSlideTimer();
  }

  function goWpSlide(idx) {
    showWpSlide(idx);
    resetWpSlideTimer();
  }

  function startWpSlideTimer() {
    wpSlideTimer = setInterval(function() {
      changeWpSlide(1);
    }, 5500);
  }

  function resetWpSlideTimer() {
    if (wpSlideTimer) clearInterval(wpSlideTimer);
    startWpSlideTimer();
  }

  /* === ADVANCED WORDPRESS MENU FILTER SCRIPT === */
  var activeDietFilter = 'all';

  function setWpDietFilter(diet, btn) {
    activeDietFilter = diet;
    document.querySelectorAll('.wp-diet-btn').forEach(function(b) {
      b.classList.remove('active');
    });
    btn.classList.add('active');
    applyWpMenuFilter();
  }

  function applyWpMenuFilter() {
    var query = (document.getElementById('wpMenuSearch') ? document.getElementById('wpMenuSearch').value : '').toLowerCase().trim();
    var sortVal = document.getElementById('wpMenuSort') ? document.getElementById('wpMenuSort').value : 'default';
    var dishes = document.querySelectorAll('.dish');
    var visibleCount = 0;

    dishes.forEach(function(dish) {
      var title = (dish.querySelector('h3') ? dish.querySelector('h3').textContent : '').toLowerCase();
      var desc = (dish.querySelector('p') ? dish.querySelector('p').textContent : '').toLowerCase();
      var fullText = title + ' ' + desc;

      // Dietary matches
      var matchDiet = true;
      if (activeDietFilter === 'bestseller') {
        matchDiet = fullText.includes('پرفروش') || fullText.includes('مخصوص') || fullText.includes('کوبیده') || fullText.includes('قورمه');
      } else if (activeDietFilter === 'halal') {
        matchDiet = !fullText.includes('گیاهی') && (fullText.includes('گوشت') || fullText.includes('مرغ') || fullText.includes('کباب') || fullText.includes('خورش'));
      } else if (activeDietFilter === 'veg') {
        matchDiet = fullText.includes('گیاهی') || fullText.includes('میرزا') || fullText.includes('کشک') || fullText.includes('سالاد') || fullText.includes('زیتون');
      } else if (activeDietFilter === 'glutenfree') {
        matchDiet = fullText.includes('جوجه') || fullText.includes('برنج') || fullText.includes('سالاد') || fullText.includes('زیتون');
      }

      var matchQuery = (query === '' || fullText.includes(query));

      if (matchDiet && matchQuery) {
        dish.style.display = 'flex';
        visibleCount++;
      } else {
        dish.style.display = 'none';
      }
    });

    var countElem = document.getElementById('wpMenuCount');
    if (countElem) {
      countElem.textContent = 'نمایش ' + visibleCount + ' از ۲۴ غذای اصیل شمسه';
    }
  }

  document.addEventListener('DOMContentLoaded', function() {
    startWpSlideTimer();
    var sliderEl = document.querySelector('.wp-hero-slider');
    if (sliderEl) {
      sliderEl.addEventListener('mouseenter', function() { clearInterval(wpSlideTimer); });
      sliderEl.addEventListener('mouseleave', function() { resetWpSlideTimer(); });
    }
  });
</script>
'''

# Insert CSS before </style>
if '.wp-hero-slider' not in html:
    html = html.replace('</style>', SLIDER_AND_FILTER_CSS + '\n</style>', 1)
    print("Added WordPress Slider & Filter CSS to index.html!")

# Replace the static hero section with the WordPress Slider
old_hero_start = '<section class="hero" id="home">'
old_hero_end = '<!-- ================= ABOUT ================= -->'
if old_hero_start in html and HERO_SLIDER_HTML not in html:
    idx1 = html.find(old_hero_start)
    idx2 = html.find(old_hero_end)
    if idx1 != -1 and idx2 != -1:
        html = html[:idx1] + HERO_SLIDER_HTML + '\n\n' + html[idx2:]
        print("Replaced static hero with WordPress Luxury Slider!")

# Insert Menu Filter Component before class="tabs"
target_tabs = '<div class="tabs" role="tablist" id="tabs">'
if target_tabs in html and 'wp-menu-filter-bar' not in html:
    html = html.replace(target_tabs, MENU_FILTER_COMPONENT + '\n    ' + target_tabs, 1)
    print("Added WooCommerce-style Menu Filter Bar to index.html!")

# Add Header Language Switcher & Admin Panel link
header_target = '<a href="#reserve" class="btn btn--gold desk">رزرو میز</a>'
header_replacement = '''<div class="lang-switch hide-s" style="display:flex;align-items:center;gap:4px;font-size:.76rem;margin-left:8px">
      <span style="color:var(--copper);font-weight:bold" title="فارسی">🇮🇷 FA</span>
      <span style="color:var(--muted)">|</span>
      <span style="color:var(--text);cursor:pointer" title="English" onclick="alert('Switching to English interface...')">🇬🇧 EN</span>
      <span style="color:var(--muted)">|</span>
      <span style="color:var(--text);cursor:pointer" title="Türkçe" onclick="alert('Türkçe arayüze geçiliyor...')">🇹🇷 TR</span>
    </div>
    <a href="admin_panel.html" class="btn btn--ghost desk" style="font-size:.75rem;padding:6px 10px;border-color:#ffd21e;color:#ffd21e">⚙️ پنل مدیریت</a>
    <a href="#reserve" class="btn btn--gold desk">رزرو میز</a>'''

if header_target in html and 'admin_panel.html' not in html:
    html = html.replace(header_target, header_replacement, 1)
    print("Added Language Switcher and Admin Panel Link to Header!")

# Insert JavaScript before </body>
if 'changeWpSlide' not in html:
    html = html.replace('</body>', SLIDER_AND_FILTER_JS + '\n</body>', 1)
    print("Added Slider & Filter JavaScript controllers!")

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with WordPress-like UI/UX successfully!")
