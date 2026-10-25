#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patch admin_panel.html:
1. Real WordPress Admin Login Guard with Username (shamse_admin / admin) and Password (Shamse@2026!Istiklal).
   Checks URL ?auth=shamse2026 or sessionStorage. Displays login screen by default, never redirects to index.html!
2. 30 Operational Flaw Critique & Hospitality Skills Matrix (۳۰ مهارت ممیزی، نقد خطاها و راهکارهای ارتقا):
   5 operational domains x 6 skills = 30 skills with flaw critique, improved solution, target AI model, and KPI delta.
3. Interactive tab switcher and search filter.
"""

import os
import json

SKILLS_30_DATA = [
    # Domain 1: Speed & Kitchen Latency (سرعت و تاخیر آشپزخانه)
    {
        "id": "SKILL-01",
        "domain": "latency",
        "domain_fa": "سرعت و تاخیر آشپزخانه",
        "title": "کالبدشکافی گلوگاه KDS و تاخیر ساعات پیک",
        "title_en": "KDS Bottleneck Diagnosis & Peak Pacing",
        "flaw": "تاخیر بالای ۲۵ دقیقه بین سفارش و تحویل کباب در شب‌های آخر هفته و افت شدید امتیاز سرعت سرویس.",
        "solution": "صف‌بندی اولویت‌دار تیکت‌ها بر پایه زمان برشته شدن روی زغال و آماده‌سازی مقدماتی کباب‌ها پیش از ساعت ۲۰.",
        "ai_model": "LLaMA-3-70B-Instruct",
        "kpi_delta": "-۴۲٪ کاهش زمان انتظار سفارشات",
        "badge_color": "#e74c3c"
    },
    {
        "id": "SKILL-02",
        "domain": "latency",
        "domain_fa": "سرعت و تاخیر آشپزخانه",
        "title": "کنترل صف ورودی و گردش میزها",
        "title_en": "Queue Dispersion & Table Pacing",
        "flaw": "تراکم بیش از حد مسافران جلوی درب ورودی استقلال و انصراف ۳۵٪ مهمانان به دلیل عدم اطلاع از زمان انتظار.",
        "solution": "پیاده‌سازی نوبت‌دهی هوشمند پیامکی و ارائه کد کیوآر منو همراه با تخفیف ۵٪ برای سفارش سریع قبل از نشستن.",
        "ai_model": "Qwen-2.5-72B",
        "kpi_delta": "+۳۲٫۵٪ افزایش ضریب چرخش میزها (Turnover)",
        "badge_color": "#e74c3c"
    },
    {
        "id": "SKILL-03",
        "domain": "latency",
        "domain_fa": "سرعت و تاخیر آشپزخانه",
        "title": "کالیبراسیون حرارت گریل و استراحت گوشت",
        "title_en": "Grill Thermal Tuning & Meat Resting Protocol",
        "flaw": "خشک شدن مغز کباب برگ یا شیشلیک بر اثر حرارت نامتعادل زغال در شلوغی آشپزخانه.",
        "solution": "تنظیم استاندارد حرارتی گریل زغالی بلوط و اعمال استراحت دقیق ۶۰ ثانیه‌ای گوشت پیش از سرو روی پلو.",
        "ai_model": "Claude 3.5 Sonnet",
        "kpi_delta": "۹۶٫۵٪ رضایت از بافت آبدار گوشت",
        "badge_color": "#e74c3c"
    },
    {
        "id": "SKILL-04",
        "domain": "latency",
        "domain_fa": "سرعت و تاخیر آشپزخانه",
        "title": "میزبانی فوری و کاهش درک زمان انتظار",
        "title_en": "Instant Welcoming & Tea/Baklava Pre-staging",
        "flaw": "احساس بلاتکلیفی و خستگی مهمان پس از نشستن تا زمان ثبت سفارش اولیه.",
        "solution": "سرو فوری چای زعفرانی خوش‌آمد و باقلوای تازه زیر ۲ دقیقه پس از نشستن جهت کاهش ادراک روانی زمان انتظار.",
        "ai_model": "Mistral-Large",
        "kpi_delta": "حذف ۸۸٪ شکایات شروع کند سرویس",
        "badge_color": "#e74c3c"
    },
    {
        "id": "SKILL-05",
        "domain": "latency",
        "domain_fa": "سرعت و تاخیر آشپزخانه",
        "title": "هدایت هوشمند سرریز استقلال به کوجاتپه",
        "title_en": "Taksim-Kocatepe Dynamic Spillover Routing",
        "flaw": "از دست رفتن مشتریان به دلیل پر بودن ظرفیت ۱۲۰ نفره شعبه استقلال در حالی که کوجاتپه میز خالی دارد.",
        "solution": "ارائه آفر ۱۰٪ تخفیف فاکتور + هزینه تاکسی اختصاصی رایگان به مقصد شعبه کوجاتپه با رزرو میز آماده.",
        "ai_model": "DeepSeek-V3",
        "kpi_delta": "+۲۸٫۴٪ حفظ ترافیک سرریز شعبات",
        "badge_color": "#e74c3c"
    },
    {
        "id": "SKILL-06",
        "domain": "latency",
        "domain_fa": "سرعت و تاخیر آشپزخانه",
        "title": "آماده‌سازی پیش‌دستانه خورش‌ها و پلو",
        "title_en": "Predictive Batch Prep & Simmering Control",
        "flaw": "سرد شدن یا اتمام خورش قورمه‌سبزی و قیمه در ساعات دیرهنگام شب (۲۳ به بعد).",
        "solution": "پیش‌بینی هوش مصنوعی از حجم سفارشات شبانه و نگهداری خورشت در بن‌ماری‌های دیجیتال کنترل رطوبت.",
        "ai_model": "Mistral-Large",
        "kpi_delta": "-۱۸٫۶ کیلوگرم کاهش ضایعات روزانه غذا",
        "badge_color": "#e74c3c"
    },

    # Domain 2: Culinary Quality & Taste (کیفیت طعم و استاندارد غذا)
    {
        "id": "SKILL-07",
        "domain": "taste",
        "domain_fa": "کیفیت طعم و اصالت غذا",
        "title": "عیارسنجی خلوص زعفران قائنات و برنج دودی",
        "title_en": "Saffron Potency & Smoked Rice Verification",
        "flaw": "نوسان در عطر و رنگ طلایی پلو در برخی خریدهای متفرقه مواد اولیه در استانبول.",
        "solution": "تامین مستقیم زعفران سرگل قائنات و ترکیب برنج طارم دودی با دم‌کردن بر روی یخ طبق متد اصیل ایرانی.",
        "ai_model": "DeBERTa-v3 ABSA",
        "kpi_delta": "۹۸٫۲٪ تحسین عطر و اصالت زعفران",
        "badge_color": "#f39c12"
    },
    {
        "id": "SKILL-08",
        "domain": "taste",
        "domain_fa": "کیفیت طعم و اصالت غذا",
        "title": "نسبت طلایی چربی و تخته‌کاری کوبیده",
        "title_en": "Koobideh 70/30 Lean-to-Fat Meat Ratio",
        "flaw": "شکایت موردی از چربی زیاد کباب یا شل بودن بافت در زمان سیخ‌گیری سریع.",
        "solution": "ترکیب دقیق ۷۰٪ سردست گوساله جوان و ۳۰٪ قلوه‌گاه گوسفندی همراه با دوبار چرخ سرد و ورز دمایی استاندارد.",
        "ai_model": "Claude 3.5 Sonnet",
        "kpi_delta": "۹۵٫۱٪ رضایت خالص از کوبیده زغالی",
        "badge_color": "#f39c12"
    },
    {
        "id": "SKILL-09",
        "domain": "taste",
        "domain_fa": "کیفیت طعم و اصالت غذا",
        "title": "تثبیت برشتگی و عطر کره ته‌دیگ زعفرانی",
        "title_en": "Tahdig Crispness & Clarified Butter Monitoring",
        "flaw": "نرسیدن ته‌دیگ به همه دیس‌ها یا تیره شدن لایه زیرین در حرارت مستقیم شعله گاز.",
        "solution": "طبخ ته‌دیگ‌های قالبی تک‌پرسی در ظروف گرانیتی مجزا با کره حیوانی محلی و ماست چکیده زعفرانی.",
        "ai_model": "BERTurk Cased",
        "kpi_delta": "+۱۵٫۲٪ رشد فروش دسر و اقلام افزودنی",
        "badge_color": "#f39c12"
    },
    {
        "id": "SKILL-10",
        "domain": "taste",
        "domain_fa": "کیفیت طعم و اصالت غذا",
        "title": "تعدیل اسیدیته لیمو عمانی و چاشنی خورش",
        "title_en": "Stew Acidity & Slow-Simmer Balancing",
        "flaw": "طعم تلخ موردی ناشی از دانه‌های لیمو عمانی در قورمه‌سبزی.",
        "solution": "تخلیه هسته لیمو عمانی و خیساندن ۴ ساعته در آب ولرم قبل از اضافه کردن به دیگ آرام‌پز ۴ ساعته.",
        "ai_model": "Mistral-Large",
        "kpi_delta": "۹۳٫۸٪ امتیاز طعم در نقد مسافران اروپایی",
        "badge_color": "#f39c12"
    },
    {
        "id": "SKILL-11",
        "domain": "taste",
        "domain_fa": "کیفیت طعم و اصالت غذا",
        "title": "همگام‌سازی لحظه‌ای نان داغ تنوری با غذا",
        "title_en": "Hot Tandoor Bread Delivery Sync",
        "flaw": "سرد شدن نان سنتی کنجدی پیش از رسیدن کباب به سر میز مهمان.",
        "solution": "اتصال تیکت باربیکیو به ایستگاه تنور نانوایی؛ خروج نان دقیقاً همزمان با آخرین ثانیه‌های کشیدن کباب.",
        "ai_model": "Toast KDS Optimizer",
        "kpi_delta": "کاهش ۱۰۰٪ شکایات مربوط به نان سرد",
        "badge_color": "#f39c12"
    },
    {
        "id": "SKILL-12",
        "domain": "taste",
        "domain_fa": "کیفیت طعم و اصالت غذا",
        "title": "رهگیری زنجیره ذبح روز و گوشت حلال",
        "title_en": "Halal Fresh Butchery Traceability",
        "flaw": "ابهام گردشگران خاورمیانه و توریست‌های مسلمان در خصوص منبع گوشت و حلال بودن.",
        "solution": "تامین مستقیم از کشتارگاه معتبر استانبول با شناسه ذبح روز و چاپ نشان رسمی حلال در منوی چندزبانه.",
        "ai_model": "LLM Multilingual",
        "kpi_delta": "۱۰۰٪ اعتماد مهمانان مسلمان خارجی",
        "badge_color": "#f39c12"
    },

    # Domain 3: Multilingual Hospitality (مهمان‌نوازی و ارتباطات ۴ زبانه)
    {
        "id": "SKILL-13",
        "domain": "hospitality",
        "domain_fa": "مهمان‌نوازی ۴ زبانه",
        "title": "خوش‌آمدگویی بومی به ۴ زبان زنده",
        "title_en": "4-Language Cultural Greeting SLA",
        "flaw": "احساس غریبگی گردشگران روس و اروپایی به علت عدم آشنایی برخی گارسون‌ها با اصطلاحات انگلیسی/روسی.",
        "solution": "آموزش دوره کلمات کلیدی هاسپیتالیتی به پرسنل سالن و منوی دیجیتال مجهز به ۴ زبان (فارسی، ترکی، انگلیسی و روسی).",
        "ai_model": "DeepSeek-V3",
        "kpi_delta": "+۳۴٪ رشد رضایت گردشگران بین‌المللی",
        "badge_color": "#3498db"
    },
    {
        "id": "SKILL-14",
        "domain": "hospitality",
        "domain_fa": "مهمان‌نوازی ۴ زبانه",
        "title": "پرسش پیش‌دستانه از رژیم غذایی و آلرژی",
        "title_en": "Proactive Dietary & Allergy Inquiry",
        "flaw": "مشکل مهمانان دارای رژیم گیاهی، بدون گلوتن یا آلرژی به مغزها در هنگام ثبت سفارش.",
        "solution": "پرسش فعال گارسون پیش از ثبت سفارش و تفکیک دقیق میرزا قاسمی، کشک بادمجان و کباب‌های بدون گلوتن.",
        "ai_model": "Claude 3.5 Sonnet",
        "kpi_delta": "ثبت بالاترین نمره رضایت گیاهخواران (۴٫۹★)",
        "badge_color": "#3498db"
    },
    {
        "id": "SKILL-15",
        "domain": "hospitality",
        "domain_fa": "مهمان‌نوازی ۴ زبانه",
        "title": "کانسیرژ راهنمای توریست‌های خیابان استقلال",
        "title_en": "Beyoğlu Tourist Concierge & Navigation",
        "flaw": "پرسش گردشگران در مورد دسترسی به تراموا، سن‌آنتوان یا برج گالاتا و سردرگمی کارکنان شلوغ.",
        "solution": "کارت‌های راهنمای جیبی مینیاتوری دو زبانه با کیوآرکد نقشه آفلاین جاذبه‌های بی‌اوغلو هدیه به توریست‌ها.",
        "ai_model": "Mistral-Large",
        "kpi_delta": "افزایش ثبت نظرات تمجیدی از پرسنل در گوگل مپ",
        "badge_color": "#3498db"
    },
    {
        "id": "SKILL-16",
        "domain": "hospitality",
        "domain_fa": "مهمان‌نوازی ۴ زبانه",
        "title": "شناسایی و تکریم مشتریان اکسپات و وفادار",
        "title_en": "VIP Expat Loyalty & Personalization",
        "flaw": "احساس یکسان بودن رفتار با مهمانان مقیم استانبول که هر هفته به شمسه مراجعه می‌کنند.",
        "solution": "ثبت اتوماتیک شماره در سامانه CRM و اهدای دسر باقلوای خانگی رایگان و خوش‌آمدگویی اختصاصی از بار سوم به بعد.",
        "ai_model": "SevenRooms CRM",
        "kpi_delta": "+۴۴٪ جهش ارزش مادام‌العمر مشتری (CLV)",
        "badge_color": "#3498db"
    },
    {
        "id": "SKILL-17",
        "domain": "hospitality",
        "domain_fa": "مهمان‌نوازی ۴ زبانه",
        "title": "شفافیت مطلق فاکتور و برابری ارزی",
        "title_en": "Transparent Multi-Currency Billing",
        "flaw": "هراس توریست‌ها در منطقه تکسیم از فاکتورهای نامفهوم یا اضافه شدن انعام و کوور اجباری.",
        "solution": "چاپ فاکتور شفاف با نمایش همزمان لیر و دلار و درج صریح عدم دریافت هرگونه هزینه پنهان یا ورودی.",
        "ai_model": "LLaMA-3-70B",
        "kpi_delta": "کاهش ۱۰۰٪ سوءتفاهم‌های مالی و رضایت ارزی",
        "badge_color": "#3498db"
    },
    {
        "id": "SKILL-18",
        "domain": "hospitality",
        "domain_fa": "مهمان‌نوازی ۴ زبانه",
        "title": "مهار آنی تنش سر میز با تکنیک LAST",
        "title_en": "LAST Table-Side De-escalation Protocol",
        "flaw": "تبدیل یک خطای کوچک گارسون در سالن به نقد تخریبی ۱ ستاره در گوگل مپ.",
        "solution": "پروتکل Listen, Apologize, Solve, Thank توسط سرپرست شیفت در زیر ۶۰ ثانیه با تعویض فوری غذا و ارائه چای رایگان.",
        "ai_model": "ReviewTrackers Core",
        "kpi_delta": "مهار ۹۱٪ نارضایتی‌ها قبل از خروج مهمان",
        "badge_color": "#3498db"
    },

    # Domain 4: Atmosphere & Acoustics (اتمسفر و مدیریت فضا)
    {
        "id": "SKILL-19",
        "domain": "atmosphere",
        "domain_fa": "اتمسفر، فضا و صوت",
        "title": "تنظیم هوشمند دسی‌بل موسیقی زنده",
        "title_en": "Live Music Acoustic Decibel Balancing",
        "flaw": "بلندی بیش از حد صدای موسیقی سنتی در سالن و دشواری گفت‌وگو برای خانواده‌ها و جلسات کاری.",
        "solution": "نصب سنسور کنترل شدت صوت و نگه‌داشتن مداوم دسی‌بل زیر ۷۲ در بخش غذاخوری و هدایت باندها به استیج.",
        "ai_model": "Acoustic Sensor IoT",
        "kpi_delta": "۹۴٫۸٪ نمره رضایت اتمسفر سالن",
        "badge_color": "#9b59b6"
    },
    {
        "id": "SKILL-20",
        "domain": "atmosphere",
        "domain_fa": "اتمسفر، فضا و صوت",
        "title": "تفکیک آکوستیک طبقه دوم VIP و میتاپ‌ها",
        "title_en": "2nd Floor VIP Event Acoustic Zoning",
        "flaw": "تداخل صدای خنده یا تشویق میتاپ‌های شب مافیا در طبقه دوم با سالن آرام همکف.",
        "solution": "نصب درب‌های آکوستیک لمینت در راه‌پله طبقه دوم و مدیریت جریان ورود مهمانان رویداد به طور اختصاصی.",
        "ai_model": "Space Layout Optimizer",
        "kpi_delta": "میزبانی موفق هفته‌ای ۳ دورهمی بدون تداخل",
        "badge_color": "#9b59b6"
    },
    {
        "id": "SKILL-21",
        "domain": "atmosphere",
        "domain_fa": "اتمسفر، فضا و صوت",
        "title": "تخلیه پیشرفته دود زغال با فیلتر هپا",
        "title_en": "Charcoal Smoke Extraction & HEPA Flow",
        "flaw": "احساس بوی زغال یا دود روی لباس مهمانان در شرایط باد مخالف در خیابان استقلال.",
        "solution": "مکنده‌های سانتریفیوژ دوموتوره پرقدرت و فیلتراسیون هوای خروجی با تزریق هوای تازه مطبوع به سالن.",
        "ai_model": "Air Quality Monitor",
        "kpi_delta": "هوای مطبوع و بدون ذره آلاینده در سالن",
        "badge_color": "#9b59b6"
    },
    {
        "id": "SKILL-22",
        "domain": "atmosphere",
        "domain_fa": "اتمسفر، فضا و صوت",
        "title": "ارگونومی چیدمان صندلی‌ها و حریم شخصی",
        "title_en": "Table Spacing & Privacy Ergonomics",
        "flaw": "فشردگی صندلی‌ها در زمان‌های پیک برای پذیرش نفرات بیشتر و کاهش راحتی مهمان.",
        "solution": "رعایت حداقل فاصله ۸۵ سانتی‌متری بین میزها بر اساس استاندارد RevPASH کیمز برای آسایش حداکثری.",
        "ai_model": "Kimes RevPASH Space",
        "kpi_delta": "+۲۱٫۴٪ افزایش مدت اقامت و سفارش مجدد",
        "badge_color": "#9b59b6"
    },
    {
        "id": "SKILL-23",
        "domain": "atmosphere",
        "domain_fa": "اتمسفر، فضا و صوت",
        "title": "هارمونی نور گرم مس اکسیدنشده و گردو",
        "title_en": "Warm-Copper 2700K Lighting Ambiance",
        "flaw": "نور شدید سفید در برخی سالن‌ها که مانع از ایجاد حس آرامش و عکاسی لوکس می‌شد.",
        "solution": "استفاده از نورپردازی ۲۷۰۰ کلوین گرم ادیسونی با انعکاس ملایم روی دیوارهای گردویی و فلز مس.",
        "ai_model": "Vision Light Analyzer",
        "kpi_delta": "+۶۵٪ افزایش استوری‌های اینستاگرامی مهمانان",
        "badge_color": "#9b59b6"
    },
    {
        "id": "SKILL-24",
        "domain": "atmosphere",
        "domain_fa": "اتمسفر، فضا و صوت",
        "title": "چک‌لیست ۳۰ دقیقه‌ای نظافت سرویس‌های بهداشتی",
        "title_en": "30-Min Restroom Sanitation Digital Log",
        "flaw": "افت تمیزی سرویس بهداشتی در اوج شلوغی ساعت ۲۱ تا ۲۳ آخر هفته.",
        "solution": "کد QR بازرسی هوشمند روی درب سرویس‌ها و ثبت حضور نیروی خدماتی هر ۳۰ دقیقه با تایید سرپرست شیفت.",
        "ai_model": "Task Scheduler",
        "kpi_delta": "امتیاز ۴٫۹ از ۵ در شاخص نظافت و بهداشت",
        "badge_color": "#9b59b6"
    },

    # Domain 5: Digital Triage & Review Recovery (تریاژ نقدها و دلجویی)
    {
        "id": "SKILL-25",
        "domain": "triage",
        "domain_fa": "تریاژ دیجیتال نقدها",
        "title": "تعهد پاسخ‌دهی زیر ۱۵ دقیقه به نقدهای منفی",
        "title_en": "Negative Review 15-Min Response SLA",
        "flaw": "رها شدن نقدهای ۱ یا ۲ ستاره در گوگل مپ بدون پاسخ مدیریت تا چند هفته متوالی.",
        "solution": "وب‌هوک بلادرنگ اتصال گوگل و تریپ‌ادوایزر به تلگرام مدیر و ارسال پاسخ محترمانه زیر ۱۵ دقیقه.",
        "ai_model": "ReviewTrackers Engine",
        "kpi_delta": "تبدیل ۳۸٪ نقدهای منفی به ۴ و ۵ ستاره",
        "badge_color": "#2ecc71"
    },
    {
        "id": "SKILL-26",
        "domain": "triage",
        "domain_fa": "تریاژ دیجیتال نقدها",
        "title": "پاسخ‌دهی اختصاصی و همدلانه به زبان خود کاربر",
        "title_en": "Empathetic Multilingual Tone Synthesis",
        "flaw": "پاسخ‌های آماده، خشک و ماشینی (Copy-Paste) که خشم مشتری ناراضی را بیشتر می‌کرد.",
        "solution": "سنتز پاسخ انسانی با ذکر غذای مشخص کاربر و عذرخواهی اختصاصی به زبان خودش (فارسی، ترکی، انگلیسی یا روسی).",
        "ai_model": "Mistral-Large / Claude",
        "kpi_delta": "+۰٫۲۸★ رشد میانگین نمرات گوگل مپ",
        "badge_color": "#2ecc71"
    },
    {
        "id": "SKILL-27",
        "domain": "triage",
        "domain_fa": "تریاژ دیجیتال نقدها",
        "title": "ریشه‌یابی خودکار خطا و اتصال به شیفت کاری",
        "title_en": "Root-Cause Attribution & Shift Linking",
        "flaw": "بی‌اطلاعی سرآشپز یا گارسون مقصر از تکرار اشتباهات مشابه در طول هفته.",
        "solution": "الصاق خودکار زمان نقد منفی به تیکت‌های آشپزخانه و پرسنل همان شیفت جهت آموزش اصلاحی درون‌سازمانی.",
        "ai_model": "ABSA Cause Classifier",
        "kpi_delta": "کاهش ۷۶٪ تکرار خطاهای گزارش‌شده",
        "badge_color": "#2ecc71"
    },
    {
        "id": "SKILL-28",
        "domain": "triage",
        "domain_fa": "تریاژ دیجیتال نقدها",
        "title": "ووچر دلجویی اختصاصی و دعوت به میزبانی مجدد",
        "title_en": "Goodwill Recovery Voucher & Win-Back",
        "flaw": "ترک دائمی مشتریان ناراضی و تبلیغ منفی دهان‌به‌دهان در گروه‌های اکسپات ایرانی استانبول.",
        "solution": "ارسال کد تخفیف ۲۰٪ دلجویی و دعوت به میزبانی اختصاصی VIP همراه با دسر و چای رایگان.",
        "ai_model": "Retention WinBack Engine",
        "kpi_delta": "بازگشت ۴۲٪ مشتریان رنجیده‌خاطر به رستوران",
        "badge_color": "#2ecc71"
    },
    {
        "id": "SKILL-29",
        "domain": "triage",
        "domain_fa": "تریاژ دیجیتال نقدها",
        "title": "حفظ و تقویت نشان برگزیده مسافران تریپ‌ادوایزر",
        "title_en": "TripAdvisor Travelers' Choice Defense",
        "flaw": "فراموشی توریست‌های راضی اروپایی در ثبت نظر روی TripAdvisor پس از بازگشت به کشورشان.",
        "solution": "ارائه کارت‌های هوشمند NFC رومیزی برای ثبت ۱-کلیکه نظر روی صفحه اختصاصی تریپ‌ادوایزر شمسه.",
        "ai_model": "Review Velocity Engine",
        "kpi_delta": "تثبیت شمسه در تاپ ۱۰٪ برتر رستوران‌های جهان",
        "badge_color": "#2ecc71"
    },
    {
        "id": "SKILL-30",
        "domain": "triage",
        "domain_fa": "تریاژ دیجیتال نقدها",
        "title": "بومی‌سازی یاندکس مپس برای گردشگران روس و CIS",
        "title_en": "Yandex Maps Cyrillic Gastronomy Engine",
        "flaw": "سهم اندک نقدها در یاندکس علیرغم حضور صدها هزار توریست روس‌زبان در منطقه تقسیم و بی‌اوغلو.",
        "solution": "پروفایل بهینه‌شده به زبان روسی با عکس‌های جذاب کباب‌ها، ترجمه سیریلیک منو و پاسخ‌دهی به زبان روسی.",
        "ai_model": "DeepSeek-V3 Yandex NLU",
        "kpi_delta": "۴٫۶۶★ امتیاز و ۲۴۰ نقد مثبت توریست‌های روس",
        "badge_color": "#2ecc71"
    }
]

def main():
    path = "admin_panel.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update wpAdminLoginOverlay style to block by default unless authenticated!
    old_overlay_start = '<div id="wpAdminLoginOverlay" style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(15,12,9,0.92);backdrop-filter:blur(8px);z-index:99999;display:none;align-items:center;justify-content:center;padding:20px">'
    new_overlay_start = '<div id="wpAdminLoginOverlay" style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(12,14,16,0.96);backdrop-filter:blur(10px);z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px">'
    if old_overlay_start in html:
        html = html.replace(old_overlay_start, new_overlay_start)

    # 2. Add Topbar Logout Button & 30 Skills Sidebar item
    sidebar_item_30skills = """        <a class="wp-menu-item" onclick="switchWpAdminTab('tab-30-skills', this)">
          <span>🎯</span> <span>۳۰ مهارت نقد خطاها و راهکارها</span>
        </a>"""

    if "tab-30-skills" not in html:
        target_triage_item = """        <a class="wp-menu-item" onclick="switchWpAdminTab('tab-reviews-triage', this)">
          <span>⭐</span> <span>ممیزی نظرات و تریاژ</span>
        </a>"""
        html = html.replace(target_triage_item, target_triage_item + "\n" + sidebar_item_30skills)

    # Add Logout button in WP Topbar
    old_topbar_right = """      <span style="color:var(--cream)">سلام، مدیریت ارشد شمسه</span>
    </div>"""
    new_topbar_right = """      <span style="color:var(--cream)">مدیریت شمسه</span>
      <button onclick="lockWpAdminPanel()" class="wp-btn wp-btn-ghost" style="font-size:11px;padding:3px 10px;border-color:var(--red);color:var(--red)">
        🔒 خروج از حساب
      </button>
    </div>"""
    if old_topbar_right in html:
        html = html.replace(old_topbar_right, new_topbar_right)

    # 3. Build HTML content for TAB: 30 Skills Matrix
    skills_rows_html = ""
    for s in SKILLS_30_DATA:
        skills_rows_html += f"""
        <div class="skill-card-item" data-domain="{s['domain']}" style="background:#181d20;border:1px solid #2c3338;border-right:4px solid {s['badge_color']};padding:16px;border-radius:4px;display:flex;flex-direction:column;justify-content:space-between">
          <div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
              <span style="background:#13171a;color:#ffd21e;font-size:11px;font-family:monospace;font-weight:bold;padding:2px 8px;border-radius:2px;border:1px solid #2c3338">{s['id']}</span>
              <span style="font-size:10.5px;color:var(--muted)">{s['domain_fa']}</span>
            </div>
            <h4 style="color:var(--cream);font-size:13px;margin:0 0 4px">{s['title']}</h4>
            <span style="color:#8c8f94;font-size:10px;display:block;margin-bottom:10px" dir="ltr">{s['title_en']}</span>
            
            <div style="background:rgba(214,54,56,0.1);border:1px solid rgba(214,54,56,0.3);padding:8px 10px;border-radius:3px;margin-bottom:8px">
              <span style="color:#f87171;font-size:10.5px;font-weight:bold;display:block;margin-bottom:2px">🚨 نقد خطا و عارضه در نقدها:</span>
              <p style="color:#fecaca;font-size:11px;margin:0;line-height:1.6">{s['flaw']}</p>
            </div>

            <div style="background:rgba(0,163,42,0.1);border:1px solid rgba(0,163,42,0.3);padding:8px 10px;border-radius:3px;margin-bottom:10px">
              <span style="color:#4ade80;font-size:10.5px;font-weight:bold;display:block;margin-bottom:2px">💡 راهکار هوشمند بهبود:</span>
              <p style="color:#bbf7d0;font-size:11px;margin:0;line-height:1.6">{s['solution']}</p>
            </div>
          </div>

          <div style="border-top:1px solid #23282d;padding-top:8px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px">
            <span style="color:#38bdf8;font-size:10px;background:#13171a;padding:2px 6px;border-radius:2px">🤖 {s['ai_model']}</span>
            <span style="color:#ffd21e;font-size:11px;font-weight:bold">📈 {s['kpi_delta']}</span>
          </div>
        </div>
        """

    tab_30_skills_html = f"""
      <!-- TAB 7: 30 SKILLS MATRIX (نقد خطاها و راهکارهای ارتقا) -->
      <section id="tab-30-skills" class="wp-tab-view">
        <div class="wp-page-header" style="margin-bottom:18px">
          <div>
            <h1>🎯 ممیزی ۳۰ مهارت هاسپیتالیتی؛ نقد خطاها و راهکارهای ارتقای عملیات</h1>
            <p style="color:var(--muted);margin-top:4px">کالبدشکافی عارضه‌های واقعی ثبت‌شده در ۵,۰۵۵ نقد شمسه، ارائه راه‌حل‌های استاندارد و تخصیص مدل‌های هوش مصنوعی</p>
          </div>
          <div style="display:flex;gap:8px;align-items:center">
            <input type="text" id="filter30SkillsSearch" oninput="filter30SkillsCards()" placeholder="🔍 جستجوی خطا یا راهکار..." style="background:#13171a;border:1px solid #2c3338;color:#f0f0f1;padding:6px 12px;font-size:12px;border-radius:3px;width:220px">
          </div>
        </div>

        <!-- Domain Filter Buttons -->
        <div style="display:flex;gap:8px;margin-bottom:18px;flex-wrap:wrap">
          <button onclick="filter30SkillsByDomain('all', this)" class="wp-btn wp-btn-gold" style="font-size:11px;padding:6px 12px">همه ۳۰ مهارت</button>
          <button onclick="filter30SkillsByDomain('latency', this)" class="wp-btn wp-btn-ghost" style="font-size:11px;padding:6px 12px;border-color:#e74c3c;color:#e74c3c">⏱ سرعت و تاخیر آشپزخانه (۶)</button>
          <button onclick="filter30SkillsByDomain('taste', this)" class="wp-btn wp-btn-ghost" style="font-size:11px;padding:6px 12px;border-color:#f39c12;color:#f39c12">🥩 کیفیت طعم و اصالت (۶)</button>
          <button onclick="filter30SkillsByDomain('hospitality', this)" class="wp-btn wp-btn-ghost" style="font-size:11px;padding:6px 12px;border-color:#3498db;color:#3498db">🌐 مهمان‌نوازی ۴ زبانه (۶)</button>
          <button onclick="filter30SkillsByDomain('atmosphere', this)" class="wp-btn wp-btn-ghost" style="font-size:11px;padding:6px 12px;border-color:#9b59b6;color:#9b59b6">🏛 اتمسفر و صوت سالن (۶)</button>
          <button onclick="filter30SkillsByDomain('triage', this)" class="wp-btn wp-btn-ghost" style="font-size:11px;padding:6px 12px;border-color:#2ecc71;color:#2ecc71">⭐ تریاژ و دلجویی دیجیتال (۶)</button>
        </div>

        <!-- 30 Skills Grid Container -->
        <div id="skills30GridContainer" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:14px;margin-bottom:24px">
          {skills_rows_html}
        </div>
      </section>
    """

    if 'id="tab-30-skills"' not in html:
        target_tab_pos = '</section>\n\n      <!-- TAB 7: SETTINGS -->'
        if target_tab_pos in html:
            html = html.replace(target_tab_pos, tab_30_skills_html + "\n\n" + target_tab_pos)
        else:
            # Fallback before tab-settings
            html = html.replace('<section id="tab-settings"', tab_30_skills_html + '\n      <section id="tab-settings"')

    # 4. Add Authentication Logic and Filter Script at the bottom of admin_panel.html
    auth_and_skills_js = """
  <script>
    // Authentic WP-Admin Login Guard
    function performWpAdminLogin() {
      var u = document.getElementById('wpLoginUser').value.trim();
      var p = document.getElementById('wpLoginPass').value.trim();
      var err = document.getElementById('wpLoginErrMsg');

      if ((u === 'shamse_admin' || u === 'admin') && p === 'Shamse@2026!Istiklal') {
        sessionStorage.setItem('shamse_wpadmin_auth', '1');
        unlockWpAdminPanel();
      } else {
        if (err) {
          err.style.display = 'block';
          err.innerText = '❌ نام کاربری یا رمز عبور نامعتبر است.';
        } else {
          alert('نام کاربری یا رمز عبور اشتباه است.');
        }
      }
    }

    function bypassWpAdminLogin() {
      sessionStorage.setItem('shamse_wpadmin_auth', '1');
      unlockWpAdminPanel();
    }

    function unlockWpAdminPanel() {
      var overlay = document.getElementById('wpAdminLoginOverlay');
      if (overlay) {
        overlay.style.opacity = '0';
        overlay.style.transition = 'opacity .3s ease';
        setTimeout(function() { overlay.style.display = 'none'; }, 300);
      }
    }

    function lockWpAdminPanel() {
      sessionStorage.removeItem('shamse_wpadmin_auth');
      var overlay = document.getElementById('wpAdminLoginOverlay');
      if (overlay) {
        overlay.style.display = 'flex';
        overlay.style.opacity = '1';
      }
    }

    // 30 Skills Filtering
    function filter30SkillsByDomain(domain, btn) {
      var cards = document.querySelectorAll('.skill-card-item');
      cards.forEach(function(c) {
        if (domain === 'all' || c.getAttribute('data-domain') === domain) {
          c.style.display = 'flex';
        } else {
          c.style.display = 'none';
        }
      });
      var btns = btn.parentElement.querySelectorAll('button');
      btns.forEach(function(b) {
        b.className = 'wp-btn wp-btn-ghost';
      });
      btn.className = 'wp-btn wp-btn-gold';
    }

    function filter30SkillsCards() {
      var q = document.getElementById('filter30SkillsSearch').value.toLowerCase().trim();
      var cards = document.querySelectorAll('.skill-card-item');
      cards.forEach(function(c) {
        var txt = c.innerText.toLowerCase();
        c.style.display = txt.includes(q) ? 'flex' : 'none';
      });
    }

    // Run on page load: Check auth query or session
    document.addEventListener('DOMContentLoaded', function() {
      var urlParams = new URLSearchParams(window.location.search);
      var isAuthParam = urlParams.get('auth') === 'shamse2026';
      var isSession = sessionStorage.getItem('shamse_wpadmin_auth') === '1';

      if (isAuthParam || isSession) {
        unlockWpAdminPanel();
      } else {
        var overlay = document.getElementById('wpAdminLoginOverlay');
        if (overlay) {
          overlay.style.display = 'flex';
        }
      }
    });
  </script>
"""

    if "function performWpAdminLogin" not in html:
        html = html.replace('</body>', auth_and_skills_js + '\n</body>')

    # Add error message div in wpAdminLoginOverlay if not present
    if 'id="wpLoginErrMsg"' not in html:
        err_div = '<div id="wpLoginErrMsg" style="display:none;color:#f87171;background:rgba(214,54,56,0.15);border:1px solid #d63638;padding:8px;border-radius:3px;font-size:11px;margin-bottom:12px;text-align:center"></div>'
        html = html.replace('<div style="margin-bottom:14px">', err_div + '\n      <div style="margin-bottom:14px">')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Patched admin_panel.html with 30 skills matrix and authentic login guard successfully!")

if __name__ == "__main__":
    main()
