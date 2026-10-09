"""Writing: long-form posts migrated from the old Squarespace blog.

Posts live in content/writing/<slug>.md with a small front-matter block:
title, date (YYYY-MM-DD), category, audience (coach | bfh | client), excerpt.
The URL is /writing/<slug>. The old /blog/<slug> URL redirects there (see build.py).
"""
import datetime as dt
import html
import json
import os
import re

from layout import VAULT, LINKEDIN, CONSULT, SITE
from ui import hero, sec, head_row

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content", "writing")
BFH_TRIAL = "https://app.builtforher.io/pricing"


# ---------------------------------------------------------------- Markdown (the small subset the posts use)
def _inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
               lambda m: f'<a href="{html.escape(m.group(2))}" rel="noopener">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t


def md_to_html(md):
    out = []
    for block in re.split(r"\n\s*\n", md.strip()):
        lines = [ln.rstrip() for ln in block.strip().splitlines()]
        first = lines[0]
        if first.startswith("### "):
            out.append(f"<h3>{_inline(first[4:])}</h3>")
        elif first.startswith("## "):
            out.append(f"<h2>{_inline(first[3:])}</h2>")
        elif all(re.match(r"^\d+\.\s", ln) for ln in lines):
            items = "".join(f"<li>{_inline(re.sub(r'^\d+\.\s+', '', ln))}</li>" for ln in lines)
            out.append(f"<ol>{items}</ol>")
        elif all(re.match(r"^[-*]\s", ln) for ln in lines):
            items = "".join(f"<li>{_inline(ln[2:])}</li>" for ln in lines)
            out.append(f"<ul>{items}</ul>")
        else:
            out.append(f"<p>{_inline(' '.join(lines))}</p>")
    return "\n".join(out)


def _parse(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    meta = dict(ln.split(": ", 1) for ln in m.group(1).splitlines() if ": " in ln)
    body = m.group(2)
    # Split off the reference list so the call to action sits right after the article.
    parts = re.split(r"\n## References?:?\s*\n", body, maxsplit=1)
    meta["slug"] = os.path.splitext(os.path.basename(path))[0]
    meta["body_html"] = md_to_html(parts[0])
    meta["refs_html"] = md_to_html(parts[1]) if len(parts) > 1 else ""
    d = dt.date.fromisoformat(meta["date"])
    meta["date_obj"] = d
    meta["date_h"] = f"{d.strftime('%b')} {d.day}, {d.year}"
    meta["words"] = len(re.findall(r"\w+", parts[0]))
    return meta


def load_posts():
    posts = [_parse(os.path.join(CONTENT, f)) for f in os.listdir(CONTENT) if f.endswith(".md")]
    return sorted(posts, key=lambda p: p["date_obj"], reverse=True)


POSTS = load_posts()


# ---------------------------------------------------------------- Calls to action by audience
def _cta_block(eyebrow, title, para, btn, link):
    return f"""<aside class="post-cta dark" aria-label="{eyebrow}">
<span class="eyebrow">{eyebrow}</span>
<h2 class="h-cell">{title}</h2>
<p>{para}</p>
<div class="btns">{btn}{link}</div>
</aside>"""


def audience_cta(aud):
    if aud == "coach":
        return _cta_block(
            "For coaches", "Put this to work with your clients.",
            "The Trainer’s Coach Vault is my library of consultation systems, programming frameworks and client tools, "
            "including the Initial Consultation System. A free account opens selected resources, previews and search.",
            f'<a class="btn btn-red" href="{VAULT}/signup" rel="noopener" data-track="Free Vault account (post)">Get a free Vault account</a>',
            '<a class="link-u" href="/projects/vault" style="color:#fff">What’s in the Vault →</a>')
    if aud == "bfh":
        return _cta_block(
            "Built For Her™", "Training built for women, by design.",
            "Built For Her™ is my coach-built training app for women: structured programs, set-by-set logging "
            "and nutrition that matches the training. Try it free for 7 days.",
            f'<a class="btn btn-red" href="{BFH_TRIAL}" rel="noopener" data-track="BFH trial (post)">Start your free trial</a>',
            '<a class="link-u" href="/projects/built-for-her" style="color:#fff">About Built For Her™ →</a>')
    return _cta_block(
        "Train with JR", "Want this applied to your training?",
        "Local to Corvallis? Start with a free consult at Timberhill or G3. Anywhere else, apply for online coaching.",
        f'<a class="btn btn-red" href="{CONSULT}" data-track="Book a free consult (post)">Book a free consult</a>',
        '<a class="link-u" href="/apply" style="color:#fff" data-track="Apply (post)">Apply for online coaching →</a>')


# ---------------------------------------------------------------- Index
def _post_rows(posts):
    out = []
    for p in posts:
        out.append(
            f'<a class="row post-row" href="/writing/{p["slug"]}">'
            f'<span class="k">{p["category"]}<br><span class="dt">{p["date_h"]}</span></span>'
            f'<span class="t">{html.escape(p["title"])}</span>'
            f'<span class="d">{html.escape(p["excerpt"])}</span></a>'
        )
    return f'<div class="rows">{"".join(out)}</div>'


def index_body():
    coach = f"""<div class="coach-cap">
<div class="stack" style="gap:16px">
<span class="eyebrow">Coach or trainer?</span>
<h2 class="h-md">Get the systems behind the posts.</h2>
<p class="lead">The Trainer’s Coach Vault holds the consultation systems, programming frameworks and client tools I use on the floor. A free account opens selected resources, previews and search.</p>
</div>
<div class="btns"><a class="btn btn-red" href="{VAULT}/signup" rel="noopener" data-track="Free Vault account (writing)">Get a free Vault account</a>
<a class="link-u" href="/projects/vault">What’s in the Vault →</a></div>
</div>"""
    return (
        hero("Writing", "Coaching,<br>with the receipts.",
             "Research reviews and coaching notes. Every post lists its sources. Shorter posts go up on LinkedIn every weekday.",
             f'<a class="btn btn-red" href="{LINKEDIN}" rel="noopener">Follow JR on LinkedIn</a>'
             f'<a class="link-u" href="#coaches">For coaches →</a>',
             short=True, size="h-display")
        + sec("light", head_row("The archive", "Long-form posts",
                                "Written for coaches, for women who lift and for anyone who wants to know why a program is built the way it is.")
              + _post_rows(POSTS), mark=False)
        + sec("gray", coach, mark=True, id="coaches", tight=True, label="For coaches")
    )


# ---------------------------------------------------------------- Post pages
def _schema(p):
    data = {
        "@context": "https://schema.org", "@type": "BlogPosting",
        "headline": p["title"], "description": p["excerpt"],
        "datePublished": p["date"], "url": f"{SITE}/writing/{p['slug']}",
        "mainEntityOfPage": f"{SITE}/writing/{p['slug']}",
        "image": f"{SITE}/assets/og-image.png",
        "author": {"@type": "Person", "name": "JR Prieto-Romero", "url": f"{SITE}/about"},
        "publisher": {"@type": "Organization", "name": "JR Strength & Fitness",
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/jr-logo.png"}},
    }
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def post_body(p):
    mins = max(1, round(p["words"] / 230))
    more = [q for q in POSTS if q["slug"] != p["slug"]]
    same = [q for q in more if q["audience"] == p["audience"]]
    more = (same + [q for q in more if q not in same])[:2]
    refs = (f'<section class="refs" aria-label="References"><h2>References</h2>{p["refs_html"]}</section>'
            if p["refs_html"] else "")
    article = f"""<article class="post">
<div class="prose post-body">
{p["body_html"]}
</div>
{audience_cta(p["audience"])}
{refs}
</article>"""
    return (
        hero(f'{p["category"]} · {p["date_h"]}', html.escape(p["title"]),
             f'By JR Prieto-Romero, CSCS · {mins} min read', short=True, size="h-md")
        + sec("light", article, mark=False)
        + sec("gray", head_row("Keep reading", "More writing", None, size="h-md")
              + _post_rows(more)
              + '<div class="btns" style="padding-top:36px"><a class="link-u" href="/writing">All writing →</a></div>',
              mark=False, tight=True)
    )


def page_specs():
    specs = []
    for p in POSTS:
        specs.append(dict(
            path=f"/writing/{p['slug']}", file=f"writing/{p['slug']}.html", active="",
            title=f"{p['title']} | JR Strength & Fitness", description=p["excerpt"],
            body=post_body(p), og_type="article", head=_schema(p)))
    return specs
