#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Outreach v2 Engine, 30 Selected Skills, Rubric Scoring, and Anti-Spam Architecture.
"""

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import pytest
from automation.outreach_v2_engine import (
    hash_ab_variant,
    is_suppressed,
    add_suppression,
    classify_reply_intent,
    generate_v2_email,
    run_rubric_audit,
    SUPPRESSION_FILE
)

def test_outreach_v2_email_length_and_headers():
    email_data = generate_v2_email("رستوران شمسه", "shamsemedia1@gmail.com", stage=1)
    # Word count must be in golden range: 75 to 125 words
    assert 75 <= email_data["word_count"] <= 125, f"Email length should be 75-125 words, got {email_data['word_count']}"
    assert "List-Unsubscribe" in email_data["headers"]
    assert "List-Unsubscribe-Post" in email_data["headers"]
    assert email_data["headers"]["List-Unsubscribe-Post"] == "List-Unsubscribe=One-Click"
    assert email_data["variant"] in ["A", "B", "C"]

def test_outreach_v2_three_stages():
    # Test Stage 1 (Day 0)
    st1 = generate_v2_email("رستوران شمسه", "test@example.com", stage=1)
    assert st1["stage"] == 1
    assert "پادکست" in st1["body"]

    # Test Stage 2 (Day 5)
    st2 = generate_v2_email("رستوران شمسه", "test@example.com", stage=2)
    assert st2["stage"] == 2
    assert "پیگیری" in st2["subject"]

    # Test Stage 3 (Day 12 Breakup)
    st3 = generate_v2_email("رستوران شمسه", "test@example.com", stage=3)
    assert st3["stage"] == 3
    assert "آخرین پیام" in st3["subject"]
    assert "بایگانی" in st3["body"]

def test_suppression_and_reply_classification():
    import uuid
    test_email = f"optout-{uuid.uuid4().hex[:8]}@shamse-test.com"
    assert not is_suppressed(test_email)
    add_suppression(test_email, reason="unsubscribe")
    assert is_suppressed(test_email)

    # Test reply triage
    assert classify_reply_intent("لطفا من رو حذف کنید و دیگه پیام ندید") == "unsubscribe"
    assert classify_reply_intent("نه متشکرم تمایلی نداریم") == "no"
    assert classify_reply_intent("الان سرمون شلوغه ماه بعد تماس بگیرید") == "later"
    assert classify_reply_intent("سلام عالیه، سه‌شنبه ساعت ۱۰ تماس بگیرید صحبت کنیم") == "interested"

def test_rubric_score_progression():
    audit = run_rubric_audit()
    assert audit["total_max"] == 140
    assert audit["v1_score"] == 81
    assert audit["v2_score"] >= 117
    assert len(audit["axes"]) == 7
