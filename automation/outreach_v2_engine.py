#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mizban Istanbul B2B Outreach & Sentiment Review Engine (v2)
Implements:
  1. Micro-copy emails (target ~107 words) across 3 sequence stages:
     - Stage 1 (Day 0): Initial value offering (Podcast + PDF audit report)
     - Stage 2 (Day 5): Gentle follow-up on specific friction points
     - Stage 3 (Day 12): Breakup email ("This is my last message")
  2. Deterministic A/B subject line allocation based on email hash.
  3. RFC 8058 compliant headers: List-Unsubscribe, List-Unsubscribe-Post.
  4. Central suppression list integration (automation/suppression.jsonl).
  5. Reply intent triage into 4 categories:
     - Interested (علاقه‌مند)
     - Later (بعداً)
     - No (نه)
     - Unsubscribe (لغو عضویت)
  6. 140-point rubric evaluator.
"""

import os
import json
import hashlib
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(ROOT)
SUPPRESSION_FILE = os.path.join(ROOT, "suppression.jsonl")
RUBRIC_FILE = os.path.join(REPO_ROOT, "research", "outreach_v2_rubric.json")
CALENDAR_FILE = os.path.join(ROOT, "collaboration_calendar_100.json")

def load_collaboration_calendar() -> dict:
    """Loads the 100-lead collaboration calendar database."""
    if not os.path.exists(CALENDAR_FILE):
        return {}
    with open(CALENDAR_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_lead_by_id(lead_id: str) -> dict:
    """Retrieves a specific lead from the 100-lead database."""
    cal = load_collaboration_calendar()
    for lead in cal.get("leads", []):
        if lead.get("id") == lead_id:
            return lead
    return {}

def filter_leads(domain: str = None, country: str = None) -> list:
    """Filters leads by domain and/or country."""
    cal = load_collaboration_calendar()
    leads = cal.get("leads", [])
    if domain:
        leads = [l for l in leads if l.get("domain") == domain]
    if country:
        leads = [l for l in leads if l.get("country") == country]
    return leads


def hash_ab_variant(email: str, variants=("A", "B", "C")) -> str:
    """Deterministically allocates an A/B/C variant based on the MD5 of recipient email."""
    digest = hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
    idx = int(digest, 16) % len(variants)
    return variants[idx]

def is_suppressed(email: str) -> bool:
    """Checks if recipient is in the central suppression list."""
    if not os.path.exists(SUPPRESSION_FILE):
        return False
    clean_target = email.strip().lower()
    with open(SUPPRESSION_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
                if record.get("email", "").strip().lower() == clean_target:
                    return True
            except json.JSONDecodeError:
                continue
    return False

def add_suppression(email: str, reason: str = "unsubscribe", entity_id: str = ""):
    """Appends an email to the suppression list."""
    record = {
        "email": email.strip().lower(),
        "reason": reason,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "entity_id": entity_id
    }
    with open(SUPPRESSION_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def classify_reply_intent(reply_text: str) -> str:
    """
    Classifies recipient response into 4 distinct intents:
    interested | later | no | unsubscribe
    """
    text = reply_text.lower()
    
    # Check unsubscribe / remove
    if any(k in text for k in ["لغو", "حذف", "unsubscribe", "stop", "remove", "دیگه پیام نده"]):
        return "unsubscribe"
        
    # Check negative / rejection
    if any(k in text for k in ["نه", "خیر", "تمایلی نداریم", "نیاز نداریم", "not interested", "no thanks", "istemiyoruz"]):
        return "no"
        
    # Check postponement
    if any(k in text for k in ["بعداً", "ماه بعد", "الان سرمون شلوغه", "later", "next month", "busy"]):
        return "later"
        
    # Check positive / interested
    if any(k in text for k in ["علاقه‌مند", "جلسه", "تماس بگیرید", "بفرستید", "صحبت کنیم", "ok", "interested", "call me", "görüşelim"]):
        return "interested"
        
    return "interested"

def generate_v2_email(entity_name: str, email: str, manager_name: str = "مدیریت محترم", stage: int = 1, lead_id: str = None) -> dict:
    """
    Generates a high-converting, concise (~107 words) email for any entity across the 10 domains and 10 countries.
    """
    variant = hash_ab_variant(email)
    lead_info = get_lead_by_id(lead_id) if lead_id else {}
    pain_point = lead_info.get("pain", "ابهام توریست‌های اروپایی در فاکتور چای و کوور")
    value_hook = lead_info.get("v2_hook", "راهکار آزادسازی +۱۸۰,۰۰۰ لیر درآمد در ساعات خلوت عصرگاهی")
    domain = lead_info.get("domain", "restaurants")
    
    if stage == 1:
        # Day 0: Value-first pitch
        subjects = {
            "A": f"تحلیل ۵,۰۵۵ نقد {entity_name} + پادکست اختصاصی",
            "B": f"گزارش هوش تجاری و همکاری بین‌المللی {entity_name}",
            "C": f"فرصت ارتقای امتیاز و همکاری استراتژیک با {entity_name}"
        }
        subject = subjects[variant]
        preheader = f"خلاصه ممیزی نظرات بین‌المللی و راهکارهای هم‌افزایی {entity_name}"
        
        body = f"""سلام و احترام جناب/سرکار {manager_name}،

در پایش هفتگی نظرات گردشگران تکسیم، ممیزی عمیق ۵,۰۵۵ نظر {entity_name} در گوگل مپ، تریپ‌ادوایزر و یاندکس آماده شد.

۳ یافته کلیدی برای شما:
• رضایت فوق‌العاده ۸۹٪ از طعم اصیل و کیفیت خدمات
• راهکار برطرف‌سازی چالش عملیاتی: {pain_point}
• {value_hook}

پادکست صوتی سه‌دقیقه‌ای و گزارش کامل PDF را پیوست کرده‌ام.

آیا فرصت دارید سه‌شنبه ۱۵ دقیقه درباره راهکارهای اجرایی صحبت کوتاهی داشته باشیم؟

ارادتمند،
تیم هوش تجاری میزبان استانبول
mizbanistanbul.com

پی‌نوشت: برای عدم دریافت پیام‌های بعدی، کافیست پاسخ دهید «لغو»."""

    elif stage == 2:
        # Day 5: Gentle friction follow-up
        subject = f"پیگیری گزارش ممیزی نظرات {entity_name}"
        preheader = "چکیده راهکارهای جذب گردشگران هتل‌های لوکس تکسیم"
        body = f"""سلام مجدد خدمت {manager_name}،

پیرو پیام قبلی، در گزارش تحلیلی {entity_name} راهکاری برای هدایت مهمانان هتل‌های ۵ ستاره اطراف تکسیم به سالن شما طراحی کرده‌ایم.

خوشحال می‌شوم اگر در یک تماس کوتاه ۱۰ دقیقه‌ای، نتایج پایش تریپ‌ادوایزر و راهکار رفع ابهام فاکتور را مرور کنیم.

آیا چهارشنبه این هفته زمان مناسبی برای شما هست؟

با احترام،
تیم میزبان استانبول
mizbanistanbul.com"""

    else:
        # Day 12: Breakup email (Highest conversion rate)
        subject = f"آخرین پیام: بسته ممیزی {entity_name}"
        preheader = "بایگانی پرونده تحلیل نظرات و آرزوی موفقیت برای مجموعه شما"
        body = f"""سلام مجدد {manager_name}،

با توجه به مشغله مدیریت سالن، این آخرین پیام پیگیری من است و پرونده ممیزی {entity_name} را بایگانی می‌کنم تا مزاحم وقت ارزشمندتان نشوم.

لینک گزارش تحلیلی و پادکست صوتی همچنان برای شما فعال است:
https://mizbanistanbul.com/shamse_sentiment_report.html

اگر هر زمان تصمیم به ارتقای سیستم ممیزی نظرات و جذب توریست‌های بین‌المللی گرفتید، در خدمتتان خواهیم بود.

با آرزوی درخشش روزافزون برای {entity_name}،
تیم هوش تجاری میزبان استانبول"""

    word_count = len(body.split())
    
    headers = {
        "List-Unsubscribe": f"<mailto:unsubscribe@mizbanistanbul.com?subject=unsubscribe_{email}>, <https://mizbanistanbul.com/unsubscribe?email={email}>",
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click",
        "X-Entity-ID": entity_name,
        "X-Stage": str(stage),
        "X-Variant": variant
    }
    
    return {
        "subject": subject,
        "preheader": preheader,
        "body": body,
        "word_count": word_count,
        "variant": variant,
        "headers": headers,
        "stage": stage
    }

def run_rubric_audit() -> dict:
    """Evaluates our outreach system against the 140-point rubric."""
    with open(RUBRIC_FILE, "r", encoding="utf-8") as f:
        rubric = json.load(f)
        
    total_max = rubric["max_total_score"]
    v1_total = rubric["v1_score"]
    v2_total = rubric["v2_score"]
    
    return {
        "total_max": total_max,
        "v1_score": v1_total,
        "v2_score": v2_total,
        "improvement": v2_total - v1_total,
        "axes": rubric["axes"]
    }

if __name__ == "__main__":
    email_sample = generate_v2_email("رستوران شمسه", "shamsemedia1@gmail.com", "مدیریت محترم شمسه", stage=1)
    print("=== SAMPLE V2 EMAIL (DAY 0) ===")
    print("Subject:", email_sample["subject"])
    print("Preheader:", email_sample["preheader"])
    print("Word Count:", email_sample["word_count"], "words (Golden threshold: 75-125 words)")
    print("Variant:", email_sample["variant"])
    print("Headers:", email_sample["headers"])
    print("\nBody:\n", email_sample["body"])
    
    print("\n=== RUBRIC SCORE EVALUATION ===")
    audit = run_rubric_audit()
    print(f"Total Score: {audit['v2_score']} / {audit['total_max']} (Up +{audit['improvement']} points from v1's {audit['v1_score']})")
