#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compiles 10 HD video slides and the executive audio podcast into an MP4 video:
- assets/video/shamse_intelligence_video.mp4
- shamse_intelligence_video.mp4 (root copy for direct link/download)
"""

import os
import subprocess

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES_DIR = os.path.join(REPO_ROOT, "assets", "video", "slides")
AUDIO_PATH = os.path.join(REPO_ROOT, "assets", "audio", "shamse_intelligence_podcast.mp3")
OUT_VIDEO_ASSET = os.path.join(REPO_ROOT, "assets", "video", "shamse_intelligence_video.mp4")
OUT_VIDEO_ROOT = os.path.join(REPO_ROOT, "shamse_intelligence_video.mp4")

os.makedirs(os.path.dirname(OUT_VIDEO_ASSET), exist_ok=True)

# Duration per slide: ~6.56 seconds so 10 slides = 65.6 seconds (matching audio)
DURATION_PER_SLIDE = 6.566

# Create concat demuxer file
concat_txt = os.path.join(SLIDES_DIR, "concat.txt")
with open(concat_txt, "w") as f:
    for i in range(1, 11):
        slide_file = os.path.abspath(os.path.join(SLIDES_DIR, f"slide_{i:02d}.png"))
        f.write(f"file '{slide_file}'\n")
        f.write(f"duration {DURATION_PER_SLIDE:.3f}\n")
    # Concat demuxer needs last file repeated
    last_slide = os.path.abspath(os.path.join(SLIDES_DIR, "slide_10.png"))
    f.write(f"file '{last_slide}'\n")

cmd = [
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0", "-i", concat_txt,
    "-i", AUDIO_PATH,
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "25",
    "-c:a", "aac", "-b:a", "192k",
    "-shortest",
    OUT_VIDEO_ASSET
]

print("Running ffmpeg command:", " ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True)

if res.returncode != 0:
    print("FFmpeg error:", res.stderr)
    raise RuntimeError(f"FFmpeg failed with code {res.returncode}")

# Copy to root
import shutil
shutil.copyfile(OUT_VIDEO_ASSET, OUT_VIDEO_ROOT)

size = os.path.getsize(OUT_VIDEO_ASSET)
print(f"Video compiled successfully: {OUT_VIDEO_ASSET} ({size:,} bytes)")
print(f"Root video created: {OUT_VIDEO_ROOT} ({os.path.getsize(OUT_VIDEO_ROOT):,} bytes)")
