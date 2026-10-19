"""Builds the static site into ../public. Run: python3 src/build.py"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from layout import page, SITE  # noqa: E402
import pages as P  # noqa: E402
import projects as PR  # noqa: E402
import writing as W  # noqa: E402
import newsletter as NL  # noqa: E402
import seo as S  # noqa: E402
import proof as PF  # noqa: E402

INDEXNOW_KEY = "56104907287d3a6e9553e37ffe6a0415"
import review as RV  # noqa: E402
import layout as L  # noqa: E402
import examprep as XP  # noqa: E402
import resources as RS  # noqa: E402
from PIL import Image, ImageDraw, ImageFilter  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public")
ASSETS = os.path.join(OUT, "assets")

PAGES = [
    dict(path="/", file="index.html", active="", schema=True,
         title="JR Romero, CSCS | Strength Coach in Corvallis, Oregon",
         description="Strength coach JR Romero, CSCS: personal training at Timberhill Athletic Club and G3 Sports & Fitness in Corvallis, online coaching, and tools for coaches.",
         body=P.HOME),
    dict(path="/train", file="train.html", active="train",
         title="Personal Trainer & Training in Corvallis, OR | JR Romero, CSCS",
         head=S.ld(S.IN_PERSON_SERVICE, S.FAQ_LD, S.breadcrumbs([("Home", "/"), ("Train with JR", "/train")])),
         description="Corvallis personal trainer JR Romero, CSCS. Start with a free consult at Timberhill Athletic Club or G3 Sports & Fitness. Not local? Apply for online coaching.",
         body=P.TRAIN),
    dict(path="/consult", file="consult.html", active="train",
         title="Book a Free Consult | Timberhill or G3 | JR Strength & Fitness",
         description="Local to Corvallis? Start with a free consult at Timberhill Athletic Club or G3 Sports & Fitness. Anywhere else, apply for online coaching.",
         body=P.CONSULT_PAGE, head=S.ld(S.IN_PERSON_SERVICE, S.breadcrumbs([("Home", "/"), ("Train with JR", "/train"), ("Free consult", "/consult")]))),
    dict(path="/online-training", file="online-training.html", active="train",
         title="Online Coaching | Training & Nutrition | JR Strength & Fitness",
         description="Individualized online training and nutrition coaching from JR Romero, CSCS. Essentials, Core and Premium packages from $199 a month.",
         body=P.ONLINE, head=S.ld(S.ONLINE_SERVICE, S.breadcrumbs([("Home", "/"), ("Train with JR", "/train"), ("Online coaching", "/online-training")]))),
    dict(path="/apply", file="apply.html", active="train",
         title="Apply for Online Coaching | JR Strength & Fitness",
         description="Apply for online training and nutrition coaching with JR Romero, CSCS. Applications go straight to JR.",
         body=P.APPLY, script=P.APPLY_SCRIPT + P.FORM_SCRIPT, closing=False),
    dict(path="/about", file="about.html", active="about",
         title="About JR Romero, CSCS | JR Strength & Fitness",
         description="JR Romero, CSCS: Director of Personal Training at Timberhill Athletic Club, Director of Performance at G3 Sports & Fitness, founder of four coaching products.",
         body=P.ABOUT),
    dict(path="/proof", file="proof.html", active="proof", sitemap=PF.LIVE, noindex=not PF.LIVE,
         title="Client Reviews & Results | JR Romero, CSCS",
         description=f"{PF.REVIEW_COUNT} client reviews of JR Romero, CSCS, posted word for word from {PF.SOURCES}.",
         body=PF.BODY, script=PF.SCRIPT, head=S.ld(S.breadcrumbs([("Home", "/"), ("Proof", "/proof")]))),
    dict(path="/review", file="review.html", active="", sitemap=False, noindex=True, closing=False,
         title="Leave a Review | JR Strength & Fitness",
         description="Trained with JR Romero, CSCS? Leave a review. JR reads every one and posts it only with your permission.",
         body=RV.BODY, script=RV.SCRIPT + P.FORM_SCRIPT),
    dict(path="/notes", file="notes.html", active="",
         title="Notes from the Floor | JR Strength & Fitness",
         description="Research reviews and coaching notes from JR Romero, CSCS: consultations, programming, strength and conditioning science, and training women.",
         body=W.index_body(), script=W.INDEX_SCRIPT, head=W.FEED_LINK),
    dict(path="/newsletter", file="newsletter.html", active="",
         title="Newsletter | Notes from the Floor | JR Strength & Fitness",
         description="Notes from JR Romero, CSCS: what he's testing with clients and coaches, new writing, and first word on TRAINCND and The Credential Standard.",
         body=NL.PAGE),
    dict(path="/subscribed", file="subscribed.html", active="", sitemap=False, noindex=True,
         title="You're in | JR Strength & Fitness",
         description="Confirm your newsletter subscription from the email JR just sent.",
         body=NL.THANKS),
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
         description="What JR Romero is building: The Trainer’s Coach Vault, Built For Her™, TRAINCND and The Credential Standard.",
         body=PR.projects_index()),
] + [
    dict(path=f"/projects/{p['slug']}", file=f"projects/{p['slug']}.html", active="projects",
         title=f"{p['name']} | Projects | JR Strength & Fitness".replace("&amp;", "&"),
         description=p.get('meta') or (p['tagline'] + " " + p['card']).replace("&amp;", "&"),
         body=PR.project_page(p), script=P.FORM_SCRIPT if p.get("waitlist") else "",
         head=S.ld(S.project_ld(p), S.breadcrumbs([("Home", "/"), ("Projects", "/projects"), (p["name"].replace("&amp;", "&"), f"/projects/{p['slug']}")])))
    for p in PR.PROJECTS
] + [
] + [
    dict(path=p["path"], file=p["path"].lstrip("/") + ".html", active="projects", closing=False,
         title=p["title"], description=p["description"], body=XP.body(p),
         head=S.ld(*XP.schema(p, SITE, S.PERSON_ID, S.ORG_ID),
                   S.breadcrumbs([("Home", "/"), ("Projects", "/projects"), ("The Trainer's Coach Vault", "/projects/vault"),
                                  ("Exam Prep", XP.HUB), (p["name"], p["path"])])))
    for p in (XP.NASM, XP.ACE)
] + [
    dict(path=XP.HUB, file=XP.HUB.lstrip("/") + ".html", active="projects", closing=False,
         title=XP.HUB_TITLE, description=XP.HUB_DESCRIPTION, body=XP.HUB_BODY,
         head=S.ld(*XP.hub_schema(SITE),
                   S.breadcrumbs([("Home", "/"), ("Projects", "/projects"), ("The Trainer's Coach Vault", "/projects/vault"),
                                  ("Exam Prep", XP.HUB)]))),
] + W.page_specs() + [
    dict(path="/accessibility", file="accessibility.html", active="",
         title="Accessibility | JR Strength & Fitness",
         description="How jrstrengthandfitness.com is tested for accessibility, what was fixed and what is still known to be wrong.",
         body=P.ACCESSIBILITY),
    dict(path="/404", file="404.html", active="", sitemap=False, noindex=True,
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
    ("/new-gallery", "/"),
    ("/blog", "/notes"), ("/blog-1", "/notes"),
    # Oct 2026: the articles section moved from /writing to /notes (Notes from the Floor)
    ("/writing", "/notes"), ("/writing/:path*", "/notes/:path*"),
] + [(f"/blog/{p['slug']}", f"/notes/{p['slug']}") for p in W.POSTS] + [
    # 2023 posts that were retired: send each to its closest match
    ("/blog/mastering-client-assessment-and-goal-setting-for-effective-progress",
     "/notes/5-questions-to-ask-during-a-personal-training-consultation"),
    ("/blog/creating-effective-workout-programs-a-step-by-step-guide-to-tailored-fitness-routines", "/projects/vault"),
    ("/blog/anatomy-and-exercise-science-basics-fundamentals-every-personal-trainer-should-know", "/projects/vault"),
    ("/blog/essential-qualities-of-personal-trainers", "/projects/vault"),
    ("/blog/introduction-to-personal-training-unveiling-the-role-benefits-and-opportunities", "/train"),
    ("/blog/:path*", "/notes"),
    ("/store", "/"), ("/store/:path*", "/"), ("/cart", "/"),
    # Oct 2026: the unpublished draft "How to Choose a Personal Trainer in Corvallis" was retired for this article
    ("/notes/how-to-choose-a-personal-trainer-in-corvallis", "/notes/what-to-look-for-personal-trainer-corvallis"),
    # Short links to Exam Prep. /exam-prep is now the hub page that lists both exams (Oct 17 2026).
    ("/nasm-cpt-exam-prep", XP.NASM["path"]), ("/nasm-exam-prep", XP.NASM["path"]), ("/projects/exam-prep", XP.HUB),
    ("/ace-cpt-exam-prep", XP.ACE["path"]), ("/ace-exam-prep", XP.ACE["path"]),
    # Review card QR codes land on /review; these send clients straight to Google's review form for each gym.
    ("/review/timberhill", RV.GOOGLE_REVIEW["timberhill"]), ("/review/g3", RV.GOOGLE_REVIEW["g3"]),
]
PAGES += RS.PAGES


# Share cards for the pages people send most (Oct 17 2026). Same design as the article cards.
PAGE_CARDS = [
    ("page-train", "Personal training in Corvallis", "TRAIN WITH JR"),
    ("page-consult", "Book a free 30-minute consult", "TIMBERHILL OR G3"),
    ("page-proof", f"{PF.REVIEW_COUNT} client reviews" + (", all five stars" if PF.ALL_FIVE and len(PF.RATED) == PF.REVIEW_COUNT else ""), "CLIENT REVIEWS"),
    ("page-online", "Online training and nutrition coaching", "ONLINE COACHING"),
]
_CARD_FOR = {"/train": "page-train", "/consult": "page-consult", "/proof": "page-proof", "/online-training": "page-online"}
for _spec in PAGES:
    _name = _CARD_FOR.get(_spec["path"])
    if _name:
        _head = next(h for n, h, _ in PAGE_CARDS if n == _name)
        _spec.update(og_image=SITE + f"/assets/share/{_name}.jpg", og_image_size=(1200, 630),
                     og_image_alt=f"{_head}: JR Romero, CSCS")


def build_pages():
    if PF.LIVE and not any(k == "proof" for _, _, k in L.NAV):
        L.NAV.insert(3, ("/proof", "Proof", "proof"))
    for spec in PAGES:
        html = page(path=spec["path"], title=spec["title"].replace("&", "&amp;"),
                    description=spec["description"].replace("&", "&amp;"), body=spec["body"],
                    active=spec["active"], schema=spec.get("schema", False),
                    script=spec.get("script", "") + (NL.SCRIPT if "data-newsletter" in spec["body"] else "")
                    + (PR.VAULT_STATS_SCRIPT if "data-vault-stat" in spec["body"] else "")
                    + (RS.SCRIPT if "rs-form" in spec["body"] else ""), closing=spec.get("closing", True),
                    og_type=spec.get("og_type", "website"), head=spec.get("head", ""), noindex=spec.get("noindex", False),
                    og_image=spec.get("og_image"), og_image_alt=spec.get("og_image_alt"), og_image_size=spec.get("og_image_size"))
        os.makedirs(os.path.dirname(os.path.join(OUT, spec["file"])), exist_ok=True)
        with open(os.path.join(OUT, spec["file"]), "w", encoding="utf-8") as fh:
            fh.write(html)


# ---------------------------------------------------------------- Launch guard
# Nothing on the built site may load from a third party at page load: no hosted fonts (GDPR),
# no session replay or ad pixels (wiretap claims, cookie consent). Vercel Web Analytics is
# first-party (/_vercel/insights) and cookieless. This scans the OUTPUT in public/, never src/,
# so the names below can't match the guard itself. Links and form actions are fine; loads are not.
THIRD_PARTY_LOADS = [
    r'<script[^>]*\ssrc=["\'](?:https?:)?//',
    r'<link[^>]*rel=["\'](?:stylesheet|preconnect|preload|modulepreload|dns-prefetch)["\'][^>]*href=["\'](?:https?:)?//',
    r'<link[^>]*href=["\'](?:https?:)?//[^"\']*["\'][^>]*rel=["\'](?:stylesheet|preconnect|preload|modulepreload|dns-prefetch)',
    r'<iframe[^>]*\ssrc=["\'](?:https?:)?//',
    r'@import\s+url\(\s*["\']?(?:https?:)?//',
    r'url\(\s*["\']?https?://',
    r'fonts\.googleapis\.com|fonts\.gstatic\.com|use\.typekit\.net',
    r'platform\.twitter\.com|platform\.linkedin\.com|connect\.facebook\.net/[^"\']*sdk|addthis|sharethis|disqus|hotjar\.com|fullstory\.com|logrocket|rrweb|smartlook|mouseflow|clarity\.ms|posthog|mixpanel|cdn\.amplitude|googletagmanager|google-analytics\.com|connect\.facebook\.net|static\.ads-twitter',
]


def guard_no_third_party():
    import re
    bad = []
    for d, _, files in os.walk(OUT):
        for f in files:
            if not f.endswith((".html", ".css", ".js")) or f.startswith("_"):
                continue
            path = os.path.join(d, f)
            text = open(path, encoding="utf-8").read()
            for pat in THIRD_PARTY_LOADS:
                for m in re.finditer(pat, text, re.I):
                    bad.append(f"{os.path.relpath(path, OUT)}: {m.group(0)[:90]}")
    if bad:
        raise SystemExit("Third-party load found in the built site:\n  " + "\n  ".join(sorted(set(bad))[:20]))


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
        # Redirects to other sites stay temporary (307), so changing the target later is never stuck in browser caches.
        "redirects": [{"source": s, "destination": d, "permanent": not d.startswith("http")} for s, d in REDIRECTS],
        "headers": [
            {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=3600, must-revalidate"}]},
            # Basic hardening. No CSP yet: the pages use inline scripts and styles.
            {"source": "/(.*)", "headers": [
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
                {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), interest-cohort=()"},
            ]},
        ],
    }
    with open(os.path.join(ROOT, "vercel.json"), "w") as fh:
        json.dump(cfg, fh, indent=2)
    _mod = {f"/notes/{p['slug']}": (p.get("updated_obj") or p["date_obj"]).isoformat() for p in W.ALL}
    urls = "".join(f"<url><loc>{SITE}{p['path'] if p['path'] != '/' else '/'}</loc>"
                   + (f"<lastmod>{_mod[p['path']]}</lastmod>" if p["path"] in _mod else "") + "</url>"
                   for p in PAGES if p.get("sitemap", True))
    with open(os.path.join(OUT, "sitemap.xml"), "w") as fh:
        fh.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    with open(os.path.join(OUT, "robots.txt"), "w") as fh:
        fh.write(S.robots_txt())
    # IndexNow (Bing, Yandex, Seznam, Naver): the key file proves the site owns the key used to ping
    # https://api.indexnow.org/indexnow when pages change. Set up Oct 18 2026. Do not change the key.
    with open(os.path.join(OUT, INDEXNOW_KEY + ".txt"), "w") as fh:
        fh.write(INDEXNOW_KEY)
    with open(os.path.join(OUT, "llms.txt"), "w") as fh:
        fh.write(S.llms_txt(PR.PROJECTS, W.POSTS))
    with open(os.path.join(OUT, "notes", "feed.xml"), "w", encoding="utf-8") as fh:
        fh.write(W.feed_xml())


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
    # Google wants a favicon that is a multiple of 48px; Bing and older tools ask for /favicon.ico at the root.
    def tile(size):
        t = Image.new("RGBA", (size, size), (10, 10, 10, 255))
        pad = int(size * 0.12)
        m = mark.copy()
        m.thumbnail((size - 2 * pad, size - 2 * pad), Image.LANCZOS)
        t.alpha_composite(m, ((size - m.width) // 2, (size - m.height) // 2))
        return t.convert("RGB")

    for size, name in ((32, "favicon-32.png"), (48, "favicon-48.png"), (96, "favicon-96.png"),
                       (180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")):
        tile(size).save(os.path.join(ASSETS, name), optimize=True)
    tile(48).save(os.path.join(OUT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    tile(180).save(os.path.join(OUT, "apple-touch-icon.png"), optimize=True)
    with open(os.path.join(OUT, "site.webmanifest"), "w") as fh:
        json.dump({"name": "JR Strength & Fitness", "short_name": "JR S&F", "start_url": "/", "display": "browser",
                   "background_color": "#0a0a0a", "theme_color": "#0a0a0a",
                   "icons": [{"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
                             {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, fh)


if __name__ == "__main__":
    import layout
    layout.LOGO_W, layout.LOGO_H = fetch_assets()
    import hashlib
    layout.CSS_VER = hashlib.sha1(open(os.path.join(ASSETS, "styles.css"), "rb").read()).hexdigest()[:10]
    build_pages()
    build_config()
    build_images()
    pending = [k for c in PF.CASES for k, v in c.items() if isinstance(v, PF.PENDING) or (isinstance(v, list) and any(isinstance(x, PF.PENDING) for x in v))]
    if pending and os.environ.get("ALLOW_PENDING") != "1":
        raise SystemExit("A case file still has placeholders JR must fill in: " + ", ".join(pending) + ". Set ALLOW_PENDING=1 only for a preview.")
    import sharecard
    sharecard.build_all(W.ALL, PAGE_CARDS)
    guard_no_third_party()
    print("built", len(PAGES), "pages ->", OUT)
