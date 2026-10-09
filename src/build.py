"""Builds the static site into ../public. Run: python3 src/build.py"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from layout import page, SITE  # noqa: E402
import pages as P  # noqa: E402
import projects as PR  # noqa: E402
from PIL import Image, ImageDraw, ImageFilter  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")
ASSETS = os.path.join(OUT, "assets")

PAGES = [
    dict(path="/", file="index.html", active="", schema=True,
         title="JR Strength & Fitness | Coach, Builder · Corvallis, Oregon",
         description="JR Prieto-Romero, CSCS: Director of Training at Timberhill Athletic Club and Director of Personal Training and Performance at G3 Sports & Fitness. Coaching in Corvallis and online, plus tools for coaches.",
         body=P.HOME),
    dict(path="/train", file="train.html", active="train",
         title="Train with JR | In-Person in Corvallis & Online Coaching",
         description="Train with JR Prieto-Romero, CSCS. Local clients start with a free consult at Timberhill Athletic Club or G3 Sports & Fitness in Corvallis; anywhere else, apply for online coaching.",
         body=P.TRAIN),
    dict(path="/consult", file="consult.html", active="train",
         title="Book a Free Consult | Timberhill or G3 | JR Strength & Fitness",
         description="Local to Corvallis? Start with a free consult at Timberhill Athletic Club or G3 Sports & Fitness. Anywhere else, apply for online coaching.",
         body=P.CONSULT_PAGE),
    dict(path="/online-training", file="online-training.html", active="train",
         title="Online Coaching | Training & Nutrition | JR Strength & Fitness",
         description="Individualized online training and nutrition coaching from JR Prieto-Romero, CSCS. Essentials, Core and Premium packages from $129 a month.",
         body=P.ONLINE),
    dict(path="/apply", file="apply.html", active="train",
         title="Apply for Online Coaching | JR Strength & Fitness",
         description="Apply for online training and nutrition coaching with JR Prieto-Romero, CSCS. Applications go straight to JR.",
         body=P.APPLY, script=P.APPLY_SCRIPT + P.FORM_SCRIPT, closing=False),
    dict(path="/about", file="about.html", active="about",
         title="About JR Prieto-Romero, CSCS | JR Strength & Fitness",
         description="Director of Training at Timberhill Athletic Club, Director of Personal Training and Performance at G3 Sports & Fitness, Oregon State Exercise & Sport Science graduate, ~20,000 coaching hours.",
         body=P.ABOUT),
    dict(path="/writing", file="writing.html", active="",
         title="Writing | JR Strength & Fitness",
         description="JR Prieto-Romero writes about coaching systems, consultations and building in public.",
         body=P.WRITING),
    dict(path="/privacy-policy", file="privacy-policy.html", active="",
         title="Privacy Policy | JR Strength & Fitness",
         description="How JR Strength and Fitness LLC collects and uses information on jrstrengthandfitness.com.",
         body=P.PRIVACY),
    dict(path="/terms-of-service", file="terms-of-service.html", active="",
         title="Terms of Service | JR Strength & Fitness",
         description="Terms for using jrstrengthandfitness.com and JR Strength and Fitness coaching services.",
         body=P.TERMS),
    dict(path="/refund-policy", file="refund-policy.html", active="",
         title="Refund Policy | JR Strength & Fitness",
         description="Cancellation and refund terms for JR Strength and Fitness online coaching packages.",
         body=P.REFUND),
dict(path="/projects", file="projects.html", active="projects",
         title="Projects | JR Strength & Fitness",
         description="What JR Prieto-Romero is building: The Trainer’s Coach Vault, Built For Her™, TRAINCND and The Credential Standard.",
         body=PR.projects_index()),
] + [
    dict(path=f"/projects/{p['slug']}", file=f"projects/{p['slug']}.html", active="projects",
         title=f"{p['name']} | Projects | JR Strength & Fitness".replace("&amp;", "&"),
         description=(p['tagline'] + " " + p['card']).replace("&amp;", "&"),
         body=PR.project_page(p), script=P.FORM_SCRIPT if p.get("waitlist") else "")
    for p in PR.PROJECTS
] + [
    dict(path="/404", file="404.html", active="", sitemap=False,
         title="Page not found | JR Strength & Fitness",
         description="That page moved or never existed.",
         body=P.NOT_FOUND),
]

# Old Squarespace URLs -> new pages (301)
REDIRECTS = [
    ("/home", "/"), ("/home-1", "/"),
    ("/online-coaching", "/online-training"), ("/onlinetraining-1", "/online-training"), ("/programs", "/online-training"),
    ("/train-with-me", "/consult"), ("/contact", "/consult"), ("/waiver", "/terms-of-service"),
    ("/mentorship", "/"), ("/trainer-mentorship", "/"), ("/mentorship-program-application", "/"),
    ("/resources", "/"), ("/new-gallery", "/"),
    ("/blog", "/writing"), ("/blog-1", "/writing"), ("/blog/:path*", "/writing"),
    ("/store", "/"), ("/store/:path*", "/"), ("/cart", "/"),
]


def build_pages():
    for spec in PAGES:
        html = page(path=spec["path"], title=spec["title"].replace("&", "&amp;"),
                    description=spec["description"].replace("&", "&amp;"), body=spec["body"],
                    active=spec["active"], schema=spec.get("schema", False),
                    script=spec.get("script", ""), closing=spec.get("closing", True))
        os.makedirs(os.path.dirname(os.path.join(OUT, spec["file"])), exist_ok=True)
        with open(os.path.join(OUT, spec["file"]), "w", encoding="utf-8") as fh:
            fh.write(html)


LOGO_SOURCES = [
    # Original transparent logo from the Squarespace media library (928x240).
    # Commit public/assets/jr-logo.png to the repo before Squarespace is cancelled.
    "https://images.squarespace-cdn.com/content/v1/5d9eaed4bf57527be7c50028/c2f798e6-e0f3-45a0-86e8-947aa60a30df/Untitled+design+%2814%29.png",
]


def fetch_assets():
    """Ensure brand images exist: logo, JR mark and watermark."""
    import io
    import urllib.request
    logo_path = os.path.join(ASSETS, "jr-logo.png")
    if not os.path.exists(logo_path):
        last = None
        for url in LOGO_SOURCES:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "image/png,image/*"})
                data = urllib.request.urlopen(req, timeout=30).read()
                Image.open(io.BytesIO(data)).convert("RGBA").save(logo_path, optimize=True)
                break
            except Exception as exc:  # try next source
                last = exc
        else:
            raise SystemExit(f"Could not fetch logo: {last}")
    logo = Image.open(logo_path).convert("RGBA")
    logo = logo.crop(logo.getbbox())
    logo.save(logo_path, optimize=True)
    # JR mark = everything left of the first wide empty column gap
    alpha = logo.split()[3]
    w, h = logo.size
    col_has_ink = [alpha.crop((x, 0, x + 1, h)).getextrema()[1] > 10 for x in range(w)]
    gap = next(x for x in range(int(w * 0.2), int(w * 0.5)) if not any(col_has_ink[x:x + 8]))
    mark = logo.crop((0, 0, gap, h))
    mark = mark.crop(mark.getbbox())
    mark.save(os.path.join(ASSETS, "jr-mark.png"), optimize=True)
    wm = Image.new("RGBA", mark.size, (235, 235, 235, 0))
    wm.putalpha(mark.split()[3])
    wm.save(os.path.join(ASSETS, "jr-watermark.png"), optimize=True)
    return logo.size


def build_config():
    cfg = {
        "buildCommand": "echo \"Prebuilt site: run python3 src/build.py locally before committing\"",
        "outputDirectory": "public",
        "installCommand": "",
        "framework": None,
        "cleanUrls": True,
        "trailingSlash": False,
        "redirects": [{"source": s, "destination": d, "permanent": True} for s, d in REDIRECTS],
        "headers": [{"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=3600, must-revalidate"}]}],
    }
    with open(os.path.join(ROOT, "vercel.json"), "w") as fh:
        json.dump(cfg, fh, indent=2)
    urls = "".join(f"<url><loc>{SITE}{p['path'] if p['path'] != '/' else '/'}</loc></url>"
                   for p in PAGES if p.get("sitemap", True))
    with open(os.path.join(OUT, "sitemap.xml"), "w") as fh:
        fh.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    with open(os.path.join(OUT, "robots.txt"), "w") as fh:
        fh.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")


def build_images():
    logo = Image.open(os.path.join(ASSETS, "jr-logo.png")).convert("RGBA")
    mark = Image.open(os.path.join(ASSETS, "jr-mark.png")).convert("RGBA")
    wm = Image.open(os.path.join(ASSETS, "jr-watermark.png")).convert("RGBA")

    # Social share card 1200x630: dark ground, red glow, watermark, logo
    W, H = 1200, 630
    bg = Image.new("RGBA", (W, H), (12, 12, 12, 255))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(glow)
    d.ellipse((-200, 330, 700, 900), fill=(225, 6, 18, 70))
    d.ellipse((800, -260, 1500, 300), fill=(150, 150, 150, 60))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    bg.alpha_composite(glow)
    big = wm.resize((int(wm.width * 3.0), int(wm.height * 3.0)))
    a = big.split()[3].point(lambda v: int(v * 0.06))
    big.putalpha(a)
    bg.alpha_composite(big, (W - big.width + 140, -60))
    lw = 760
    lg = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    bg.alpha_composite(lg, ((W - lw) // 2, (H - lg.height) // 2 - 30))
    bar = ImageDraw.Draw(bg)
    bar.rectangle(((W - 90) // 2, (H + lg.height) // 2 + 10, (W + 90) // 2, (H + lg.height) // 2 + 15), fill=(225, 6, 18, 255))
    bg.convert("RGB").save(os.path.join(ASSETS, "og-image.png"), optimize=True)

    # Favicons from the JR mark on black
    for size, name in ((32, "favicon-32.png"), (180, "apple-touch-icon.png")):
        tile = Image.new("RGBA", (size, size), (10, 10, 10, 255))
        pad = int(size * 0.12)
        m = mark.copy()
        m.thumbnail((size - 2 * pad, size - 2 * pad), Image.LANCZOS)
        tile.alpha_composite(m, ((size - m.width) // 2, (size - m.height) // 2))
        tile.convert("RGB").save(os.path.join(ASSETS, name), optimize=True)


if __name__ == "__main__":
    import layout
    layout.LOGO_W, layout.LOGO_H = fetch_assets()
    import hashlib
    layout.CSS_VER = hashlib.sha1(open(os.path.join(ASSETS, "styles.css"), "rb").read()).hexdigest()[:10]
    build_pages()
    build_config()
    build_images()
    print("built", len(PAGES), "pages ->", OUT)
