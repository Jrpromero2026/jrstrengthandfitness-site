"""Share cards: one 1200x630 image per article, used when the link is shared (LinkedIn, Facebook, texts).

Design C (chosen Oct 2026): black ground, red "Notes from the Floor" tag, the headline in Jost 800
uppercase, logo and byline at the bottom, and a photo on the right that fades into the black.
The photo is the article's own `image` when it has one, otherwise JR's portrait.

Cards are written to public/assets/share/<slug>.jpg on every build. Pillow's output is
deterministic, so unchanged articles produce byte-identical files and no git diff.
"""
import os

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")
FONTS = os.path.join(PUBLIC, "assets", "fonts")
OUT_DIR = os.path.join(PUBLIC, "assets", "share")
PORTRAIT = os.path.join(PUBLIC, "assets", "photos", "jr-portrait.webp")
LOGO = os.path.join(PUBLIC, "assets", "jr-logo.png")

W, H = 1200, 630
BG = (10, 10, 10)
RED = (225, 6, 18)          # site red (--red in styles.css)
WHITE = (246, 246, 246)
BYLINE_GREY = (216, 216, 216)
RULE_GREY = (85, 85, 85)
LEFT = 72
TAG_TEXT = "NOTES FROM THE FLOOR"
BYLINE = "JR ROMERO, CSCS"
PHOTO_X, PHOTO_W = 640, 560


def _font(weight, size):
    return ImageFont.truetype(os.path.join(FONTS, f"jost-latin-{weight}-normal.woff2"), size)


def _spaced(draw, xy, text, font, fill, tracking):
    """Draw text with letter-spacing (tracking in em)."""
    x, y = xy
    gap = font.size * tracking
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + gap
    return x - gap


def _spaced_width(text, font, tracking):
    return sum(font.getlength(c) for c in text) + font.size * tracking * (len(text) - 1)


def _cover(img, w, h, fx=0.5, fy=0.16):
    """Crop-and-scale like CSS object-fit: cover with an object-position of fx, fy."""
    s = max(w / img.width, h / img.height)
    img = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    left = round((img.width - w) * fx)
    top = round((img.height - h) * fy)
    return img.crop((left, top, left + w, top + h))


def _wrap(words, font, width):
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if cur and font.getlength(t) > width:
            lines.append(cur)
            cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    return lines


def _fit_headline(title, max_w, max_h):
    """Largest size (64 down to 40) whose wrapped headline fits; then balance the lines."""
    words = title.upper().split()
    for size in range(64, 39, -2):
        font = _font(800, size)
        lh = round(size * 1.02)
        lines = _wrap(words, font, max_w)
        if len(lines) <= 5 and len(lines) * lh <= max_h and all(font.getlength(l) <= max_w for l in lines):
            # balance: narrow the measure as far as possible without adding a line
            lo, hi = max_w * 0.5, max_w
            while hi - lo > 4:
                mid = (lo + hi) / 2
                if len(_wrap(words, font, mid)) == len(lines):
                    hi = mid
                else:
                    lo = mid
            return font, _wrap(words, font, hi), lh
    font = _font(800, 40)
    return font, _wrap(words, font, max_w)[:5], 41


def render(title, photo_path=None, photo_focus=(0.5, 0.16)):
    card = Image.new("RGB", (W, H), BG)

    # photo on the right, fading into the black ground
    src = Image.open(photo_path or PORTRAIT).convert("RGB")
    card.paste(_cover(src, PHOTO_W, H, *photo_focus), (PHOTO_X, 0))
    shade = Image.new("L", (W, 1))
    stops = [(0, 255), (624, 255), (792, 140), (1008, 0), (W, 0)]
    for x in range(W):
        for (x0, a0), (x1, a1) in zip(stops, stops[1:]):
            if x0 <= x <= x1:
                shade.putpixel((x, 0), round(a0 + (a1 - a0) * (x - x0) / max(1, x1 - x0)))
                break
    card.paste(Image.new("RGB", (W, H), BG), (0, 0), shade.resize((W, H)))

    d = ImageDraw.Draw(card)

    # red tag
    tf = _font(700, 19)
    tw = _spaced_width(TAG_TEXT, tf, 0.18)
    top = 60
    d.rectangle((LEFT, top, LEFT + 32 + round(tw), top + 44), fill=RED)
    _spaced(d, (LEFT + 16, top + 8), TAG_TEXT, tf, (255, 255, 255), 0.18)

    # logo and byline
    logo = Image.open(LOGO).convert("RGBA")
    lw = 150
    logo = logo.resize((lw, round(logo.height * lw / logo.width)), Image.LANCZOS)
    foot_mid = H - 60 - 26
    card.paste(logo, (LEFT, foot_mid - logo.height // 2), logo)
    bx = LEFT + lw + 22
    d.rectangle((bx, foot_mid - 17, bx + 1, foot_mid + 17), fill=RULE_GREY)
    bf = _font(600, 19)
    _spaced(d, (bx + 24, foot_mid - 14), BYLINE, bf, BYLINE_GREY, 0.12)

    # headline
    h_top = top + 44 + 26
    h_bottom = foot_mid - 26 - 34
    font, lines, lh = _fit_headline(title, 700, h_bottom - h_top)
    y = h_top
    for line in lines:
        d.text((LEFT, y), line, font=font, fill=WHITE)
        y += lh
    return card


def build_all(posts):
    os.makedirs(OUT_DIR, exist_ok=True)
    keep = set()
    for p in posts:
        photo = os.path.join(PUBLIC, p["image"].lstrip("/")) if p.get("image") else None
        focus = (0.5, 0.4) if photo else (0.5, 0.16)
        name = p["slug"] + ".jpg"
        render(p["title"], photo, focus).save(os.path.join(OUT_DIR, name), "JPEG", quality=86, optimize=True)
        keep.add(name)
    for f in os.listdir(OUT_DIR):  # drop cards for deleted articles
        if f.endswith(".jpg") and f not in keep:
            os.remove(os.path.join(OUT_DIR, f))


def url_for(slug):
    return f"/assets/share/{slug}.jpg"
