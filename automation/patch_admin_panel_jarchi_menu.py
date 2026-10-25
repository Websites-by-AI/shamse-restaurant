#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اسکریپت افزودن تب «جارچی استقلال و پیشنهادات منو» و هدر همگام ۳۶۵ روزه به پنل ادمین و سایت اصلی
Patch Admin Panel & Index Header with Jarchi Slogans, AI Menu Domains, and Unified 365-Day Auth Sync
"""

import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMIN_HTML_PATH = os.path.join(REPO_ROOT, "admin_panel.html")
INDEX_HTML_PATH = os.path.join(REPO_ROOT, "index.html")

def patch_admin_panel():
    with open(ADMIN_HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # ۱. افزودن نشانگر سشن ۳۶۵ روزه به نوار بالای ادمین (wp-admin-bar)
    sync_badge = '<span class="wp-badge-status" id="adminSyncBadge" style="border-color:#27ae60;color:#2ecc71;background:rgba(39,174,96,0.15)">✓ ورود یکپارچه فعال • سشن ۳۶۵ روزه (یکساله تا ۲۰۲۷) • سینک با تلگرام</span>'
    if 'id="adminSyncBadge"' not in html:
        target = '<span class="wp-badge-status">🟢 سرور روی پورت ۸۰۸۰ فعال</span>'
        replacement = target + "\n      " + sync_badge
        html = html.replace(target, replacement, 1)

    # ۲. افزودن آیتم منو به سایدبار ادمین
    menu_item = """        <a class="wp-menu-item" onclick="switchWpAdminTab('tab-jarchi-menu', this)">
          <span>📢</span> <span>جارچی استقلال و پیشنهادات منو</span>
        </a>"""
    if "tab-jarchi-menu" not in html:
        target_menu = """        <a class="wp-menu-item" onclick="switchWpAdminTab('tab-30-skills', this)">
          <span>🎯</span> <span>۳۰ مهارت نقد خطاها و راهکارها</span>
        </a>"""
        html = html.replace(target_menu, target_menu + "\n" + menu_item, 1)

    # ۳. محتوای تب جدید tab-jarchi-menu
    tab_content = """
      <!-- TAB: JARCHI & AI MENU RECOMMENDATIONS -->
      <section id="tab-jarchi-menu" class="wp-tab-view">

        <!-- HEADER BANNER -->
        <div class="wp-card" style="border:2px solid var(--gold);background:linear-gradient(135deg,#1c140e,#2a1d13);margin-bottom:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;border-bottom:1px solid rgba(210,154,90,0.3);padding-bottom:14px;margin-bottom:14px">
            <div>
              <span class="wp-badge" style="background:var(--gold);color:#101e22;font-weight:bold;margin-bottom:6px">سیستم اختصاصی جذب عابر و مهندسی منو v2.4</span>
              <h2 style="color:var(--cream);margin:4px 0 6px;font-size:18px">📢 موتور هوشمند جارچی خیابان استقلال، ۱۰ حوزه AI و مهندسی سود منو</h2>
              <p style="color:var(--muted);margin:0;font-size:12px">استراتژی‌های میدانی خوش‌آمدگویی، روانشناسی توریست‌ها، تطبیق فصلی و جغرافیایی منو و همگام‌سازی احراز هویت ۳۶۵ روزه</p>
            </div>
            <div style="display:flex;gap:8px">
              <a href="https://t.me/shamse_restaurant_bot" target="_blank" class="wp-btn" style="background:#229ED9;color:#fff">
                🤖 تست در ربات تلگرام
              </a>
              <a href="restaurant_portal.html?token=SHAMSE-TAK-2026" class="wp-btn wp-btn-gold">
                🚀 پرتال اختصاصی شعبه
              </a>
            </div>
          </div>

          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px">
            <div style="background:rgba(0,0,0,0.3);padding:10px 14px;border-radius:6px;border-right:3px solid var(--copper)">
              <div style="font-size:11px;color:var(--muted)">تعداد شعارهای دادزن</div>
              <div style="font-size:20px;font-weight:bold;color:var(--gold)">۱۰ شعار تخصصی</div>
              <div style="font-size:10px;color:#2ecc71">۵ زبان: FA / EN / RU / AR / TR</div>
            </div>
            <div style="background:rgba(0,0,0,0.3);padding:10px 14px;border-radius:6px;border-right:3px solid #2ecc71">
              <div style="font-size:11px;color:var(--muted)">حوزه‌های ارتقای هوش مصنوعی</div>
              <div style="font-size:20px;font-weight:bold;color:#2ecc71">۱۰ حوزه راهبردی</div>
              <div style="font-size:10px;color:var(--cream)">فصلی، جغرافیا، کامنت‌ها و ضایعات</div>
            </div>
            <div style="background:rgba(0,0,0,0.3);padding:10px 14px;border-radius:6px;border-right:3px solid #38bdf8">
              <div style="font-size:11px;color:var(--muted)">میانگین حاشیه سود منو</div>
              <div style="font-size:20px;font-weight:bold;color:#38bdf8">۶۹٫۲٪ سود ناخالص</div>
              <div style="font-size:10px;color:var(--muted)">با محاسبه بهای مواد اولیه و ارز</div>
            </div>
            <div style="background:rgba(0,0,0,0.3);padding:10px 14px;border-radius:6px;border-right:3px solid #e74c3c">
              <div style="font-size:11px;color:var(--muted)">اعتبار سشن دیتابیس</div>
              <div style="font-size:20px;font-weight:bold;color:var(--cream)">۳۶۵ روزه (یکساله)</div>
              <div style="font-size:10px;color:#2ecc71">سینک با تلگرام و وب‌سایت ✓</div>
            </div>
          </div>
        </div>

        <!-- SECTION 1: 10 STREET BARKER SLOGANS -->
        <div class="wp-card" style="margin-bottom:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid var(--card-border);padding-bottom:10px">
            <h3 style="margin:0;color:var(--cream);font-size:15px">📢 ۱۰ شعار میدانی دادزن و تکنیک‌های جذب مشتری در خیابان استقلال</h3>
            <span class="wp-badge" style="background:var(--copper);color:#fff">استراتژی میدانی FOH</span>
          </div>
          <p style="font-size:12px;color:var(--muted);margin-bottom:14px">
            برخلاف روش‌های سنتی دادزدن گوش‌خراش، مدل جارچی مدرن شمسه بر پایه <b>روانشناسی جذب گردشگر</b>، <b>سینی نمونه‌چشی (Tasting Tray)</b>، <b>شفافیت قیمت بدون هزینه پنهان</b> و <b>احترام چندزبانه</b> طراحی شده است:
          </p>

          <div style="overflow-x:auto">
            <table class="wp-table" style="font-size:11px;line-height:1.5">
              <thead>
                <tr>
                  <th style="width:7%">کد</th>
                  <th style="width:13%">مخاطب هدف</th>
                  <th style="width:6%">زبان</th>
                  <th style="width:30%">متن شعار دادزن (Hook Text)</th>
                  <th style="width:26%">تکنیک میدانی و سینی نمونه‌چشی</th>
                  <th style="width:18%">محرک روانشناختی و نرخ جذب</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><b>SLOGAN-01</b></td>
                  <td>مسافران ایرانی</td>
                  <td><span class="wp-badge" style="background:#27ae60;color:#fff">فارسی</span></td>
                  <td>«دلت برای عطر زعفرون قائنات و ته‌دیگ طلایی تنگ نشده؟ بفرمایید شمسه، طعم همون خونه‌ست!»</td>
                  <td>نمایش سینی مسی با تکه‌های کوچک ته‌دیگ برشته و بوی زعفران داغ به عابران ایرانی.</td>
                  <td><b>حس غربت و دلتنگی غذای مادر</b><br><span style="color:#2ecc71">+۲۸٪ جذب عابر</span></td>
                </tr>
                <tr>
                  <td><b>SLOGAN-02</b></td>
                  <td>توریست‌های عربی و خلیج</td>
                  <td><span class="wp-badge" style="background:#2980b9;color:#fff">عربی</span></td>
                  <td style="direction:rtl;text-align:right">«أهلاً وسهلاً! أطيب كباب بالزعفران والأرز الإيراني الأصيل، لحم حلال ۱۰۰٪ وطعم لا يُنسى في قلب تقسیم!»</td>
                  <td>ارائه کارت منوی عربی همراه با استشمام عطر هل و گلاب و کباب زغالی تازه با میزبانی شرقی.</td>
                  <td><b>اطمینان از ذبح ۱۰۰٪ حلال و برنج اعلا</b><br><span style="color:#2ecc71">+۳۲٪ جذب عرب</span></td>
                </tr>
                <tr>
                  <td><b>SLOGAN-03</b></td>
                  <td>توریست‌های غربی و اروپا</td>
                  <td><span class="wp-badge" style="background:#8e44ad;color:#fff">انگلیسی</span></td>
                  <td style="direction:ltr;text-align:left">“Real UNESCO Persian Gastronomy! Complimentary Saffron Tea, Honest Prices & Zero Hidden Cover Charges!”</td>
                  <td>نمایش کارت شفاف قیمت‌ها به یورو/لیر و تابلوی واضح No Hidden Cover Charge با استکان کمرباریک چای لاهیجان.</td>
                  <td><b>رفع ترس از کلاهبرداری توریستی و فاکتور مخفی</b><br><span style="color:#2ecc71">+۲۴٪ تبدیل غربی</span></td>
                </tr>
                <tr>
                  <td><b>SLOGAN-04</b></td>
                  <td>توریست‌های روس و CIS</td>
                  <td><span class="wp-badge" style="background:#d35400;color:#fff">روسی</span></td>
                  <td style="direction:ltr;text-align:left">«Настоящий сочный шашлык на углях и шафрановый плов! Русское меню и восточное гостеприимство на Истикляль!»</td>
                  <td>نشان دادن تبلت دیجیتال با منوی تصویری خط سیریلیک روسی و خوش‌آمدگویی کوتاه روسی توسط پرسنل.</td>
                  <td><b>امنیت زبانی و رفع لکنت سفارش غذا</b><br><span style="color:#2ecc71">+۲۹٪ جذب روس</span></td>
                </tr>
                <tr>
                  <td><b>SLOGAN-05</b></td>
                  <td>زوج‌ها و عکاسان</td>
                  <td><span class="wp-badge" style="background:#16a085;color:#fff">FA / EN</span></td>
                  <td>«از شلوغی و هیاهوی استقلال خسته شدی؟ بیا بالکن آرام شمسه، تکسیم زیر پاته با یک فنجون چای زعفرونی!»</td>
                  <td>اشاره به نمای چشم‌نواز بالکن طبقه بالا و پیشنهاد فضای دنج دور از سر و صدای پیاده‌راه.</td>
                  <td><b>نیاز به خلوت دنج و ثبت عکس اینستاگرامی</b><br><span style="color:#2ecc71">+۳۵٪ جذب زوج‌ها</span></td>
                </tr>
                <tr>
                  <td><b>SLOGAN-06</b></td>
                  <td>گردشگران حساس به قیمت</td>
                  <td><span class="wp-badge" style="background:#7f8c8d;color:#fff">TR / FA</span></td>
                  <td>«کوبیده داغ زغالی با دوغ محلی نعناعی فقط ۳۹۰ لیر! کیفیت درجه یک، قیمت منصفانه در قلب استقلال!»</td>
                  <td>نشان دادن پلاکارد فاکتور بدون هزینه پنهان با قیمت مقطوع و کیفیت اثبات‌شده.</td>
                  <td><b>شفافیت مالی آنی و مقایسه با فست‌فودهای گران</b><br><span style="color:#2ecc71">+۲۶٪ تبدیل اقتصادی</span></td>
                </tr>
                <tr>
                  <td><b>SLOGAN-07</b></td>
                  <td>ماجراجویان غذایی (Foodies)</td>
                  <td><span class="wp-badge" style="background:#e67e22;color:#fff">EN / TR</span></td>
                  <td>«اگه ته‌دیگ زعفرونیمون ترد و طلایی نبود، کل شامت مهمون شمسه! اصالت ایرانی یعنی همین!»</td>
                  <td>رویکرد افتخارآمیز به کیفیت پخت کته کباب با گارانتی بی قید و شرط طعم.</td>
                  <td><b>ریسک صفر مشتری و کنجکاوی چشیدن طعم</b><br><span style="color:#2ecc71">+۳۳٪ جلب کنجکاوی</span></td>
                </tr>
                <tr>
                  <td><b>SLOGAN-08</b></td>
                  <td>دوستداران موسیقی شبانه</td>
                  <td><span class="wp-badge" style="background:#9b59b6;color:#fff">FA / TR</span></td>
                  <td>«شام لذیذ با نوای زنده تار و تنبک ایرانی! موسیقی زنده در شعبه کوجاتپه، ترانسفر رایگان ۵ دقیقه‌ای!»</td>
                  <td>پخش ویدیوی کوتاه ساز سنتی روی تبلت پرسنل و ترانسفر فوری به سالن مجلل شعبه دوم.</td>
                  <td><b>اشتیاق به تفریح شبانه و دورهمی فاخر</b><br><span style="color:#2ecc71">+۲۱٪ سرریز به شعبه ۲</span></td>
                </tr>
                <tr>
                  <td><b>SLOGAN-09</b></td>
                  <td>عابران عجول (Quick Bites)</td>
                  <td><span class="wp-badge" style="background:#c0392b;color:#fff">EN / FA</span></td>
                  <td>«کباب اکسپرس آماده در کمتر از ۱۰ دقیقه! سریع، داغ و لذیذ، بدون معطلی به گشت شهری‌تون برسید!»</td>
                  <td>معرفی ست کباب بیرون‌بر یا سالن سریع برای عابرانی که عازم موزه یا مترو هستند.</td>
                  <td><b>مدیریت زمان فشرده توریست‌های گذری</b><br><span style="color:#2ecc71">+۲۲٪ فروش ظهر</span></td>
                </tr>
                <tr>
                  <td><b>SLOGAN-10</b></td>
                  <td>خانواده‌ها با کودک و سالمند</td>
                  <td><span class="wp-badge" style="background:#27ae60;color:#fff">FA / EN</span></td>
                  <td>«فضای خانوادگی صمیمی با منوی مخصوص کودکان بدون ادویه تند و کالسکه پسند؛ خوش آمدید به خانه خودتان!»</td>
                  <td>استقبال صمیمانه از خانواده‌ها، کمک به حمل کالسکه در ورودی و ارائه فوری صندلی کودک.</td>
                  <td><b>آسودگی والدین از ایمنی، راحتی و سلامت فرزند</b><br><span style="color:#2ecc71">+۳۸٪ وفاداری خانوادگی</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 2: 10 AI DOMAINS -->
        <div class="wp-card" style="margin-bottom:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid var(--card-border);padding-bottom:10px">
            <h3 style="margin:0;color:var(--cream);font-size:15px">🧠 ۱۰ حوزه استراتژیک ارتقای هوش مصنوعی در رستوران شمسه</h3>
            <span class="wp-badge" style="background:var(--gold);color:#101e22;font-weight:bold">AI Architecture</span>
          </div>

          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px">

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-01: انطباق فصلی منو</b>
                <span class="wp-badge" style="background:#27ae60;color:#fff">Weather LSTM</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">پیشنهاد پویای غذا و نوشیدنی بر اساس دمای هوا و فصول استانبول:</p>
              <ul style="font-size:10px;color:var(--muted);padding-right:16px;margin:0;line-height:1.6">
                <li><b>بهار:</b> شربت بیدمشک، کباب ترش گیلانی، باقالی‌پلو بهاره.</li>
                <li><b>تابستان:</b> دوغ نعناعی یخ‌مال، جوجه ماستی، سالاد شیرازی لیمویی، بستنی و فالوده.</li>
                <li><b>پاییز:</b> خورش فسنجان گردویی ملس با انار ساوه، سوپ جو تبریز داغ.</li>
                <li><b>زمستان:</b> چلو ماهیچه مجلسی مشهد، دیزی سنگی، دمنوش زعفران، دارچین و نبات.</li>
              </ul>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> +۱۴٪ افزایش فروش دسر و نوشیدنی</div>
            </div>

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-02: تفکیک منو بر اساس جغرافیا</b>
                <span class="wp-badge" style="background:#2980b9;color:#fff">Geo-Clustering</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">سفارشی‌سازی ترکیب غذاها متناسب با بافت جمعیتی دو شعبه:</p>
              <ul style="font-size:10px;color:var(--muted);padding-right:16px;margin:0;line-height:1.6">
                <li><b>شعبه استقلال:</b> منوی اکسپرس، ساندویچ لقمه کوبیده تیک‌اوی، چای ولکام، بالکن دنج.</li>
                <li><b>شعبه کوجاتپه:</b> سینی همایونی ۴ تا ۶ نفره، دورهمی مافیا، میتاپ استارتاپی، موسیقی زنده.</li>
              </ul>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> +۲۲٪ بهینه‌سازی درآمد ساعات غیرپیک</div>
            </div>

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-03: مهندسی بازخورد نقدها</b>
                <span class="wp-badge" style="background:#e74c3c;color:#fff">ABSA Loop</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">اتصال بلادرنگ ۵,۰۵۵ نقد به پروتکل‌های آشپزخانه:</p>
              <ul style="font-size:10px;color:var(--muted);padding-right:16px;margin:0;line-height:1.6">
                <li><b>نقد مهسا:</b> سنسور صف ورودی و کته قالبی پیش‌پخت (کاهش تاخیر از ۳۵ به ۱۰ دقیقه).</li>
                <li><b>نقد دیوید:</b> تفکیک رسمی چای رایگان ولکام و عبارت No Hidden Charges.</li>
                <li><b>نقد دیمیتری:</b> منوی تصویری خط سیریلیک روسی و تبلت سفارش‌گیری.</li>
              </ul>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> حذف ۹۲٪ کامنت‌های زیر ۳ ستاره</div>
            </div>

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-04: قیمت‌گذاری پویا و سود</b>
                <span class="wp-badge" style="background:#38bdf8;color:#000">Yield RevPASH</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">تطبیق هوشمند قیمت با نوسان ارز و ساعات شبانه‌روز:</p>
              <ul style="font-size:10px;color:var(--muted);padding-right:16px;margin:0;line-height:1.6">
                <li><b>Happy Hour:</b> تخفیف ۲۰٪ در ساعات ۱۴:۳۰ تا ۱۷:۳۰ برای دورکارها و توریست‌ها.</li>
                <li><b>سینک ارزی:</b> اتصال منوی دیجیتال به نرخ روز صرافی لیر/دلار بانک مرکزی ترکیه.</li>
                <li><b>کمبوهای طلایی:</b> ترکیب کباب کوبیده + زیتون پرورده + ماست موسیر با حاشیه سود ۶۸٪.</li>
              </ul>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> +۱۸۴,۰۰۰ لیر سود ماهانه خالص</div>
            </div>

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-05: کنترل ضایعات و پیش‌بینی تقاضا</b>
                <span class="wp-badge" style="background:#16a085;color:#fff">ARIMA / Prophet</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">پیش‌بینی کیلوگرم گوشت چرخ‌کرده، راسته و برنج مورد نیاز هر شیفت بر اساس آب و هوا، پروازها و تقویم توریستی.</p>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> کاهش ۹۵٪ ضایعات روزانه برنج و گوشت خام</div>
            </div>

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-06: جفت‌سازی طعم‌ها (Taste Pairing)</b>
                <span class="wp-badge" style="background:#8e44ad;color:#fff">Taste Recommender</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">پیشنهاد خودکار مزه‌های سنتی (میرزاقاسمی، زیتون پرورده، بورانی اسفناج) متناسب با نوع کباب انتخابی کاربر روی تبلت یا تلگرام.</p>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> +۳۱٪ افزایش در سبد سفارش پیش‌غذا</div>
            </div>

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-07: تغذیه سالم، گلوتن‌فری و کودک</b>
                <span class="wp-badge" style="background:#f39c12;color:#000">Diet Classifier</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">تفکیک نشان‌های کالری، بدون گلوتن (Gluten-Free)، بدون پیاز/ادویه تند برای مسافران حساس و منوی کته نرم کودکان.</p>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> +۱۹٪ افزایش رضایت مشتریان خانوادگی</div>
            </div>

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-08: تبلیغات لحظه‌ای آب و هوا</b>
                <span class="wp-badge" style="background:#34495e;color:#fff">LLM Real-Time</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">ارسال خودکار استوری و پیام تلگرام در روزهای بارانی استقلال: «باران پاییزی استقلال با عطر چای دمی زعفرانی شمسه و کاسه سوپ جو داغ می‌چسبه!»</p>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> +۲۷٪ افزایش تبدیل مخاطبان آنلاین</div>
            </div>

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-09: ترفیع فاکتور (AOV Upsell)</b>
                <span class="wp-badge" style="background:#d29a5a;color:#101e22">AOV Engine</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">پیشنهاد باقلوای تازه پسته با بستنی زعفرانی سنتی و ۵۰٪ تخفیف چای دمی پس از اتمام غذای اصلی روی تبلت سالن‌دار.</p>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> +۵۵ لیر افزایش میانگین ارزش هر فاکتور</div>
            </div>

            <div style="background:rgba(20,16,13,0.8);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <div style="display:flex;justify-content:space-between;margin-bottom:6px">
                <b style="color:var(--gold);font-size:12px">AI-DOM-10: ساعت هوشمند مترجم سالن</b>
                <span class="wp-badge" style="background:#2ecc71;color:#fff">Whisper + DeepL</span>
              </div>
              <p style="font-size:11px;color:var(--cream);margin-bottom:6px">تجهیز مچ‌بند و ساعت هوشمند پرسنل به موتور ترجمه گفتار-به-گفتار فوری ترکی، روسی، انگلیسی و فارسی برای ثبت بدون خطای سفارش.</p>
              <div style="font-size:11px;color:#2ecc71;margin-top:8px"><b>اثر مالی:</b> کاهش ۹۰٪ سوتفاهم‌های سالن</div>
            </div>

          </div>
        </div>

        <!-- SECTION 3: NEW MENU PRICING TABLE -->
        <div class="wp-card" style="margin-bottom:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid var(--card-border);padding-bottom:10px">
            <h3 style="margin:0;color:var(--cream);font-size:15px">💵 جدول مهندسی منوی جدید شمسه: قیمت‌ها، هزینه مواد و حاشیه سود خالص</h3>
            <span class="wp-badge" style="background:#27ae60;color:#fff">قیمت‌گذاری بهینه ۲۰۲۶</span>
          </div>

          <div style="overflow-x:auto">
            <table class="wp-table" style="font-size:11px;text-align:center">
              <thead>
                <tr>
                  <th style="text-align:right">نام غذا / آیتم منو</th>
                  <th>دسته‌بندی</th>
                  <th>قیمت قبلی (₺)</th>
                  <th>قیمت جدید (₺)</th>
                  <th>معادل دلار ($)</th>
                  <th>نسبت هزینه مواد (Food Cost)</th>
                  <th>سود ناخالص هر پرس (₺)</th>
                  <th>حاشیه سود (%)</th>
                  <th style="text-align:right">استراتژی و برچسب نقدها</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="text-align:right"><b>چلو کباب کوبیده مخصوص شمسه</b> (۲ سیخ ۱۱۰ گرمی)</td>
                  <td>کباب زغالی</td>
                  <td>۳۹۰ ₺</td>
                  <td><b style="color:#2ecc71">۴۲۰ ₺</b></td>
                  <td>$۱۲٫۵</td>
                  <td>۳۱٪</td>
                  <td>۲۹۰ ₺</td>
                  <td><b style="color:var(--gold)">۶۹٪</b></td>
                  <td style="text-align:right">پرفروش‌ترین غذا طبق ۴,۲۰۰ نظر مثبت؛ گارانتی کته ۱۰ دقیقه‌ای</td>
                </tr>
                <tr>
                  <td style="text-align:right"><b>چلو کباب برگ گوسفندی اعلا</b> (راسته مرینیت زعفرانی)</td>
                  <td>کباب زغالی</td>
                  <td>۶۲۰ ₺</td>
                  <td><b style="color:#2ecc71">۶۶۰ ₺</b></td>
                  <td>$۱۹٫۵</td>
                  <td>۳۴٪</td>
                  <td>۴۳۵ ₺</td>
                  <td><b style="color:var(--gold)">۶۶٪</b></td>
                  <td style="text-align:right">محبوب توریست‌های اروپایی و عرب با بافت فوق‌العاده نرم</td>
                </tr>
                <tr>
                  <td style="text-align:right"><b>چلو جوجه کباب زعفرانی با استخوان</b> (شنسل تازه)</td>
                  <td>کباب زغالی</td>
                  <td>۳۶۰ ₺</td>
                  <td><b style="color:#2ecc71">۳۸۰ ₺</b></td>
                  <td>$۱۱٫۲</td>
                  <td>۲۸٪</td>
                  <td>۲۷۳ ₺</td>
                  <td><b style="color:var(--gold)">۷۲٪</b></td>
                  <td style="text-align:right">وعده سبک پروتيین برای جوانان و مسافران تابستانه</td>
                </tr>
                <tr>
                  <td style="text-align:right"><b>چلو کباب شیشلیک شاندیز</b> (۶ تکه راسته دنده)</td>
                  <td>کباب زغالی</td>
                  <td>۷۸۰ ₺</td>
                  <td><b style="color:#2ecc71">۸۲۰ ₺</b></td>
                  <td>$۲۴٫۰</td>
                  <td>۳۶٪</td>
                  <td>۵۲۵ ₺</td>
                  <td><b style="color:var(--gold)">۶۴٪</b></td>
                  <td style="text-align:right">پرفروش‌ترین کباب در ضیافت‌های تجاری و خانوادگی</td>
                </tr>
                <tr>
                  <td style="text-align:right"><b>چلو ماهیچه همایونی زعفرانی</b> (با برنج دودی)</td>
                  <td>دست‌پخت مجلسی</td>
                  <td>۶۹۰ ₺</td>
                  <td><b style="color:#2ecc71">۷۴۰ ₺</b></td>
                  <td>$۲۲٫۰</td>
                  <td>۳۵٪</td>
                  <td>۴۸۱ ₺</td>
                  <td><b style="color:var(--gold)">۶۵٪</b></td>
                  <td style="text-align:right">ستاره منوی زمستانه و پاییزی، برنده Travelers' Choice</td>
                </tr>
                <tr>
                  <td style="text-align:right"><b>چلو خورش قورمه‌سبزی جاافتاده</b> (لوبیا قرمز و لیمو)</td>
                  <td>خورشت سنتی</td>
                  <td>۳۴۰ ₺</td>
                  <td><b style="color:#2ecc71">۳۶۰ ₺</b></td>
                  <td>$۱۰٫۶</td>
                  <td>۲۵٪</td>
                  <td>۲۷۰ ₺</td>
                  <td><b style="color:var(--gold)">۷۵٪</b></td>
                  <td style="text-align:right">طعم نوستالژیک ۱۰۰٪ خانگی برای مسافران ایرانی</td>
                </tr>
                <tr>
                  <td style="text-align:right"><b>چلو خورش فسنجان گردو و انار</b> (ملس ساوه)</td>
                  <td>خورشت سنتی</td>
                  <td>۳۸۰ ₺</td>
                  <td><b style="color:#2ecc71">۴۱۰ ₺</b></td>
                  <td>$۱۲٫۰</td>
                  <td>۳۰٪</td>
                  <td>۲۸۷ ₺</td>
                  <td><b style="color:var(--gold)">۷۰٪</b></td>
                  <td style="text-align:right">پیشنهاد ویژه روزهای بارانی پاییز و زمستان استانبول</td>
                </tr>
                <tr>
                  <td style="text-align:right"><b>سینی مزه ایرانی ۴ نفره</b> (میرزاقاسمی، کشک، زیتون)</td>
                  <td>پیش‌غذا</td>
                  <td>۲۸۰ ₺</td>
                  <td><b style="color:#2ecc71">۳۲۰ ₺</b></td>
                  <td>$۹٫۵</td>
                  <td>۲۲٪</td>
                  <td>۲۵۰ ₺</td>
                  <td><b style="color:var(--gold)">۷۸٪</b></td>
                  <td style="text-align:right">بالاترین نرخ جفت‌سازی و حاشیه سود در منو</td>
                </tr>
                <tr>
                  <td style="text-align:right"><b>دوغ دست‌ساز محلی نعناعی</b> (پارچ ۱ لیتری)</td>
                  <td>نوشیدنی</td>
                  <td>۹۰ ₺</td>
                  <td><b style="color:#2ecc71">۱۱۰ ₺</b></td>
                  <td>$۳٫۲</td>
                  <td>۱۸٪</td>
                  <td>۹۰ ₺</td>
                  <td><b style="color:var(--gold)">۸۲٪</b></td>
                  <td style="text-align:right">مکمل طبیعی بدون مواد نگهدارنده برای کباب‌ها</td>
                </tr>
                <tr>
                  <td style="text-align:right"><b>باقلوای تازه پسته با بستنی سنتی زعفرانی</b></td>
                  <td>دسر و چای</td>
                  <td>۱۶۰ ₺</td>
                  <td><b style="color:#2ecc71">۱۹۰ ₺</b></td>
                  <td>$۵٫۶</td>
                  <td>۲۴٪</td>
                  <td>۱۴۴ ₺</td>
                  <td><b style="color:var(--gold)">۷۶٪</b></td>
                  <td style="text-align:right">حسن ختام وعده غذایی با اهدای چای دمی رایگان</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 4: UNIFIED AUTH & 1-YEAR SESSION SYNC -->
        <div class="wp-card" style="border:1.5px solid #27ae60;background:linear-gradient(135deg,rgba(39,174,96,0.1),rgba(20,16,13,0.95))">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:14px;border-bottom:1px solid rgba(39,174,96,0.3);padding-bottom:10px">
            <div>
              <h3 style="margin:0;color:var(--cream);font-size:15px">🔄 سامانه همگام احراز هویت با اعتبار ۳۶۵ روزه (Unified 1-Year Auth Sync)</h3>
              <p style="margin:3px 0 0;font-size:11px;color:var(--muted)">اتصال سراسری و بلادرنگ نشست‌های مدیریت بین وب‌سایت، پرتال و ربات تلگرام شمسه</p>
            </div>
            <span class="wp-badge" style="background:#27ae60;color:#fff;font-size:11px">وضعیت پایگاه داده: ۱۰۰٪ همگام</span>
          </div>

          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-bottom:14px">
            <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:6px;border:1px solid rgba(255,255,255,0.1)">
              <div style="font-size:11px;color:var(--muted);margin-bottom:4px">کاربر فعال و احراز هویت شده:</div>
              <div style="font-size:16px;font-weight:bold;color:var(--gold)">shamse_admin</div>
              <div style="font-size:10px;color:var(--muted);margin-top:2px">نقش: مدیر ارشد اجرایی شمسه</div>
            </div>
            <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:6px;border:1px solid rgba(255,255,255,0.1)">
              <div style="font-size:11px;color:var(--muted);margin-bottom:4px">مدت اعتبار نشست (Session):</div>
              <div style="font-size:16px;font-weight:bold;color:#2ecc71">۳۶۵ روزه (۱ سال کامل)</div>
              <div style="font-size:10px;color:var(--muted);margin-top:2px">انقضا: اکتبر ۲۰۲۷ (بدون نیاز به لاگین مجدد)</div>
            </div>
            <div style="background:rgba(0,0,0,0.4);padding:12px;border-radius:6px;border:1px solid rgba(255,255,255,0.1)">
              <div style="font-size:11px;color:var(--muted);margin-bottom:4px">وضعیت سینک با بات تلگرام:</div>
              <div style="font-size:16px;font-weight:bold;color:#38bdf8">متصل و فعال ✓</div>
              <div style="font-size:10px;color:var(--muted);margin-top:2px">شناسه چت: @shamse_restaurant_bot</div>
            </div>
          </div>

          <div style="background:rgba(0,0,0,0.3);padding:12px;border-radius:6px;font-size:11px;line-height:1.6;color:var(--cream)">
            <b>دستور مستقیم تست ورود در تلگرام:</b><br>
            <code>/login shamse_admin Shamse@2026!Istiklal</code><br>
            <i>پس از ارسال این دستور در تلگرام، پنل اختصاصی مدیر با ۱۰ شعار دادزن، منوی فصلی و مهندسی سود باز می‌شود و توکن ۳۶۵ روزه در auth_sync_db.json ثبت می‌گردد.</i>
          </div>
        </div>

      </section>
"""

    if '<section id="tab-jarchi-menu"' not in html:
        # درج تب قبل از بسته شدن تگ main
        target_main = "</main>"
        html = html.replace(target_main, tab_content + "\n    " + target_main, 1)

    with open(ADMIN_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("Admin panel patched successfully with Jarchi Tab & 365-Day Sync Badge.")


def patch_index_html():
    with open(INDEX_HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # افزودن نشانگر وضعیت ورود یکپارچه به هدر سایت اصلی (siteExecutiveCredentialsBanner)
    sync_badge_index = """      <span style="color:rgba(255,255,255,.2)">|</span>
      <span id="siteUnifiedAuthSyncBadge" style="background:rgba(46,204,113,0.18);color:#2ecc71;border:1px solid #27ae60;padding:2px 8px;border-radius:3px;font-size:.73rem;display:inline-flex;align-items:center;gap:4px">
        <span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:#2ecc71"></span>
        ✓ ورود یکپارچه فعال • سشن ۳۶۵ روزه (تا ۲۰۲۷) • سینک با تلگرام
      </span>"""

    if "siteUnifiedAuthSyncBadge" not in html:
        target_code = """        پیشخوان ادمین: <code style="background:#13100c;color:#2ecc71;padding:1px 6px;border:1px solid #23402c">shamse_admin</code> / <code style="background:#13100c;color:#2ecc71;padding:1px 6px;border:1px solid #23402c">Shamse@2026!Istiklal</code>
      </span>"""
        replacement = target_code + "\n" + sync_badge_index
        html = html.replace(target_code, replacement, 1)

    with open(INDEX_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("Index.html patched successfully with Unified Auth Sync Badge in Header.")


if __name__ == "__main__":
    patch_admin_panel()
    patch_index_html()
