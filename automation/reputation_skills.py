#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ماژول سامانه ۱۰۰ مهارت هوش تجاری و گیت‌وی‌های چندکاناله پایش نظرات و شبکه‌های اجتماعی
(100 Hospitality Intelligence Skills & Omnichannel Reputation Gateways)

این ماژول ارتباط بین گیت‌وی‌های مختلف (گوگل مپ، یاندکس، اینستاگرام، فیسبوک، وب‌سایت، یمک‌سپتی)
و ۱۰۰ مهارت هوشمند هتلداری و رستوران‌داری را مدیریت می‌کند.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS_FILE = os.path.join(HERE, "hospitality_100_skills.json")

# ---------------------------------------------------------------- ۱) مشخصات گیت‌وی‌های دریافت داده (Omnichannel Gateways)
GATEWAYS = {
    "google-business-profile": {
        "id": "google-business-profile",
        "name_fa": "گیت‌وی گوگل مپ و بیزینس پروفایل (Google Maps & GBP)",
        "name_en": "Google Business Profile & Places API",
        "type": "api_and_webhook",
        "protocol": "REST + Google Cloud Pub/Sub",
        "endpoint": "https://mybusiness.googleapis.com/v4/accounts/{acc}/locations/{loc}/reviews",
        "channels": ["Google Maps", "Google Search Local Pack"],
        "read_frequency": "Real-time Webhook (Push) + Batch Fallback 6h",
        "write_support": True,
        "reply_endpoint": "https://mybusiness.googleapis.com/v4/accounts/{acc}/locations/{loc}/reviews/{revId}/reply",
        "status": "ready",
        "metrics_tracked": ["star_rating", "review_text", "photos_count", "reviewer_profile", "language", "timestamp"]
    },
    "yandex-maps-sprav": {
        "id": "yandex-maps-sprav",
        "name_fa": "گیت‌وی یاندکس مپ و اسپراو (Yandex Maps & Sprav)",
        "name_en": "Yandex Maps & Business Sprav Gateway",
        "type": "api_and_scraper",
        "protocol": "REST + Org Parser",
        "endpoint": "https://search-maps.yandex.ru/v1/ + sprav.yandex.ru/api",
        "channels": ["Yandex Maps", "Yandex Navigator"],
        "read_frequency": "Every 4 hours",
        "write_support": True,
        "reply_endpoint": "https://sprav.yandex.ru/api/reviews/{id}/reply",
        "status": "ready",
        "metrics_tracked": ["rating", "text", "org_id", "author_trust", "photos"]
    },
    "meta-instagram-graph": {
        "id": "meta-instagram-graph",
        "name_fa": "گیت‌وی اینستاگرام گراف (Instagram Graph API)",
        "name_en": "Meta Instagram Graph API",
        "type": "webhook_and_graph_api",
        "protocol": "Meta Graph API v20.0",
        "endpoint": "https://graph.facebook.com/v20.0/{ig-user-id}/comments",
        "channels": ["Instagram Feed", "Instagram Reels", "Instagram Stories", "Direct Messages (DM)"],
        "read_frequency": "Real-time Webhook",
        "write_support": True,
        "reply_endpoint": "https://graph.facebook.com/v20.0/{comment-id}/replies",
        "status": "ready",
        "metrics_tracked": ["comment_text", "media_id", "username", "likes_count", "timestamp", "sentiment"]
    },
    "meta-facebook-page": {
        "id": "meta-facebook-page",
        "name_fa": "گیت‌وی صفحه فیسبوک (Facebook Page Ratings & Feed)",
        "name_en": "Facebook Graph API Page Reviews",
        "type": "graph_api",
        "protocol": "Meta Graph API v20.0",
        "endpoint": "https://graph.facebook.com/v20.0/{page-id}/ratings",
        "channels": ["Facebook Page Reviews", "Community Recommendations", "Post Comments"],
        "read_frequency": "Real-time Webhook",
        "write_support": True,
        "reply_endpoint": "https://graph.facebook.com/v20.0/{rating-id}/comments",
        "status": "ready",
        "metrics_tracked": ["recommendation_type", "review_text", "rating", "author"]
    },
    "tripadvisor-content-api": {
        "id": "tripadvisor-content-api",
        "name_fa": "گیت‌وی تریپ‌ادوایزر (Tripadvisor Content API)",
        "name_en": "Tripadvisor Partner Review API",
        "type": "api",
        "protocol": "REST Partner API",
        "endpoint": "https://api.content.tripadvisor.com/api/v1/location/{locId}/reviews",
        "channels": ["Tripadvisor Istanbul Restaurant Directory"],
        "read_frequency": "Daily",
        "write_support": False,
        "reply_endpoint": "Tripadvisor Management Center Direct Portal",
        "status": "ready",
        "metrics_tracked": ["overall_rating", "sub_ratings", "trip_type", "language", "published_date"]
    },
    "turkish-delivery-portals": {
        "id": "turkish-delivery-portals",
        "name_fa": "گیت‌وی پلتفرم‌های دلیوری ترکی (Yemeksepeti & Trendyol Yemek)",
        "name_en": "Turkish Food Delivery Merchant Gateways",
        "type": "merchant_portal_api",
        "protocol": "Partner API & Ingestion Webhook",
        "endpoint": "https://merchant.yemeksepeti.com/api/v2/reviews + trendyol-partner",
        "channels": ["Yemeksepeti", "Trendyol Yemek", "GetirYemek"],
        "read_frequency": "Every 2 hours during active shifts",
        "write_support": True,
        "reply_endpoint": "/api/v2/reviews/{id}/answer",
        "status": "ready",
        "metrics_tracked": ["flavor_score", "service_score", "speed_score", "customer_notes", "delivery_time"]
    },
    "in-venue-qr-micro-survey": {
        "id": "in-venue-qr-micro-survey",
        "name_fa": "گیت‌وی کیوآرکد نظرسنجی فوری سر میز (In-Venue QR)",
        "name_en": "Table QR Micro-Survey & Direct Site Review",
        "type": "direct_http_webhook",
        "protocol": "Internal REST API /api/feedback/qr",
        "endpoint": "https://shamserestaurants.com/api/feedback/qr",
        "channels": ["Table QR Code", "Official Website /reviews page"],
        "read_frequency": "Instant Push on Form Submission",
        "write_support": True,
        "reply_endpoint": "Direct SMS / Telegram Concierge",
        "status": "active",
        "metrics_tracked": ["table_number", "food_rating", "service_rating", "guest_phone", "immediate_alert"]
    },
    "telegram-bot-concierge": {
        "id": "telegram-bot-concierge",
        "name_fa": "ربات جامع تلگرام و نظرسنجی خودکار (Telegram Bot CRM)",
        "name_en": "Telegram Bot Concierge & Post-Dining Survey",
        "type": "bot_api",
        "protocol": "Telegram Bot API Long-polling & Webhook",
        "endpoint": "https://api.telegram.org/bot{TOKEN}/sendMessage",
        "channels": ["Telegram Bot @Shamse_Restaurant_bot"],
        "read_frequency": "Real-time",
        "write_support": True,
        "reply_endpoint": "Direct chat message to user_id",
        "status": "active",
        "metrics_tracked": ["user_id", "booking_history", "nps_score", "feedback_text", "opt_in_broadcast"]
    }
}

_SKILLS_CACHE = None


# ---------------------------------------------------------------- ۲) لود و جستجوی ۱۰۰ مهارت
def load_skills():
    """بارگذاری داده‌های ساختاریافته ۱۰۰ مهارت هوش تجاری."""
    global _SKILLS_CACHE
    if _SKILLS_CACHE is None:
        if os.path.exists(SKILLS_FILE):
            with open(SKILLS_FILE, "r", encoding="utf-8") as f:
                _SKILLS_CACHE = json.load(f)
        else:
            _SKILLS_CACHE = {"skills": [], "clusters": []}
    return _SKILLS_CACHE


def get_all_skills():
    """دریافت لیست تمام ۱۰۰ مهارت."""
    return load_skills().get("skills", [])


def get_clusters():
    """دریافت دسته‌بندی‌های ۱۰ گانه."""
    return load_skills().get("clusters", [])


def get_skill_by_id(skill_id):
    """جستجوی مهارت بر اساس کد شناسه مانند SKILL-021."""
    skills = get_all_skills()
    for s in skills:
        if s.get("id").upper() == skill_id.upper():
            return s
    return None


def get_skills_by_cluster(cluster_id):
    """فیلتر مهارت‌ها بر اساس خوشه (c1 تا c10)."""
    skills = get_all_skills()
    return [s for s in skills if s.get("cluster_id") == cluster_id]


def search_skills(query):
    """جستجوی متنی میان ۱۰۰ مهارت به فارسی و انگلیسی."""
    if not query:
        return get_all_skills()
    q = query.lower().strip()
    skills = get_all_skills()
    results = []
    for s in skills:
        haystack = " ".join([
            s.get("id", ""),
            s.get("name_fa", ""),
            s.get("name_en", ""),
            s.get("description", ""),
            s.get("engine_tool", ""),
            s.get("trigger", ""),
            s.get("action", "")
        ]).lower()
        if q in haystack:
            results.append(s)
    return results


def get_gateways_status():
    """خلاصه وضعیت گیت‌وی‌های ورودی نظرات."""
    return GATEWAYS


# ---------------------------------------------------------------- ۳) موتور شبیه‌سازی و پایپ‌لاین اجرای مهارت‌ها (Skill Pipeline Engine)
CRISIS_KEYWORDS = [
    "مسموم", "دل‌درد", "حالت تهوع", "مو در غذا", "کثیف", "سوسک",
    "zehirlen", "böcek", "kıl çıktı", "food poisoning", "vomit", "sick"
]

QUEUE_KEYWORDS = [
    "صف", "معطل", "شلوغ", "ایستادیم", "جا نبود",
    "sıra", "bekledik", "kalabalık", "queue", "waited", "line"
]

PRICE_KEYWORDS = [
    "گرون", "گران", "قیمت بالا", "حساب", "فاکتور", "سیر نشدیم",
    "pahalı", "fiyat", "hesap", "porsiyon az", "expensive", "overpriced", "bill"
]

PRAISE_KEYWORDS = [
    "عالی", "فوق‌العاده", "خوشمزه", "بهترین", "دست‌مریزاد", "لذیذ", "نوستالژیک",
    "harika", "mükemmel", "lezzetli", "en iyi", "tebrikler", "delicious", "amazing", "authentic", "best"
]


def detect_language(text):
    """تشخیص ساده زبان متن نظر (fa, tr, en, ar)."""
    if not text:
        return "fa"
    # Arabic letters not usually in Persian
    if any(c in text for c in ["ة", "ي", "ؤ", "إ"]):
        return "ar"
    # Turkish letters
    if any(c in text for c in ["ş", "Ş", "ı", "İ", "ğ", "Ğ", "ç", "Ç", "ü", "Ü", "ö", "Ö"]):
        return "tr"
    # Persian alphabet check
    if re.search(r"[\u0600-\u06FF]", text):
        return "fa"
    return "en"


def simulate_review_pipeline(channel, rating, text, author="کاربر مهمان", dish_hint=None):
    """
    اجرای شبیه‌سازی هوشمند خط‌لوله نظرات (Pipeline):
    ۱. دریافت از گیت‌وی مشخص
    ۲. تشخیص زبان و تحلیل حس
    ۳. تطبیق با ۱۰۰ مهارت هوش تجاری و فعال‌سازی مهارت‌های متناسب
    ۴. تولید پاسخ چندزبانه و دستور کار داخلی
    """
    lang = detect_language(text)
    lower = text.lower() if text else ""
    rating = float(rating)

    # سنجش احساسات
    sentiment_score = 0.0
    if rating >= 4.5:
        sentiment_score = 0.85
    elif rating >= 3.5:
        sentiment_score = 0.4
    elif rating >= 2.5:
        sentiment_score = -0.2
    else:
        sentiment_score = -0.85

    # مهارت‌های فعال‌شده (Triggered Skills)
    triggered_skills = []

    # 1. Gateway ingestion skill
    if "google" in channel.lower():
        triggered_skills.append("SKILL-001")
        triggered_skills.append("SKILL-026")
    elif "instagram" in channel.lower():
        triggered_skills.append("SKILL-004")
        triggered_skills.append("SKILL-028")
    elif "yandex" in channel.lower():
        triggered_skills.append("SKILL-003")
    elif "facebook" in channel.lower():
        triggered_skills.append("SKILL-006")
    elif "qr" in channel.lower() or "table" in channel.lower():
        triggered_skills.append("SKILL-009")

    # 2. NLP Language skill
    if lang == "fa":
        triggered_skills.append("SKILL-011")
    elif lang == "tr":
        triggered_skills.append("SKILL-012")
    elif lang == "ar":
        triggered_skills.append("SKILL-014")
    else:
        triggered_skills.append("SKILL-013")

    # 3. Crisis or praise detection
    is_crisis = False
    crisis_type = None

    if any(k in lower for k in CRISIS_KEYWORDS) or (rating <= 2.0 and "بهداشت" in lower):
        is_crisis = True
        crisis_type = "safety"
        triggered_skills.extend(["SKILL-031", "SKILL-035", "SKILL-037"])

    if any(k in lower for k in QUEUE_KEYWORDS):
        triggered_skills.extend(["SKILL-023", "SKILL-081"])

    if any(k in lower for k in PRICE_KEYWORDS):
        triggered_skills.extend(["SKILL-042", "SKILL-039"])

    if rating >= 4.0:
        triggered_skills.append("SKILL-021")
        triggered_skills.append("SKILL-091")
    elif rating <= 2.0:
        triggered_skills.append("SKILL-022")
        triggered_skills.append("SKILL-025")
        triggered_skills.append("SKILL-029")

    if dish_hint or any(d in lower for d in ["قورمه", "کوبیده", "شیشلیک", "کشک بادمجان", "دیزی"]):
        triggered_skills.append("SKILL-016")
        triggered_skills.append("SKILL-041")

    # حذف تکراری‌ها با حفظ ترتیب
    seen = set()
    unique_skills = []
    for sid in triggered_skills:
        if sid not in seen:
            seen.add(sid)
            s_obj = get_skill_by_id(sid)
            if s_obj:
                unique_skills.append({
                    "id": s_obj["id"],
                    "name_fa": s_obj["name_fa"],
                    "cluster_id": s_obj["cluster_id"],
                    "action": s_obj["action"]
                })

    # تولید پاسخ هوشمند متناسب
    if is_crisis:
        ai_reply = (
            f"سلام و احترام جناب/سرکار {author} عزیز؛ "
            "پیام شما در بالاترین اولویت بررسی مدیریت و سرآشپز قرار گرفت. سلامت و رضایت مهمانان خط قرمز مطلق ماست. "
            "خواهشمندیم جهت پیگیری فوری، جبران خسارت و گفتگوی مستقیم، با شماره پشتیبانی 05528574040 در واتساپ یا تلگرام تماس حاصل فرمایید."
        )
        action_note = "🚨 هشدار قرمز: ارجاع فوری به سرآشپز و مدیر داخلی جهت بررسی شیفت پخت و تماس دلجویی."
    elif rating >= 4.0:
        ai_reply = (
            f"از لطف، نگاه پرمهر و انرژی فوق‌العاده شما در {channel} بسیار سپاسگزاریم {author} گرامی! "
            "طعم اصیل ایرانی و میزبانی شایسته از شما افتخار همیشگی تیم ما در قلب استانبول است. "
            "مشتاقانه منتظر دیدار دوباره شما در رویدادها و دورهمی‌های پنجشنبه‌های شمسه هستیم. 🌸"
        )
        action_note = "✅ ثبت در لیست مروجان (Promoter) و ارسال دعوت به ایونت‌های طبقه دوم."
    elif any(k in lower for k in QUEUE_KEYWORDS):
        ai_reply = (
            f"با سلام خدمت {author} عزیز؛ از معطلی پیش‌آمده در ساعات اوج شلوغی پیاده‌راه استقلال صمیمانه پوزش می‌طلبیم. "
            "برای اینکه دفعه بعد بدون حتی یک لحظه معطلی میز رزروشده و آماده داشته باشید، "
            "می‌توانید به سادگی از طریق ربات تلگرام (دستور /reserve) یا سایت میزتان را رزرو فرمایید."
        )
        action_note = "⏳ ثبت تگ انتظار صف و ارزیابی ظرفیت خالی ساعات غیر اوج (Yield Management)."
    else:
        ai_reply = (
            f"سلام و احترام خدمت شما {author} عزیز؛ از اینکه وقت ارزشمندتان را به اشتراک تجربه با ما اختصاص دادید سپاسگزاریم. "
            "نکات مطرح‌شده مستقیماً به بخش کنترل کیفیت ارجاع شد تا تجربه‌ای بی‌نقص برای شما فراهم آوریم. "
            "همواره مشتاق میزبانی شایسته از شما هستیم."
        )
        action_note = "⚠️ ثبت فیدبک در سیستم بهبود مستمر و تخصیص کد تخفیف جبرانی."

    return {
        "channel": channel,
        "rating": rating,
        "language": lang,
        "sentiment_score": sentiment_score,
        "is_crisis": is_crisis,
        "crisis_type": crisis_type,
        "triggered_skills_count": len(unique_skills),
        "triggered_skills": unique_skills,
        "generated_ai_reply": ai_reply,
        "internal_action_note": action_note
    }


if __name__ == "__main__":
    print(f"Total skills in database: {len(get_all_skills())}")
    print(f"Total clusters: {len(get_clusters())}")
    print(f"Active Gateways: {len(get_gateways_status())}")
    sim = simulate_review_pipeline("Google Maps", 5, "خورش قورمه‌سبزی شمسه بی‌نظیر بود، درست مثل دستپخت مادربزرگم!", "علی راد")
    print("\nSimulation Result:")
    print("Language:", sim["language"])
    print("Triggered Skills:", [s["id"] for s in sim["triggered_skills"]])
    print("AI Reply:", sim["generated_ai_reply"])
