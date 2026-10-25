#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

ANALYZER_FILE = "automation/shamse_sentiment_analyzer.py"

with open("automation/patch_shamse_sentiment_report_skills_and_links.py", "r", encoding="utf-8") as f:
    patch_code = f.read()

m = re.search(r'ENRICHED_SECTION = """([\s\S]*?)"""\n\n# Regex replacement', patch_code)
if not m:
    raise ValueError("Could not extract ENRICHED_SECTION")

raw_enriched = m.group(1)
# Escape braces for Python f-string
fstring_enriched = raw_enriched.replace("{", "{{").replace("}", "}}")

# First reset shamse_sentiment_analyzer.py to clean state
import subprocess
subprocess.run(["git", "checkout", ANALYZER_FILE], check=True)

with open(ANALYZER_FILE, "r", encoding="utf-8") as f:
    content = f.read()

target_pattern = r'      <!-- SECTION: VITAL FLAWS & 100 SKILLS CORRECTIVE PRESCRIPTIONS -->[\s\S]*?(?=      <!-- SECTION: 4-LANGUAGE AI CUSTOMER REVIEW RESPONDER -->)'

if re.search(target_pattern, content):
    patched = re.sub(target_pattern, fstring_enriched + "\n", content, count=1)
    with open(ANALYZER_FILE, "w", encoding="utf-8") as f:
        f.write(patched)
    print("Successfully patched automation/shamse_sentiment_analyzer.py with escaped braces!")
else:
    print("Target pattern not found in shamse_sentiment_analyzer.py!")
