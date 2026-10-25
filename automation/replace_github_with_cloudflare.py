#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Replace all occurrences of https://websites-by-ai.github.io/shamse-restaurant
with https://shamse-restaurant.pages.dev across all repository files.
"""

import os

OLD_URL = "https://websites-by-ai.github.io/shamse-restaurant"
NEW_URL = "https://shamse-restaurant.pages.dev"

FILES = [
    "index.html",
    "restaurant_portal.html",
    "admin_panel.html",
    "shamse_sentiment_report.html",
    "intelligence.html",
    "marketing.html",
    "events.html",
    "restaurants.html",
    "preview.html",
    "preview-marketing.html",
    "preview-events.html",
    "README.md",
    "DEPLOY.md",
    "automation/patch_admin_panel_credentials.py",
    "automation/patch_index_credentials_and_learning_infographic.py",
    "automation/patch_all_sections_links.py"
]

def main():
    count = 0
    for rel_path in FILES:
        if not os.path.exists(rel_path):
            continue
        with open(rel_path, "r", encoding="utf-8") as f:
            content = f.read()
        if OLD_URL in content:
            updated = content.replace(OLD_URL, NEW_URL)
            with open(rel_path, "w", encoding="utf-8") as f:
                f.write(updated)
            print(f"Replaced in {rel_path}")
            count += 1

    print(f"Replacement complete! Updated {count} files.")

if __name__ == "__main__":
    main()
