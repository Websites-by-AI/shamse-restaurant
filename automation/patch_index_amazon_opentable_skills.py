#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enriches index.html with:
  1. Amazon-Style Customer Rating Breakdown (Histogram bars 5-star to 1-star, Verified Diner Badges, Sentiment Keywords).
  2. Amazon-Style "Frequently Paired Together" (Chef's Signature Bundle: Kebab + Mirza Ghasemi + Saffron Tea).
  3. OpenTable / Resy-Style 1-Click Interactive Time Slot Pills & Seating Area Selector in #reserve with real-time urgency banner.
"""

import os

REPO_ROOT = "/home/user/shamse-restaurant"
INDEX_HTML = os.path.join(REPO_ROOT, "index.html")

with open(INDEX_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# 1. CSS for Amazon & OpenTable components
AMAZON_OPENTABLE_CSS = '''
/* === AMAZON-STYLE RATING BREAKDOWN & HISTOGRAM === */
.amazon-reviews-box {
  background: var(--ink-2);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 24px;
  margin: 24px 0 32px;
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 30px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}
@media (max-width: 768px) {
  .amazon-reviews-box { grid-template-columns: 1fr; gap: 20px; }
}
.amz-rating-left {
  text-align: center;
  border-left: 1px solid var(--line);
  padding-left: 20px;
}
@media (max-width: 768px) {
  .amz-rating-left { border-left: none; border-bottom: 1px solid var(--line); padding-bottom: 16px; padding-left: 0; }
}
.amz-big-star { font-size: 3.4rem; font-weight: 900; color: #ffd21e; line-height: 1; }
.amz-stars-visual { color: #ffd21e; font-size: 1.2rem; margin: 4px 0; }
.amz-hist-row {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: .82rem;
  margin-bottom: 7px;
}
.amz-bar-track {
  flex: 1;
  height: 10px;
  background: var(--ink-3);
  border-radius: 5px;
  overflow: hidden;
  position: relative;
}
.amz-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #ffd21e, var(--copper));
  border-radius: 5px;
}
.amz-keywords-cloud {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 14px;
}
.amz-key-tag {
  background: rgba(210,154,90,0.12);
  border: 1px solid var(--line-copper);
  color: var(--copper);
  padding: 3px 10px;
  border-radius: 14px;
  font-size: .76rem;
  font-weight: bold;
}

/* === AMAZON-STYLE FREQUENTLY PAIRED TOGETHER === */
.amz-bundle-card {
  background: linear-gradient(135deg, var(--ink-2) 0%, var(--ink-3) 100%);
  border: 1px solid var(--copper);
  border-radius: 8px;
  padding: 20px;
  margin: 28px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 18px;
}
.amz-bundle-items {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}
.amz-bundle-plus { color: var(--copper); font-size: 1.4rem; font-weight: 900; }
.amz-dish-thumb {
  background: var(--ink-1);
  border: 1px solid var(--line);
  padding: 8px 12px;
  border-radius: 6px;
  font-size: .8rem;
  text-align: center;
}

/* === OPENTABLE INTERACTIVE TIME SLOT PILLS === */
.opentable-slots-wrap {
  margin: 18px 0;
}
.ot-slot-pills {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-top: 8px;
}
.ot-pill {
  background: var(--ink-2);
  border: 1px solid var(--line-copper);
  color: var(--cream);
  padding: 8px 14px;
  border-radius: 20px;
  font-size: .82rem;
  cursor: pointer;
  transition: all .2s;
  font-family: inherit;
}
.ot-pill:hover, .ot-pill.active {
  background: var(--copper);
  color: #14100d;
  font-weight: 700;
  transform: translateY(-1px);
}
.ot-pill-hot {
  border-color: #ffd21e;
  color: #ffd21e;
}
.ot-seating-pills {
  display: flex;
  gap: 8px;
  margin-top: 8px;
  flex-wrap: wrap;
}
.ot-seat-btn {
  background: var(--ink-2);
  border: 1px solid var(--line);
  color: var(--text);
  padding: 6px 14px;
  border-radius: 4px;
  font-size: .8rem;
  cursor: pointer;
  transition: all .2s;
  font-family: inherit;
}
.ot-seat-btn.active {
  background: var(--copper);
  color: #14100d;
  font-weight: bold;
}
.ot-urgency-banner {
  background: rgba(229,115,115,0.12);
  border: 1px solid #ef4444;
  color: #fca5a5;
  padding: 8px 14px;
  border-radius: 4px;
  font-size: .78rem;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 16px;
}
'''

# 2. Amazon-style Rating Breakdown Component
AMAZON_REVIEWS_HTML = '''
    <!-- AMAZON-STYLE CUSTOMER RATINGS BREAKDOWN & HISTOGRAM -->
    <div class="amazon-reviews-box rev">
      
      <!-- Overall Rating Left Column -->
      <div class="amz-rating-left">
        <div style="font-size:.84rem;color:var(--muted)">امتیاز کلی مسافران</div>
        <div class="amz-big-star">۴٫۸</div>
        <div class="amz-stars-visual">★★★★★</div>
        <div style="font-size:.78rem;color:var(--cream);font-weight:bold">بر پایه ۵,۰۵۵ نقد تأییدشده</div>
        <div style="margin-top:10px">
          <span style="background:rgba(46,204,113,0.15);color:#2ecc71;border:1px solid #2ecc71;padding:2px 8px;border-radius:10px;font-size:.72rem">
            ✓ ۹۲٪ رضایت بدون اصطکاک
          </span>
        </div>
      </div>

      <!-- Rating Histogram Right Column -->
      <div>
        <div style="font-size:.84rem;color:var(--cream);font-weight:bold;margin-bottom:8px">
          توزیع درصد رضایت مهمانان (بر مبنای استانداردهای ارزیابی آمازون):
        </div>

        <div class="amz-hist-row">
          <span style="width:50px;color:#ffd21e">۵ ستاره</span>
          <div class="amz-bar-track"><div class="amz-bar-fill" style="width:82%"></div></div>
          <span style="width:36px;color:var(--muted);text-align:left">۸۲٪</span>
        </div>

        <div class="amz-hist-row">
          <span style="width:50px;color:#ffd21e">۴ ستاره</span>
          <div class="amz-bar-track"><div class="amz-bar-fill" style="width:12%"></div></div>
          <span style="width:36px;color:var(--muted);text-align:left">۱۲٪</span>
        </div>

        <div class="amz-hist-row">
          <span style="width:50px;color:#ffd21e">۳ ستاره</span>
          <div class="amz-bar-track"><div class="amz-bar-fill" style="width:4%"></div></div>
          <span style="width:36px;color:var(--muted);text-align:left">۴٪</span>
        </div>

        <div class="amz-hist-row">
          <span style="width:50px;color:var(--muted)">۲ ستاره</span>
          <div class="amz-bar-track"><div class="amz-bar-fill" style="width:1%"></div></div>
          <span style="width:36px;color:var(--muted);text-align:left">۱٪</span>
        </div>

        <div class="amz-hist-row">
          <span style="width:50px;color:var(--muted)">۱ ستاره</span>
          <div class="amz-bar-track"><div class="amz-bar-fill" style="width:1%"></div></div>
          <span style="width:36px;color:var(--muted);text-align:left">۱٪</span>
        </div>

        <!-- Sentiment Highlights (Amazon Customer Keywords) -->
        <div style="margin-top:14px;border-top:1px solid var(--line);padding-top:10px">
          <span style="font-size:.76rem;color:var(--muted)">محبوب‌ترین کلیدواژه‌های ثبت‌شده در نظرات:</span>
          <div class="amz-keywords-cloud">
            <span class="amz-key-tag">عطر زعفران و طعم اصیل کباب (۱,۸۴۰)</span>
            <span class="amz-key-tag">چای و باقلوای رایگان ولکام (۱,۴۲۰)</span>
            <span class="amz-key-tag">اتمسفر طبقه دوم VIP (۸۹۰)</span>
            <span class="amz-key-tag">برخورد صمیمی پرسنل (۷۶۰)</span>
            <span class="amz-key-tag">ته‌دیگ زعفرانی کریستالی (۶۵۰)</span>
          </div>
        </div>

      </div>

    </div>
'''

# 3. Amazon-style Frequently Paired Together Component
AMAZON_BUNDLE_HTML = '''
    <!-- AMAZON-STYLE FREQUENTLY PAIRED TOGETHER (CHEF'S SIGNATURE BUNDLE) -->
    <div class="amz-bundle-card rev">
      <div>
        <div style="display:inline-flex;align-items:center;gap:6px;background:rgba(210,154,90,0.18);color:var(--copper);padding:2px 8px;border-radius:10px;font-size:.72rem;font-weight:bold;margin-bottom:4px">
          🛒 سفارش تکمیلی هوشمند (Frequently Paired Together)
        </div>
        <h4 style="color:var(--cream);font-size:1.05rem;margin:0 0 4px">سینی ضیافت پیشنهادی سرآشپز شمسه (تخفیف پکیج دورهمی)</h4>
        <p style="font-size:.78rem;color:var(--muted);margin:0">ترکیب کباب کوبیده زعفرانی + پیش‌غذای میرزا قاسمی گیلانی + چای و باقلوای تازه</p>
      </div>

      <div class="amz-bundle-items">
        <div class="amz-dish-thumb">
          <b style="color:var(--cream)">کباب کوبیده</b>
          <div style="color:var(--copper);font-size:.75rem">۳۹۰ ₺</div>
        </div>
        <span class="amz-bundle-plus">+</span>
        <div class="amz-dish-thumb">
          <b style="color:var(--cream)">میرزا قاسمی</b>
          <div style="color:var(--copper);font-size:.75rem">۱۸۰ ₺</div>
        </div>
        <span class="amz-bundle-plus">+</span>
        <div class="amz-dish-thumb">
          <b style="color:var(--cream)">چای و باقلوا</b>
          <div style="color:#2ecc71;font-size:.75rem">رایگان (Welcome)</div>
        </div>

        <div style="margin-right:12px;text-align:left">
          <div style="font-size:.72rem;color:var(--muted);text-decoration:line-through">مجموع: ۵۷۰ ₺</div>
          <div style="font-size:1.15rem;font-weight:800;color:#ffd21e">۴۹۰ ₺ (تخفیف پکیج)</div>
          <button class="btn btn--gold" onclick="alert('پکیج ضیافت سرآشپز به سفارش شما اضافه شد!')" style="font-size:.74rem;padding:4px 10px;margin-top:4px">
            + افزودن یک‌کلیکه به سفارش
          </button>
        </div>
      </div>
    </div>
'''

# 4. OpenTable Interactive Time Slot Pills in #reserve
OPENTABLE_RESERVE_HTML = '''
        <!-- OPENTABLE-STYLE URGENCY BANNER -->
        <div class="ot-urgency-banner">
          <span>🔥</span>
          <span><b>تقاضای بالا در تکسیم:</b> در حال حاضر ۸ مهمان در حال بررسی میزهای امشب هستند. میانگین زمان تأیید رزرو: کمتر از ۳ دقیقه.</span>
        </div>

        <!-- OPENTABLE-STYLE 1-CLICK TIME SLOT PILLS -->
        <div class="opentable-slots-wrap">
          <label style="display:block;font-size:.82rem;font-weight:bold;color:var(--cream);margin-bottom:4px">
            ⏰ انتخاب سریع ساعت میز (OpenTable Time-Slots):
          </label>
          <div class="ot-slot-pills">
            <button type="button" class="ot-pill" onclick="selectOtTimeSlot('۱۲:۳۰', this)">۱۲:۳۰ (نهار)</button>
            <button type="button" class="ot-pill" onclick="selectOtTimeSlot('۱۴:۳۰', this)">۱۴:۳۰ (تخفیف ساعات خلوت)</button>
            <button type="button" class="ot-pill" onclick="selectOtTimeSlot('۱۹:۰۰', this)">۱۹:۰۰ (شام زودهنگام)</button>
            <button type="button" class="ot-pill ot-pill-hot" onclick="selectOtTimeSlot('۱۹:۳۰', this)">۱۹:۳۰ (فقط ۲ میز خالی ⚠️)</button>
            <button type="button" class="ot-pill" onclick="selectOtTimeSlot('۲۰:۳۰', this)">۲۰:۳۰ (موسیقی زنده)</button>
            <button type="button" class="ot-pill" onclick="selectOtTimeSlot('۲۱:۳۰', this)">۲۱:۳۰</button>
          </div>
        </div>

        <!-- SEATING AREA PREFERENCE -->
        <div style="margin-bottom:18px">
          <label style="display:block;font-size:.82rem;font-weight:bold;color:var(--cream);margin-bottom:4px">
            🪑 انتخاب موقعیت صندلی در شعبه:
          </label>
          <div class="ot-seating-pills">
            <button type="button" class="ot-seat-btn active" onclick="selectOtSeat('سالن اصلی همکف', this)">سالن اصلی همکف</button>
            <button type="button" class="ot-seat-btn" onclick="selectOtSeat('تراس روباز هوای آزاد', this)">تراس روباز</button>
            <button type="button" class="ot-seat-btn" onclick="selectOtSeat('طبقه دوم VIP و میتاپ', this)">طبقه دوم VIP رویدادها</button>
          </div>
        </div>
'''

# 5. Insert CSS
if '.amazon-reviews-box' not in html:
    html = html.replace('</style>', AMAZON_OPENTABLE_CSS + '\n</style>', 1)
    print("Added Amazon & OpenTable CSS to index.html!")

# 6. Insert Amazon Rating Breakdown into #reviews
reviews_target = '<!-- Multi-Platform Sentiment KPI Row -->'
if reviews_target in html and '<div class="amazon-reviews-box' not in html:
    # Find the end of the KPI row
    idx_kpi = html.find(reviews_target)
    # Search for the next </div> after the row
    idx_insert = html.find('</div>\n    </div>', idx_kpi)
    if idx_insert != -1:
        idx_insert += len('</div>\n    </div>')
        html = html[:idx_insert] + '\n\n' + AMAZON_REVIEWS_HTML + html[idx_insert:]
        print("Inserted Amazon-style Rating Breakdown into #reviews!")
    else:
        html = html.replace(reviews_target, AMAZON_REVIEWS_HTML + '\n    ' + reviews_target, 1)
        print("Inserted Amazon reviews box before KPI row!")

# 7. Insert Amazon Bundle Card into #menu
menu_target = '<div class="menu-grid">'
if menu_target in html and '<div class="amz-bundle-card' not in html:
    html = html.replace(menu_target, AMAZON_BUNDLE_HTML + '\n    ' + menu_target, 1)
    print("Inserted Amazon-style Frequently Paired Together bundle into #menu!")

# 8. Insert OpenTable Time Slot Pills into #reserve
form_target = '<form class="form rev" id="resForm" novalidate>'
if form_target in html and '<div class="opentable-slots-wrap">' not in html:
    html = html.replace(form_target, form_target + '\n' + OPENTABLE_RESERVE_HTML, 1)
    print("Inserted OpenTable time slots and urgency banner into #reserve!")


# 9. Add helper JavaScript for time slot and seating selection
JS_HELPERS = '''
<script>
  function selectOtTimeSlot(timeStr, btn) {
    document.querySelectorAll('.ot-pill').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    var timeSelect = document.getElementById('fTime');
    if (timeSelect) {
      for (var i = 0; i < timeSelect.options.length; i++) {
        if (timeSelect.options[i].text.includes(timeStr.split(' ')[0])) {
          timeSelect.selectedIndex = i;
          break;
        }
      }
    }
  }

  function selectOtSeat(seatStr, btn) {
    document.querySelectorAll('.ot-seat-btn').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    var typeSelect = document.getElementById('fType');
    if (typeSelect) {
      for (var i = 0; i < typeSelect.options.length; i++) {
        if (typeSelect.options[i].text.includes(seatStr.split(' ')[0])) {
          typeSelect.selectedIndex = i;
          break;
        }
      }
    }
  }
</script>
'''

if 'selectOtTimeSlot' not in html:
    html = html.replace('</body>', JS_HELPERS + '\n</body>', 1)
    print("Added OpenTable JavaScript handlers to index.html!")

with open(INDEX_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with Amazon & OpenTable conversion patterns successfully!")
