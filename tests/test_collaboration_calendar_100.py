#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the 100-Lead International Collaboration Calendar & Database:
  10 Domains x 10 Countries = 100 Concrete Leads
"""

import os
import json
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALENDAR_PATH = os.path.join(REPO_ROOT, "automation", "collaboration_calendar_100.json")
INTEL_HTML = os.path.join(REPO_ROOT, "intelligence.html")

def test_collaboration_calendar_integrity():
    assert os.path.exists(CALENDAR_PATH), "Calendar JSON file must exist"
    with open(CALENDAR_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data["total_leads"] == 100, f"Must have exactly 100 leads, got {data['total_leads']}"
    assert len(data["leads"]) == 100, f"Leads array length must be 100, got {len(data['leads'])}"
    assert data["total_countries"] == 10
    assert data["total_domains"] == 10

    # Verify all 10 required countries are present
    expected_countries = {"TR", "IR", "DE", "SE", "AE", "US", "CA", "GB", "FR", "NL"}
    assert set(data["countries"].keys()) == expected_countries

    # Verify all 10 required domains are present
    expected_domains = {
        "brands", "creators", "universities", "government", "specialists",
        "medical", "crowdfunding", "accelerators", "ngos", "events"
    }
    assert set(data["domains"].keys()) == expected_domains

    # Verify each lead has an operational pain and v2 hook
    for lead in data["leads"]:
        assert lead["country"] in expected_countries
        assert lead["domain"] in expected_domains
        assert len(lead["pain"]) > 10
        assert len(lead["v2_hook"]) > 10
        assert lead["website"] != ""

def test_intelligence_html_calendar_module15():
    assert os.path.exists(INTEL_HTML), "intelligence.html must exist"
    with open(INTEL_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    assert "mod-outreach-v2" in html
    assert "سالنامه جامع و بانک ۱۰۰ لید بین‌المللی" in html
    assert "calCountryFilter" in html
    assert "calDomainFilter" in html
    assert "LEAD-001" in html
    assert "LEAD-100" in html
    assert "Hasir Restaurant Group" in html
    assert "Max Burgers AB" in html
    assert "Refika'nın Mutfağı" in html
    assert "Fonbulucu" in html
    assert "Acıbadem Healthcare Group" in html
