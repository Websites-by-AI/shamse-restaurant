#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for the Somayyeh Restaurant website.

Input : src/page.html      (source template with __IMG_name__ placeholders)
Output: index.html         (normal site — images loaded from assets/img/, ready for GitHub Pages)
        preview.html       (single self-contained file — each photo embedded ONCE as base64
                            and shared through a small window.IMG map, so the file stays light)

Usage:  python3 build.py
"""
import base64, io, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src", "page.html")
IMGDIR = os.path.join(ROOT, "assets", "img")

PREVIEW_MAX_W = 900      # resize width of photos embedded into preview.html
PREVIEW_QUALITY = 62     # JPEG quality for the embedded copies
TINY_GIF = ("data:image/gif;base64,"
            "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7")

PLACEHOLDER = re.compile(r"__IMG_([a-z0-9\-]+)__")


def load_source() -> str:
    with open(SRC, encoding="utf-8") as fh:
        return fh.read()


IMGREF = re.compile(r"IMGREF\('([a-z0-9\-]+)'\)")


def build_index(src: str) -> str:
    """Normal build: point every placeholder at a real relative file path."""
    src = PLACEHOLDER.sub(lambda m: "assets/img/%s.jpg" % m.group(1), src)
    return IMGREF.sub(lambda m: "'assets/img/%s.jpg'" % m.group(1), src)


def build_preview_js(src: str) -> str:
    """Single-file build: JS object literals `src:'__IMG_x__'` / `IMGREF('x')` -> shared map."""
    src = re.sub(
        r":'__IMG_([a-z0-9\-]+)__'",
        lambda m: ":IMG['%s']" % m.group(1),
        src,
    )
    return IMGREF.sub(lambda m: "IMG['%s']" % m.group(1), src)


def build_preview(src: str) -> str:
    """Single-file build: embed each photo once, share it via window.IMG."""
    from PIL import Image

    cache: dict[str, str] = {}

    def data_uri(name: str) -> str:
        if name in cache:
            return cache[name]
        path = os.path.join(IMGDIR, name + ".jpg")
        if not os.path.exists(path):
            sys.exit("missing image: %s" % path)
        im = Image.open(path).convert("RGB")
        if im.width > PREVIEW_MAX_W:
            h = round(im.height * PREVIEW_MAX_W / im.width)
            im = im.resize((PREVIEW_MAX_W, h), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=PREVIEW_QUALITY, optimize=True, progressive=True)
        uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("ascii")
        cache[name] = uri
        return uri

    # 1) <img src="__IMG_x__">  /  <a href="__IMG_x__">  ->  tiny placeholder + data-img key
    src = re.sub(
        r'(src|href)="__IMG_([a-z0-9\-]+)__"',
        lambda m: '%s="%s" data-img="%s"' % (m.group(1), TINY_GIF, m.group(2)),
        src,
    )

    # 2) inline CSS background:  style="--hero:url('__IMG_x__')"  ->  keep css var + data-img-bg
    src = re.sub(
        r"style=\"--([a-z\-]+):url\('__IMG_([a-z0-9\-]+)__'\)\"",
        lambda m: 'style="--%s:url(\'%s\')" data-img-bg="%s" data-prop="--%s"'
        % (m.group(1), TINY_GIF, m.group(2), m.group(1)),
        src,
    )

    # 3) JS object literals:  src:'__IMG_x__'  ->  src:IMG['x']
    src = build_preview_js(src)

    if PLACEHOLDER.search(src):
        left = set(PLACEHOLDER.findall(src))
        sys.exit("unhandled image placeholders: %s" % ", ".join(sorted(left)))

    # 4) embed the unique image map once, right before the inline-image bootstrap
    names = sorted(set(re.findall(r'data-img(?:-bg)?="([a-z0-9\-]+)"', src)) |
                   set(re.findall(r"IMGREF\('([a-z0-9\-]+)'\)", src)))
    if not names:
        sys.exit("no image keys found — template layout changed?")
    img_map = ",\n".join('"%s":"%s"' % (n, data_uri(n)) for n in names)
    inject = '<script id="preview-img-map">window.IMG={%s};</script>\n' % img_map
    marker = "<script>\n(function(){\n  if(!window.IMG) return;"
    if marker not in src:
        sys.exit("bootstrap script marker not found")
    src = src.replace(marker, inject + marker, 1)
    return src


def main():
    src = load_source()
    index = build_index(src)
    preview = build_preview(src)

    for name, html in (("index.html", index), ("preview.html", preview)):
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(html)
        print("%-14s %7.1f KB" % (name, len(html.encode("utf-8")) / 1024))


if __name__ == "__main__":
    main()
