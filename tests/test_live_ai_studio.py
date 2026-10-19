"""Test Suite for Live Interactive AI Studio embedded in index.html."""

import os
import re
import json

def test_live_ai_studio():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(repo_root, "index.html")
    
    assert os.path.exists(index_path), "index.html must exist"
    
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Check Section & IDs
    assert 'id="ai-live-studio"' in html, "Must contain #ai-live-studio section"
    assert 'id="aiTab-interior"' in html, "Must contain #aiTab-interior panel"
    assert 'id="aiTab-menu"' in html, "Must contain #aiTab-menu panel"
    assert 'id="aiTab-sentiment"' in html, "Must contain #aiTab-sentiment panel"
    assert 'id="aiTab-space"' in html, "Must contain #aiTab-space panel"
    
    # 2. Check Interactive JS Functions
    assert "switchAiTab" in html, "switchAiTab function must be present"
    assert "selectAiInterior" in html, "selectAiInterior function must be present"
    assert "selectAiDish" in html, "selectAiDish function must be present"
    assert "selectAiReview" in html, "selectAiReview function must be present"
    assert "selectAiSpace" in html, "selectAiSpace function must be present"
    assert "copyGeneratedAiReply" in html, "copyGeneratedAiReply function must be present"
    
    # 3. Check All referenced images exist on disk
    img_matches = re.findall(r'assets/img/[a-zA-Z0-9_\-\.]+\.jpg', html)
    unique_imgs = set(img_matches)
    for img_rel in unique_imgs:
        img_full = os.path.join(repo_root, img_rel)
        assert os.path.isfile(img_full), f"Referenced image {img_rel} must exist on disk"
        print(f"PASS verified image asset {img_rel}")

    # 4. Check Data Keys in JS objects
    expected_interior_keys = ["copper-walnut", "isfahan-azure", "ottoman-neoclassic", "meetup-community", "cyber-speakeasy"]
    for k in expected_interior_keys:
        assert f'"{k}":' in html, f"Interior key {k} must exist in JS data"
        print(f"PASS interior preset {k} present")

    expected_menu_keys = ["koobideh", "hero-platter", "ghormeh", "zereshk", "jujeh"]
    for k in expected_menu_keys:
        assert f'"{k}":' in html, f"Menu key {k} must exist in JS data"
        print(f"PASS menu preset {k} present")

    expected_rev_keys = ["review-fa", "review-tr", "review-en", "review-triage"]
    for k in expected_rev_keys:
        assert f'"{k}":' in html, f"Review key {k} must exist in JS data"
        print(f"PASS review preset {k} present")

    expected_space_keys = ["mafia", "poetry", "cowork", "corporate"]
    for k in expected_space_keys:
        assert f'"{k}":' in html, f"Space key {k} must exist in JS data"
        print(f"PASS space preset {k} present")

    # 5. Check Navigation and CTA Linkage
    assert 'href="#ai-live-studio"' in html, "Navigation/CTA link to #ai-live-studio must exist"
    print("PASS navigation and hero CTA contain links to #ai-live-studio")

    print("\n===== ALL LIVE AI STUDIO CHECKS PASSED (0 FAILURES) =====")

if __name__ == "__main__":
    test_live_ai_studio()
