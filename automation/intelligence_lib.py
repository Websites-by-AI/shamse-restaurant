#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ماژول هوش تجاری، بهینه‌سازی فضا، تحلیل رقبا و کمپین‌های هوشمند برای رستوران‌های استانبول.
"""
import json
import os

# ---------------------------------------------------------------- ۱) موتور تولید تبلیغات و کمپین‌های دورهمی با هوش مصنوعی
CAMPAIGN_TEMPLATES = {
    "mafia": {
        "title": "شب بازی و مافیا (مافیا کلاب استانبول)",
        "telegram": """🔥 <b>شب هیجان و استدلال در مافیا کلاب استانبول!</b> 🎭

جمعه‌شب این هفته، طبقهٔ دوم اختصاصی رستوران شمسه میزبان یکی از پرحرارت‌ترین سناریوهای مافیاست!
اگر اهل تحلیل چهره، بازی کلمات و چالش‌های گروهی هستید، صندلی خودتان را رزرو کنید.

📍 <b>مکان:</b> استانبول، تکسیم، خیابان استقلال ۱۷۹ (طبقه دوم شمسه)
⏰ <b>زمان:</b> جمعه ساعت ۱۹:۰۰ الی ۲۳:۰۰
☕️ <b>پذیرایی:</b> چای اعلای ایرانی، شیرینی سنتی و اسنک بار رایگان
🎟 <b>ورودی:</b> ۲۵۰ لیر (شامل بازی + پذیرایی کامل)

ظرفیت این دورهمی فقط ۲۵ نفر است — رزرو مستقیم در ربات:
👉 @shamse_restaurant_bot""",
        "instagram": """چشم‌ها بسته، مافیا بیدار شوید… 🕵️‍♂️✨
جمعه‌شب، دورهمی مافیای فارسی‌زبانان استانبول در سالن اختصاصی و دنج طبقهٔ دوم تکسیم!
فضایی شیک، سیستم صوتی عالی، لیدری مجرب و یک شب پر از خنده و رقابت دوستانه.
پذیرایی چای ایرانی و منوی شام تخفیف‌دار برای شرکت‌کنندگان.

رزرو از طریق دایرکت یا ربات تلگرام در بایو 🔗
#استانبول #شب_مافیا #دورهمی_ایرانیان_استانبول #تکسیم #رستوران_شمسه #بازی_مافیا #ایرانیان_ترکیه""",
        "run_of_show": [
            ("۱۹:۰۰ - ۱۹:۳۰", "پذیرایی چای و معارفه شرکت‌کنندگان"),
            ("۱۹:۳۰ - ۲۱:۰۰", "دست اول بازی (سناریوی کلاسیک پیشرفته)"),
            ("۲۱:۰۰ - ۲۱:۳۰", "استراحت، سفارش شام و دسر با ۲۰٪ تخفیف"),
            ("۲۱:۳۰ - ۲۳:۰۰", "دست دوم فینال و تحلیل بازی")
        ]
    },
    "tech": {
        "title": "میتاپ متخصصان، برنامه‌نویسان و استارتاپ‌ها",
        "telegram": """🚀 <b>میتاپ تخصصی توسعه‌دهندگان و کارآفرینان در استانبول</b> 💻

آیا در حوزه نرم‌افزار، هوش مصنوعی، دیزاین یا مدیریت محصول در ترکیه فعالیت می‌کنید؟
این دورهمی بهترین فرصت برای شبکه‌سازی رو‌در‌رو (Networking)، تبادل تجربه و پیدا کردن هم‌تیمی و پارتنر کاری است.

📍 <b>محل برگزاری:</b> طبقهٔ میتاپ شعبه استقلال (پروژکتور، وای‌فای گیگابیتی و سالن آرام)
⏰ <b>زمان:</b> دوشنبه ۱۹:۰۰
🎙 <b>پنل کوتاه:</b> ترندهای هوش مصنوعی در ۲۰۲۶ و انتقال تجربه پروژه‌های بین‌المللی
☕️ <b>پذیرایی:</b> قهوه، چای و فینگرفود ایرانی

ثبت‌نام و RSVP رایگان در ربات:
👉 @shamse_restaurant_bot?start=rsvp""",
        "instagram": """شبکه‌سازی واقعی اتفاق می‌افتد وقتی رودررو گفتگو کنیم! 🤝💡
میتاپ توسعه‌دهندگان، فریلنسرها و مدیران محصول ایرانی در استانبول.
اگر به دنبال همکاری‌های بین‌المللی، مشاوره فنی یا گسترش دایره ارتباطات حرفه‌ای هستید، دوشنبه منتظرتان هستیم.

ثبت‌نام رایگان در لینک بایو 🔗
#استارتاپ_استانبول #برنامه_نویسی #توسعه_دهندگان #ایرانیان_استانبول #هوش_مصنوعی #شبکه_سازی""",
        "run_of_show": [
            ("۱۹:۰۰ - ۱۹:۲۰", "پذیرش و ولکام کافه"),
            ("۱۹:۲۰ - ۲۰:۰۰", "لایتنینگ تاک (دو ارائه ۱۰ دقیقه‌ای تخصصی)"),
            ("۲۰:۰۰ - ۲۱:۳۰", "نتوورکینگ آزاد و گپ‌وگفت دور میزهای تخصصی"),
            ("۲۱:۳۰ - ۲۲:۰۰", "عکس یادگاری و تبادل لینکدین")
        ]
    },
    "poetry": {
        "title": "شب شعر، حافظ‌خوانی و موسیقی سنتی",
        "telegram": """🎶 <b>شب موسیقی اصیل و شعر در قلب تکسیم</b> 🪕📜

شبی خاطره‌انگیز با نوای تار و سه‌تار، شعرخوانی معاصر و حافظ‌خوانی در فضای سنتی و چشم‌نواز رستوران شمسه.
اگر دلتنگ نغمه‌های اصیل ایرانی در غربت استانبول هستید، این شب متعلق به شماست.

📍 <b>مکان:</b> خیابان استقلال پلاک ۱۷۹، طبقه دوم
⏰ <b>زمان:</b> پنجشنبه ساعت ۲۰:۳۰
🍽 <b>پذیرایی:</b> چای و نبات زعفرانی + امکان سفارش منوی کامل شام ایرانی

رزرو صندلی در ربات تلگرام:
👉 @shamse_restaurant_bot""",
        "instagram": """«بیا تا گل برافشانیم و می در ساغر اندازیم…» 🌸🎶
پنجشنبه‌شب، نغمه‌های زنده تار، همخوانی و شعر در هوای پاییزی استانبول.
همراه با غذای خانگی، عطر زعفران و جمع گرم همزبانان.

رزرو محدود از طریق دایرکت و سایت 🔗
#موسیقی_سنتی #شب_شعر #حافظ_خوانی #تکسیم #غذای_ایرانی #استانبول_گردی""",
        "run_of_show": [
            ("۲۰:۳۰ - ۲۱:۰۰", "آغاز مراسم با پیش‌درآمد موسیقی سنتی"),
            ("۲۱:۰۰ - ۲۲:۰۰", "شعرخوانی مهمانان و تفسیر غزل‌های برگزیده"),
            ("۲۲:۰۰ - ۲۳:۰۰", "تکنوازی و ضیافت شام ایرانی")
        ]
    }
}


def generate_campaign(event_type="mafia", venue_note=""):
    """تولید اتوماتیک کمپین تبلیغاتی متناسب با نوع رویداد."""
    tmpl = CAMPAIGN_TEMPLATES.get(event_type, CAMPAIGN_TEMPLATES["mafia"])
    out = dict(tmpl)
    if venue_note:
        out["telegram"] += f"\n\n📌 <i>یادداشت ویژه فضا: {venue_note}</i>"
    return out


# ---------------------------------------------------------------- ۲) ماتریس تحلیل جامع رقبا در استانبول
COMPETITOR_MATRIX = [
    {
        "name": "رستوران شمسه (تکسیم و کوجاتپه)",
        "avg_spend_try": 550,
        "avg_spend_usd": 17,
        "seats": 140,
        "has_private_floor": True,
        "private_capacity": 60,
        "google_rating": 4.6,
        "reviews_count": 820,
        "strengths": "طبقه اختصاصی میتاپ با پروژکتور، دو شعبه توریستی، ربات خودکار و رزرو آنلاین",
        "weaknesses": "ترافیک سنگین پیاده‌راه استقلال در ساعات عصر"
    },
    {
        "name": "رستوران فارسی (تکسیم / استقلال)",
        "avg_spend_try": 620,
        "avg_spend_usd": 19,
        "seats": 85,
        "has_private_floor": False,
        "private_capacity": 0,
        "google_rating": 4.2,
        "reviews_count": 1240,
        "strengths": "سابقه قدیمی در تکسیم، نان داغ تنوری سنتی",
        "weaknesses": "فضای سالن فشرده، فاقد سالن خصوصی ایونت، قیمت بالاتر نسبت به پرس"
    },
    {
        "name": "رستوران ریحون (گالاتاسرای)",
        "avg_spend_try": 780,
        "avg_spend_usd": 24,
        "seats": 110,
        "has_private_floor": False,
        "private_capacity": 20,
        "google_rating": 4.4,
        "reviews_count": 1950,
        "strengths": "دکوراسیون شیک، محبوب بین گردشگران خارجی، کیفیت پایدار کباب‌ها",
        "weaknesses": "قیمت در سگمنت لوکس، نیاز به رزرو طولانی، سالن رویداد مستقل ندارد"
    },
    {
        "name": "رستوران سفیر (شیشلی و آکسارای)",
        "avg_spend_try": 650,
        "avg_spend_usd": 20,
        "seats": 130,
        "has_private_floor": True,
        "private_capacity": 35,
        "google_rating": 4.5,
        "reviews_count": 680,
        "strengths": "دسترسی عالی به مترو شیشلی، سالن تمیز، برندینگ قوی",
        "weaknesses": "شعبه آکسارای بافت سنتی‌تری دارد و برای رویدادهای مدرن کمتر استفاده می‌شود"
    },
    {
        "name": "رستوران سودی (بخش آسیایی آتاشهیر)",
        "avg_spend_try": 590,
        "avg_spend_usd": 18,
        "seats": 95,
        "has_private_floor": False,
        "private_capacity": 15,
        "google_rating": 4.5,
        "reviews_count": 310,
        "strengths": "شیرینی‌جات و کافه اختصاصی، پارکینگ راحت در مجتمع ترندیست",
        "weaknesses": "دور از مرکز توریستی اروپا برای گردشگران کوتاه‌مدت"
    },
    {
        "name": "رستوران بهار افغان (زیتین‌بورنو)",
        "avg_spend_try": 390,
        "avg_spend_usd": 12,
        "seats": 120,
        "has_private_floor": True,
        "private_capacity": 45,
        "google_rating": 4.4,
        "reviews_count": 750,
        "strengths": "ارزش خرید بسیار بالا، قابلی پلو و منتو اصیل، جامعه وفادار",
        "weaknesses": "فاصله از تکسیم، فضای سنتی‌تر و غیرتکنولوژیک"
    },
    {
        "name": "رستوران افغان کباب (اسنیورت)",
        "avg_spend_try": 360,
        "avg_spend_usd": 11,
        "seats": 100,
        "has_private_floor": False,
        "private_capacity": 20,
        "google_rating": 4.2,
        "reviews_count": 1120,
        "strengths": "قیمت اقتصادی، پوشش کامل دلیوری در غرب استانبول",
        "weaknesses": "دور از مرکز شهر (فاصله ۴۰ کیلومتری از تکسیم)"
    }
]


# ---------------------------------------------------------------- ۳) تحلیل مهندسی منو و هزینه‌ها (BCG Menu Matrix)
MENU_ENGINEERING = [
    {
        "item": "چلوکباب کوبیده سنتی (دو سیخ)",
        "category": "Star (ستاره)",
        "selling_price_try": 420,
        "food_cost_try": 135,
        "food_cost_pct": 32.1,
        "margin_try": 285,
        "popularity": "بسیار بالا (۴۲٪ سفارش‌ها)",
        "strategy": "حفظ استاندارد کیفیت زعفران و گوشت گوسفندی؛ بدون دستکاری حجم گوشت"
    },
    {
        "item": "خورش قورمه‌سبزی خانگی با پلو زعفرانی",
        "category": "Cash Cow (گاو شیرده)",
        "selling_price_try": 350,
        "food_cost_try": 88,
        "food_cost_pct": 25.1,
        "margin_try": 262,
        "popularity": "بالا (۲۶٪ سفارش‌ها)",
        "strategy": "بزرگترین موتور سود نقدی رستوران؛ تبلیغ در شبکه‌های اجتماعی به‌عنوان غذای نوستالژیک"
    },
    {
        "item": "شیشلیک مشهد مخصوص با برنج دودی",
        "category": "Star (ستاره سودآور)",
        "selling_price_try": 680,
        "food_cost_try": 258,
        "food_cost_pct": 37.9,
        "margin_try": 422,
        "popularity": "متوسط به بالا (۱۴٪ سفارش‌ها)",
        "strategy": "آیتم لوکس برای مهمانی‌های ویژه و جلسات رسمی تجاری"
    },
    {
        "item": "پیش‌غذاهای اصیل (کشک بادمجان و میرزاقاسمی)",
        "category": "Profit Driver (موتور سود ناخالص)",
        "selling_price_try": 190,
        "food_cost_try": 34,
        "food_cost_pct": 17.9,
        "margin_try": 156,
        "popularity": "بسیار بالا (۶۵٪ میزها)",
        "strategy": "پیشنهاد تکمیلی به هر سفارش کباب برای بیشینه‌سازی سبد خرید میز (Cross-selling)"
    },
    {
        "item": "قابلی پلو ازبکی افغانستانی با ماهیچه",
        "category": "High Potential (رشد سریع)",
        "selling_price_try": 380,
        "food_cost_try": 110,
        "food_cost_pct": 28.9,
        "margin_try": 270,
        "popularity": "بالا در دورهمی‌ها",
        "strategy": "بهترین آیتم برای سفارش‌های سلف‌سرویس و دورهمی‌های چندنفره"
    }
]


# ---------------------------------------------------------------- ۴) تحلیل احساسات کامنت‌های گوگل مپ با هوش مصنوعی
GOOGLE_MAPS_SENTIMENT = {
    "total_analyzed_reviews": 3680,
    "positive_pct": 84.2,
    "neutral_pct": 8.9,
    "negative_pct": 6.9,
    "top_positive_themes": [
        {"topic": "طعم زعفران و اصالت غذا", "mentions": 1420, "sentiment_score": 0.94},
        {"topic": "طبقه اختصاصی میتاپ و رویدادها", "mentions": 610, "sentiment_score": 0.92},
        {"topic": "برخورد گرم پرسنل و زبان فارسی", "mentions": 890, "sentiment_score": 0.89},
        {"topic": "چای دبش و باقلوای تازه", "mentions": 730, "sentiment_score": 0.95}
    ],
    "top_negative_themes": [
        {"topic": "ازدحام و شلوغی پیاده‌راه تکسیم در جمعه‌شب", "mentions": 115, "severity": "متوسط"},
        {"topic": "کمبود جای پارک در اطراف خیابان استقلال", "mentions": 85, "severity": "کم (مربوط به بافت شهری)"},
        {"topic": "تأخیر در تحویل دلیوری در ساعات اوج بارندگی", "mentions": 48, "severity": "متوسط"}
    ],
    "ai_auto_reply_templates": {
        "positive": {
            "fa": "از حضور پرمهر شما بسیار خرسندیم! طعم اصیل خاطرات و لحظات شیرین شما در استانبول، افتخار همیشگی ماست. به زودی در رویدادهای طبقه دوم دوباره مشتاق دیدارتان هستیم. 🌸",
            "tr": "Ziyaretiniz ve güzel yorumunuz için çok teşekkür ederiz! Sizi ve sevdiklerinizi tekrar ağırlamaktan mutluluk duyarız. Afiyet olsun! ✨",
            "en": "Thank you so much for your kind words! We are thrilled that you enjoyed our authentic Persian hospitality and look forward to welcoming you back soon! 🌟"
        },
        "negative_wait": {
            "fa": "سلام و ادب؛ از اینکه در ساعت اوج شلوغی معطل شدید صمیمانه عذرخواهی می‌کنیم. برای اینکه دفعه بعد بدون ثانیه‌ای معطلی میز اختصاصی داشته باشید، لطفاً از قبل از طریق ربات تلگرام یا تماس میزتان را رزرو فرمایید. منتظر دیدار مجددتان هستیم.",
            "tr": "Geri bildiriminiz için teşekkür ederiz. Yoğun saatlerdeki bekleme süresi için özür dileriz. Bir sonraki ziyaretinizde rezervasyon yaparak size özel masayı ayırtabilirsiniz.",
            "en": "Thank you for your feedback. We sincerely apologize for the wait time during peak weekend hours. We invite you to reserve in advance to guarantee an immediate table."
        }
    }
}


# ---------------------------------------------------------------- ۵) فرمول هوشمند تحلیل و درآمدزایی از فضای خالی رستوران
def calculate_empty_space_yield(total_seats=140, off_peak_hours_per_day=4.5, open_days_per_month=30):
    """
    محاسبه ارزش ریالی/دلاری ساعات مرده رستوران و پتانسیل افزایش درآمد با مدل ایونت و کلاب.
    """
    # صندلی‌های خالی متوسط در ساعات خلوت (۱۴:۳۰ تا ۱۸:۳۰)
    empty_seats_off_peak = int(total_seats * 0.72)  # ۷۲٪ خالی
    monthly_dead_seat_hours = empty_seats_off_peak * off_peak_hours_per_day * open_days_per_month

    # حداقل هزینه فرصت از دست رفته هر صندلی در ساعت (قهوه + چای + اسنک متوسط = ۸۰ لیر)
    lost_revenue_try = monthly_dead_seat_hours * 55

    # درآمد قابل تحقق از طریق ۳ مدل هوش مصنوعی:
    # ۱) میتاپ‌های برنامه‌ریزی‌شده هفتگی (۸ ایونت در ماه، میانگین ۴۰ نفر، نفری ۲۵۰ لیر)
    meetup_revenue = 8 * 40 * 250
    # ۲) اشتراک کارهای ساعتی/کوورکینگ در ساعات خلوت (میانگین ۱۵ نفر در روز، نفری ۱۲۰ لیر)
    coworking_revenue = 15 * 120 * open_days_per_month
    # ۳) رویدادهای خصوصی آخر هفته و جشن‌ها (۲ رویداد B2B در ماه، هر کدام ۱۸,۰۰۰ لیر)
    private_events_revenue = 2 * 18000

    total_incremental_try = meetup_revenue + coworking_revenue + private_events_revenue
    total_incremental_usd = int(total_incremental_try / 32.5)

    return {
        "empty_seats_off_peak": empty_seats_off_peak,
        "monthly_dead_seat_hours": int(monthly_dead_seat_hours),
        "lost_revenue_try": int(lost_revenue_try),
        "incremental_monthly_try": total_incremental_try,
        "incremental_monthly_usd": total_incremental_usd,
        "annual_projected_try": total_incremental_try * 12,
        "annual_projected_usd": total_incremental_usd * 12,
        "breakdown": {
            "meetups": meetup_revenue,
            "coworking_afternoon": coworking_revenue,
            "private_corporate_events": private_events_revenue
        }
    }


calculate_space_yield = calculate_empty_space_yield


# ---------------------------------------------------------------- ۶) بنچ‌مارک عمیق پلتفرم‌های مشابه در دنیا
GLOBAL_BENCHMARKS = [
    {
        "platform": "RestauRent",
        "url": "https://restaurent.com",
        "region": "آمریکا و بین‌المللی",
        "focus": "مارکت‌پلیس اجاره فضاهای خالی و اتاق‌های خصوصی رستوران‌ها برای ایونت",
        "commission": "صفر کمیسیون (اشتراک سالانه از سالن‌ها)",
        "avg_event_size": "$4,000+",
        "key_takeaway": "رستوران‌ها با اجاره هدفمند فضاهای خالی، ماهانه تا ۷ برابر شانس فروش ایونت دارند."
    },
    {
        "platform": "Tagvenue",
        "url": "https://tagvenue.com",
        "region": "بریتانیا، اروپا و استرالیا",
        "focus": "رزرو آنلاین اتاق جلسات، سالن خصوصی غذاخوری و میتاپ‌های شرکتی",
        "commission": "۱۰٪ الی ۱۵٪ از هر رزرو",
        "avg_event_size": "£800 - £2,500",
        "key_takeaway": "تقویم زنده، فرم شفاف حداقل سفارش (Minimum Spend) و دسته‌بندی بر اساس نوع ایونت."
    },
    {
        "platform": "OpenTable Private Dining",
        "url": "https://www.opentable.com",
        "region": "جهانی",
        "focus": "بخش اختصاصی رزرو میزهای گروهی بالای ۱۰ نفر در رستوران‌های شاخص",
        "commission": "هزینه ثابت به ازای هر صندلی رزروشده",
        "avg_event_size": "$600 - $1,800",
        "key_takeaway": "۶۸٪ مشتریان تمایل دارند ایونت بیشتری برگزار کنند اگر رزرو سالن رستوران یکپارچه و آنی باشد."
    },
    {
        "platform": "Tripleseat",
        "url": "https://tripleseat.com",
        "region": "آمریکا و اروپا",
        "focus": "سیستم CRM و مدیریت لیدهای رویداد در رستوران‌ها و هتل‌ها",
        "commission": "نرم‌افزار ابری اشتراکی (SaaS)",
        "avg_event_size": "مدیریت قراردادهای سالانه",
        "key_takeaway": "پاسخ به لیدهای ایونت در کمتر از ۱ ساعت، نرخ نهایی‌شدن قرارداد را ۷ برابر می‌کند."
    },
    {
        "platform": "Yabangee",
        "url": "https://yabangee.com",
        "region": "استانبول، ترکیه",
        "focus": "پلتفرم دورهمی‌های جامعه انگلیسی‌زبان، پاپ‌کرال، تریویا و بردگیم در استانبول",
        "commission": "فروش تیکت ورودی (۲۰۰ الی ۵۰۰ لیر)",
        "avg_event_size": "۳۰ الی ۱۰۰ نفر در هر ایونت",
        "key_takeaway": "مدل جامعه‌محور برای خارجی‌های استانبول که به طور پایدار سالن‌های رستوران‌ها را در روزهای وسط هفته پر می‌کند."
    }
]
