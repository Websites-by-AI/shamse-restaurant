#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
موتور تحلیل شمعی احساسات و مقایسه راهکارهای فناورانه سنگین در برابر راه‌حل‌های فوری کم‌هزینه
Forex-Style Candlestick Sentiment Engine & High-Tech vs. Easy Fix Comparison with Dual Calendars

ویژگی‌ها:
۱. نمودار کندل‌استیک فارکس ۶ دوره شیفت کاری (Open, High, Low, Close, Volume)
۲. تقویم دوگانه برای هر کامنت (هجری شمسی و میلادی + ساعت اوج شیفت)
۳. جدول مقایسه راهکار های‌تک سنگین (Huge High-Tech AI) در برابر فیکس سریع و آسان (Easy Quick Fix / Instant SOP)
۴. نگاشت به چارچوب ۱۰۰ مهارت هاسپیتالیتی
۵. پشتیبانی از پادکست دو زبانه (فارسی و ترکی استانبولی)
"""

import json
import os
from typing import List, Dict, Any

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ۶ جلسه/دوره کندل‌استیک شیفت‌های کاری رستوران شمسه
CANDLESTICK_SESSIONS = [
    {
        "id": "CANDLE-01",
        "session_name": "جمعه شب: پیک ترافیک استقلال",
        "session_name_en": "Friday Night: Istiklal Peak Rush",
        "date_shamsi": "۲۴ مهر ۱۴۰۵",
        "date_miladi": "16 October 2026",
        "time_slot": "۲۰:۳۰ الی ۲۳:۳۰",
        "open": 4.80,
        "high": 4.90,
        "low": 4.10,
        "close": 4.55,
        "volume_guests": 1450,
        "candle_type": "bearish_dip_recovery",
        "color": "#e74c3c",  # قرمز متمایل به اصلاح
        "primary_flaw": "تاخیر ۳۵ دقیقه‌ای تحویل برنج در پیک شلوغی (کامنت مهسا رضایی)",
        "high_tech_solution": "استقرار سامانه کامپیوتر ویژن، پایش پیوسته صف ورودی با مدل YOLOv8 و سیستم زمان‌بندی KDS تمام خودکار آشپزخانه",
        "high_tech_tag": "High-Tech AI Frontier",
        "high_tech_cost": "$8,500 + اشتراک ابری",
        "high_tech_timeline": "۳ هفته پیاده‌سازی",
        "easy_fix_solution": "پروتکل ۵ دقیقه‌ای استقرار پلوپزهای کته قالبی پیش‌پخت هوشمند و پذیرایی رایگان نان داغ و سوپ جو به محض نشستن",
        "easy_fix_tag": "Easy Quick Fix / 5-Min SOP",
        "easy_fix_cost": "۱,۲۰۰ لیر (هزینه ۲ دیگ کته قالبی)",
        "easy_fix_timeline": "اجرای فوری در شیفت بعدی",
        "skill_code": "SKILL-01",
        "skill_domain": "سرعت سرویس و ریتم میزها"
    },
    {
        "id": "CANDLE-02",
        "session_name": "شنبه ظهر: ناهار خانوادگی مسافران",
        "session_name_en": "Saturday Lunch: Family & Tahdig Rush",
        "date_shamsi": "۲۵ مهر ۱۴۰۵",
        "date_miladi": "17 October 2026",
        "time_slot": "۱۳:۰۰ الی ۱۶:۰۰",
        "open": 4.60,
        "high": 4.88,
        "low": 4.30,
        "close": 4.75,
        "volume_guests": 1120,
        "candle_type": "bullish_gain",
        "color": "#2ecc71",  # سبز صعودی
        "primary_flaw": "عدم یکدستی برشتگی و تردی ته‌دیگ زعفرانی در شیفت‌های مختلف (کامنت آرش نیکزاد)",
        "high_tech_solution": "سنسورهای هوشمند اینترنت اشیا (IoT Sensor-Cook) با ترموکوپل‌های دیجیتال زیر کف دیگ‌های مسی جهت کنترل دمای برشتگی",
        "high_tech_tag": "High-Tech AI Frontier",
        "high_tech_cost": "$3,200",
        "high_tech_timeline": "۱۰ روز نصب سخت‌افزاری",
        "easy_fix_solution": "تنظیم تایمر زنگ‌دار ۲۵ دقیقه‌ای برای هر دیگ برنج و استفاده از پیمانه استاندارد ترکیب زعفران دم‌کرده و ماست چکیده",
        "easy_fix_tag": "Easy Quick Fix / 5-Min SOP",
        "easy_fix_cost": "۱۵۰ لیر (خرید تایمر دیجیتال)",
        "easy_fix_timeline": "اجرای همان روز",
        "skill_code": "SKILL-07",
        "skill_domain": "کیفیت طعم و اصالت پخت"
    },
    {
        "id": "CANDLE-03",
        "session_name": "یکشنبه عصر: تورهای گردشگران غربی",
        "session_name_en": "Sunday Afternoon: European Tourists",
        "date_shamsi": "۲۶ مهر ۱۴۰۵",
        "date_miladi": "18 October 2026",
        "time_slot": "۱۶:۳۰ الی ۱۹:۳۰",
        "open": 4.50,
        "high": 4.82,
        "low": 4.05,
        "close": 4.68,
        "volume_guests": 980,
        "candle_type": "bullish_recovery",
        "color": "#2ecc71",
        "primary_flaw": "ابهام توریست‌های انگلیسی در مورد کوور شارژ و رایگان بودن چای (کامنت David Miller)",
        "high_tech_solution": "سیستم جامع Billing AI با صورت‌حساب الکترونیکی داینامیک، تفکیک چندارزی خودکار و نمایشگر تبلت سر میز با تایید اثر انگشت",
        "high_tech_tag": "High-Tech AI Frontier",
        "high_tech_cost": "$4,500",
        "high_tech_timeline": "۲ هفته راه‌اندازی نرم‌افزاری",
        "easy_fix_solution": "چاپ پلاکارد دوزبانه روی میزها و عبارت برجسته: Complimentary Welcome Saffron Tea - No Hidden Charges روی برگه فاکتور",
        "easy_fix_tag": "Easy Quick Fix / 5-Min SOP",
        "easy_fix_cost": "۸۰ لیر (چاپ استند اکریلیک میز)",
        "easy_fix_timeline": "اجرای ۲ ساعته",
        "skill_code": "SKILL-25",
        "skill_domain": "شفافیت صورت‌حساب و تریاژ"
    },
    {
        "id": "CANDLE-04",
        "session_name": "سه‌شنبه شب: ضیافت توریست‌های روس",
        "session_name_en": "Tuesday Night: CIS & Russian Diners",
        "date_shamsi": "۲۸ مهر ۱۴۰۵",
        "date_miladi": "20 October 2026",
        "time_slot": "۱۹:۰۰ الی ۲۲:۰۰",
        "open": 4.65,
        "high": 5.00,
        "low": 4.35,
        "close": 4.88,
        "volume_guests": 540,
        "candle_type": "bullish_gain",
        "color": "#2ecc71",
        "primary_flaw": "سد زبانی گارسون‌ها با مسافران روس‌زبان و نیاز به نشان دادن عکس غذا (کامنت Dmitry Smirnov)",
        "high_tech_solution": "مچ‌بندهای سالن‌دار مجهز به چیپست Whisper-v3 و هوش مصنوعی DeepL جهت ترجمه صوتی بلادرنگ گفتار روسی به گوش‌پوش گارسون",
        "high_tech_tag": "High-Tech AI Frontier",
        "high_tech_cost": "$5,800",
        "high_tech_timeline": "۴ هفته سفارش و آموزش",
        "easy_fix_solution": "منوی تصویری لمینت‌شده با خط سیریلیک روسی، شماره‌گذاری عددی غذاها و بارکد QR اختصاصی روی میز",
        "easy_fix_tag": "Easy Quick Fix / 5-Min SOP",
        "easy_fix_cost": "۲۲۰ لیر (لمینت منوی روسی)",
        "easy_fix_timeline": "تحویل در عرض ۲۴ ساعت",
        "skill_code": "SKILL-13",
        "skill_domain": "آداب میزبانی و زبان توریست‌ها"
    },
    {
        "id": "CANDLE-05",
        "session_name": "پنجشنبه شب: موسیقی زنده لانژ کوجاتپه",
        "session_name_en": "Thursday Evening: Kocatepe Live Music",
        "date_shamsi": "۳۰ مهر ۱۴۰۵",
        "date_miladi": "22 October 2026",
        "time_slot": "۲۱:۰۰ الی ۰۰:۳۰",
        "open": 4.75,
        "high": 5.00,
        "low": 4.60,
        "close": 4.95,
        "volume_guests": 680,
        "candle_type": "strong_bullish",
        "color": "#2ecc71",
        "primary_flaw": "محدودیت فضای پارکینگ در تکسیم و عدم آگاهی مسافران از ترانسفر رایگان ۵ دقیقه‌ای به شعبه ۲ (کامنت Caner Demir)",
        "high_tech_solution": "سامانه دیسپچ بین‌شعبه‌ای خودکار با ترکر GPS ناوگان VIP، تخمین بلادرنگ زمان رسیدن به درب ورودی و تخصیص صندلی کلود",
        "high_tech_tag": "High-Tech AI Frontier",
        "high_tech_cost": "$6,400",
        "high_tech_timeline": "۳ هفته برنامه‌نویسی",
        "easy_fix_solution": "ایستادن راهنمای تشریفات با تابلوی شمسه در ورودی استقلال و هدایت مهمانان به ون اختصاصی شمسه با هماهنگی تلفنی واتساپ",
        "easy_fix_tag": "Easy Quick Fix / 5-Min SOP",
        "easy_fix_cost": "رایگان (استفاده از ون موجود شعبه ۲)",
        "easy_fix_timeline": "اجرای آنی",
        "skill_code": "SKILL-30",
        "skill_domain": "مدیریت سرریز و وفادارسازی"
    },
    {
        "id": "CANDLE-06",
        "session_name": "چهارشنبه عصر: غروب بالکن پانورامیک",
        "session_name_en": "Wednesday Sunset: Istiklal Balcony",
        "date_shamsi": "۲۹ مهر ۱۴۰۵",
        "date_miladi": "21 October 2026",
        "time_slot": "۱۷:۳۰ الی ۲۰:۰۰",
        "open": 4.70,
        "high": 5.00,
        "low": 4.50,
        "close": 4.85,
        "volume_guests": 840,
        "candle_type": "bullish_gain",
        "color": "#2ecc71",
        "primary_flaw": "پر بودن میزهای بالکن و تقاضای گردشگران برای رزرو آنلاین میزهای دید خیابان (کامنت احمد کمالی)",
        "high_tech_solution": "ماژول ۳D Digital Twin سالن با قابلیت انتخاب صندلی واقعیت مجازی و پیش‌پرداخت ارزی با Stripe و لیر",
        "high_tech_tag": "High-Tech AI Frontier",
        "high_tech_cost": "$7,200",
        "high_tech_timeline": "۵ هفته مدل‌سازی سه‌بعدی",
        "easy_fix_solution": "افزودن فیلد ساده «انتخاب میز بالکن» در فرم رزرو موجود سایت و پیام خودکار تایید میز در واتساپ رستوران",
        "easy_fix_tag": "Easy Quick Fix / 5-Min SOP",
        "easy_fix_cost": "رایگان (به‌روزرسانی فرم آنلاین)",
        "easy_fix_timeline": "اجرای ۳۰ دقیقه‌ای در وردپرس",
        "skill_code": "SKILL-06",
        "skill_domain": "رزرواسیون و تجربه میهمان"
    }
]

def generate_candlestick_svg(width=900, height=360) -> str:
    """
    تولید نمودار کندل‌استیک شمعی فارکس در فرمت برداری SVG
    """
    svg_parts = [
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:system-ui,sans-serif;" aria-label="Forex Style Sentiment Candlestick Chart">'
    ]
    
    # Background and Grid
    svg_parts.append('<rect width="100%" height="100%" fill="#13171a" rx="6"/>')
    svg_parts.append('<line x1="60" y1="40" x2="860" y2="40" stroke="#252f36" stroke-width="1" stroke-dasharray="4,4"/>')
    svg_parts.append('<line x1="60" y1="100" x2="860" y2="100" stroke="#252f36" stroke-width="1" stroke-dasharray="4,4"/>')
    svg_parts.append('<line x1="60" y1="160" x2="860" y2="160" stroke="#252f36" stroke-width="1" stroke-dasharray="4,4"/>')
    svg_parts.append('<line x1="60" y1="220" x2="860" y2="220" stroke="#252f36" stroke-width="1" stroke-dasharray="4,4"/>')
    svg_parts.append('<line x1="60" y1="280" x2="860" y2="280" stroke="#33414d" stroke-width="1.5"/>')

    # Y-Axis Labels (Rating 4.0 to 5.0)
    svg_parts.append('<text x="50" y="44" fill="#8c8f94" font-size="10" text-anchor="end">5.00 ★</text>')
    svg_parts.append('<text x="50" y="104" fill="#8c8f94" font-size="10" text-anchor="end">4.75 ★</text>')
    svg_parts.append('<text x="50" y="164" fill="#8c8f94" font-size="10" text-anchor="end">4.50 ★</text>')
    svg_parts.append('<text x="50" y="224" fill="#8c8f94" font-size="10" text-anchor="end">4.25 ★</text>')
    svg_parts.append('<text x="50" y="284" fill="#8c8f94" font-size="10" text-anchor="end">4.00 ★</text>')

    # Convert rating (4.0 to 5.0) to Y coordinate (280 to 40)
    # y = 280 - (val - 4.0) * 240
    def val_to_y(val):
        return 280 - (val - 4.0) * 240

    candle_width = 36
    x_positions = [130, 260, 390, 520, 650, 780]

    for i, candle in enumerate(CANDLESTICK_SESSIONS):
        cx = x_positions[i]
        o_y = val_to_y(candle["open"])
        c_y = val_to_y(candle["close"])
        h_y = val_to_y(candle["high"])
        l_y = val_to_y(candle["low"])

        is_bullish = candle["close"] >= candle["open"]
        color = "#2ecc71" if is_bullish else "#e74c3c"
        fill_color = "#2ecc71" if is_bullish else "#e74c3c"

        top_body = min(o_y, c_y)
        body_height = max(abs(c_y - o_y), 4)

        # High/Low Wick
        svg_parts.append(f'<line x1="{cx}" y1="{h_y:.1f}" x2="{cx}" y2="{l_y:.1f}" stroke="{color}" stroke-width="2"/>')
        # Candle Body
        svg_parts.append(f'<rect x="{cx - candle_width/2:.1f}" y="{top_body:.1f}" width="{candle_width}" height="{body_height:.1f}" fill="{fill_color}" stroke="{color}" stroke-width="1.5" rx="2"/>')

        # Volume Bar (height mapped to volume)
        vol_height = (candle["volume_guests"] / 1500) * 45
        svg_parts.append(f'<rect x="{cx - 14}" y="{335 - vol_height:.1f}" width="28" height="{vol_height:.1f}" fill="{color}" opacity="0.35" rx="1"/>')
        svg_parts.append(f'<text x="{cx}" y="348" fill="#a89d8e" font-size="9" text-anchor="middle">{candle["volume_guests"]}</text>')

        # High / Low value annotations
        svg_parts.append(f'<text x="{cx}" y="{h_y - 6:.1f}" fill="#ffd21e" font-size="9" font-weight="bold" text-anchor="middle">{candle["high"]:.2f}</text>')
        svg_parts.append(f'<text x="{cx}" y="{l_y + 12:.1f}" fill="#c3c4c7" font-size="8.5" text-anchor="middle">{candle["low"]:.2f}</text>')

        # Session Label Below
        svg_parts.append(f'<text x="{cx}" y="298" fill="#f0f0f1" font-size="9.5" font-weight="bold" text-anchor="middle">{candle["id"]}</text>')
        svg_parts.append(f'<text x="{cx}" y="310" fill="#d29a5a" font-size="8" text-anchor="middle">{candle["date_shamsi"]}</text>')

    # Legend & Title Header
    svg_parts.append('<text x="65" y="22" fill="#ffd21e" font-size="12" font-weight="bold">📈 تحلیل شمعی فارکس احساسات رستوران شمسه (Sentiment Candlestick Sessions)</text>')
    svg_parts.append('<rect x="680" y="10" width="12" height="12" fill="#2ecc71" rx="2"/><text x="698" y="20" fill="#c3c4c7" font-size="10">صعودی (Bullish Gain)</text>')
    svg_parts.append('<rect x="795" y="10" width="12" height="12" fill="#e74c3c" rx="2"/><text x="813" y="20" fill="#c3c4c7" font-size="10">اصلاح/افت (Dip)</text>')

    svg_parts.append('</svg>')
    return "".join(svg_parts)


def get_candlestick_sessions() -> List[Dict[str, Any]]:
    return CANDLESTICK_SESSIONS


if __name__ == "__main__":
    svg = generate_candlestick_svg()
    out_svg_path = os.path.join(REPO_ROOT, "assets", "img", "sentiment_candlestick_chart.svg")
    with open(out_svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Candlestick chart generated: {out_svg_path} ({len(svg)} bytes)")
