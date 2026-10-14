"""Writing: long-form posts at /writing/<slug>.

Posts live in content/writing/<slug>.md with a front-matter block:

    title:     required
    date:      required, YYYY-MM-DD
    category:  required (also the topic filter on /writing)
    audience:  coach | bfh | client  (picks the call to action)
    excerpt:   required, one or two sentences (search snippet, cards, RSS)
    dek:       optional, the line under the headline (defaults to excerpt)
    updated:   optional, YYYY-MM-DD, shown as "Updated" and sent to search engines
    image:     optional, a file under public/ such as /assets/writing/<slug>.webp (1600x900 is ideal)
    image_alt: required when image is set: what the photo shows
    caption:   optional line under the featured image
    draft:     true keeps the post off /writing, the sitemap, RSS and llms.txt, and marks it noindex.
               Its page still builds at /writing/<slug> so it can be reviewed. Delete the line to publish.

Markdown supported in the body: paragraphs, ## and ### headings, numbered and bulleted lists,
**bold**, *italic*, [links](url), images on their own line ![alt](/assets/...), and:

    > A pull quote, one or more lines.
    > — Who said it (optional)

    :::copy The check-in            (a dark "your move" box with a Copy button)
    1. First question
    2. Second question
    :::

    :::box Label                    (the same box without the Copy button)
    Any paragraphs or lists.
    :::

A "## References" (or "## Sources") heading starts the source list, shown after the call to action.
The old /blog/<slug> URL redirects to /writing/<slug> (see build.py).
"""
import datetime as dt
import html
import os
import re
from email.utils import format_datetime

from layout import VAULT, LINKEDIN, CONSULT, SITE
from ui import hero, sec, head_row, _lines
import newsletter as NL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content", "writing")
PUBLIC = os.path.join(ROOT, "public")
BFH_TRIAL = "https://app.builtforher.io/pricing"
PORTRAIT = "/assets/photos/jr-portrait.webp"
FEED_PATH = "/writing/feed.xml"
FEED_LINK = f'<link rel="alternate" type="application/rss+xml" title="JR Strength &amp; Fitness: Writing" href="{FEED_PATH}">'
WPM = 230


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# ---------------------------------------------------------------- Markdown (the small subset the posts use)
def _inline(text):
    t = html.escape(text, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", _link, t)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t


def _link(m):
    href = html.unescape(m.group(2))
    rel = "" if href.startswith(("/", "#", "mailto:")) else ' rel="noopener"'
    return f'<a href="{html.escape(href)}"{rel}>{m.group(1)}</a>'


def _img_size(src):
    """Width and height of a local image, so the browser reserves its space (no layout shift)."""
    try:
        from PIL import Image
        with Image.open(os.path.join(PUBLIC, src.lstrip("/"))) as im:
            return im.size
    except Exception:
        raise SystemExit(f"Image not found under public/: {src}")


def _figure(src, alt, caption="", cls="post-img", eager=False):
    w, h = _img_size(src)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    cap = f"<figcaption>{_inline(caption)}</figcaption>" if caption else ""
    return (f'<figure class="{cls}"><img src="{html.escape(src)}" alt="{html.escape(alt)}" '
            f'width="{w}" height="{h}" {load}>{cap}</figure>')


def _box(kind, label, inner_md, n):
    inner = md_to_html(inner_md, boxes=False)
    copy = ""
    if kind == "copy":
        copy = (f'<button class="btn-copy" type="button" data-copy="#box-{n}">'
                '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect>'
                '<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>'
                f'<span>Copy</span><span class="sr"> {html.escape(label)}</span></button>')
    head = (f'<div class="move-head"><span class="eyebrow">{html.escape(label)}</span>{copy}</div>'
            if label or copy else "")
    return f'<aside class="move" aria-label="{html.escape(label or "Note")}">{head}<div class="move-body" id="box-{n}">{inner}</div></aside>'


def md_to_html(md, boxes=True):
    stash = {}
    if boxes:
        def keep(m):
            key = f"@@BOX{len(stash)}@@"
            stash[key] = _box(m.group(1), m.group(2).strip(), m.group(3), len(stash))
            return f"\n\n{key}\n\n"
        md = re.sub(r"^:::(copy|box)[ \t]*(.*?)\n(.*?)\n:::[ \t]*$", keep, md.strip(), flags=re.M | re.S)
    out, ids = [], set()
    for block in re.split(r"\n\s*\n", md.strip()):
        lines = [ln.rstrip() for ln in block.strip().splitlines()]
        if not lines:
            continue
        first = lines[0]
        if first in stash:
            out.append(stash[first])
        elif first.startswith(("## ", "### ")):
            level = 2 if first.startswith("## ") else 3
            text = first[level + 1:]
            hid = slugify(re.sub(r"[*\[\]()]", "", text)) or "section"
            while hid in ids:
                hid += "-2"
            ids.add(hid)
            out.append(f'<h{level} id="{hid}">{_inline(text)}</h{level}>')
        elif len(lines) == 1 and re.match(r"^!\[[^\]]*\]\([^)\s]+\)$", first):
            m = re.match(r"^!\[([^\]]*)\]\(([^)\s]+)\)$", first)
            out.append(_figure(m.group(2), m.group(1)))
        elif all(ln.startswith(">") for ln in lines):
            body = [ln.lstrip(">").strip() for ln in lines]
            who = ""
            if body and re.match(r"^(—|--)\s*", body[-1]):
                who = re.sub(r"^(—|--)\s*", "", body.pop())
            cap = f"<figcaption>{_inline(who)}</figcaption>" if who else ""
            out.append(f'<figure class="pull"><blockquote><p>{_inline(" ".join(body))}</p></blockquote>{cap}</figure>')
        elif all(re.match(r"^\d+\.\s", ln) for ln in lines):
            items = "".join(f"<li>{_inline(re.sub(r'^\d+\.\s+', '', ln))}</li>" for ln in lines)
            out.append(f"<ol>{items}</ol>")
        elif all(re.match(r"^[-*]\s", ln) for ln in lines):
            items = "".join(f"<li>{_inline(ln[2:])}</li>" for ln in lines)
            out.append(f"<ul>{items}</ul>")
        else:
            out.append(f"<p>{_inline(' '.join(lines))}</p>")
    return "\n".join(out)


def _date_h(d):
    return f"{d.strftime('%b')} {d.day}, {d.year}"


def _parse(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        raise SystemExit(f"Missing front matter: {path}")
    meta = dict(ln.split(": ", 1) for ln in m.group(1).splitlines() if ": " in ln)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    for key in ("title", "date", "category", "excerpt"):
        if not meta.get(key):
            raise SystemExit(f"{os.path.basename(path)}: front matter needs '{key}'")
    if meta.get("image") and not meta.get("image_alt"):
        raise SystemExit(f"{os.path.basename(path)}: 'image' needs 'image_alt' (describe what the photo shows)")
    body = m.group(2)
    # Split off the source list so the call to action sits right after the article.
    parts = re.split(r"\n## (?:References?|Sources?):?\s*\n", body, maxsplit=1)
    meta["slug"] = os.path.splitext(os.path.basename(path))[0]
    meta["audience"] = meta.get("audience", "client")
    meta["draft"] = meta.get("draft", "").lower() in ("true", "yes", "1")
    meta["topic"] = slugify(meta["category"])
    meta["dek"] = meta.get("dek") or meta["excerpt"]
    meta["body_html"] = md_to_html(parts[0])
    meta["refs_html"] = md_to_html(parts[1]) if len(parts) > 1 else ""
    d = dt.date.fromisoformat(meta["date"])
    meta["date_obj"], meta["date_h"] = d, _date_h(d)
    if meta.get("updated"):
        u = dt.date.fromisoformat(meta["updated"])
        meta["updated_obj"], meta["updated_h"] = u, _date_h(u)
    plain = re.sub(r"^:::.*$", "", parts[0], flags=re.M)
    meta["words"] = len(re.findall(r"\w+", plain))
    meta["mins"] = max(1, round(meta["words"] / WPM))
    return meta


def load_all():
    posts = [_parse(os.path.join(CONTENT, f)) for f in os.listdir(CONTENT) if f.endswith(".md")]
    return sorted(posts, key=lambda p: (p["date_obj"], p["slug"]), reverse=True)


ALL = load_all()
POSTS = [p for p in ALL if not p["draft"]]     # published: index, sitemap, RSS, llms.txt, redirects
DRAFTS = [p for p in ALL if p["draft"]]
TOPICS = sorted({p["category"] for p in POSTS})


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


# ---------------------------------------------------------------- Cards
def _media(p, cls):
    if p.get("image"):
        w, h = _img_size(p["image"])
        return (f'<div class="{cls}"><img src="{html.escape(p["image"])}" alt="" width="{w}" height="{h}" '
                'loading="lazy" decoding="async"></div>')
    return f'<div class="{cls} brand-fill"><img src="/assets/jr-mark.svg" alt="" width="64" height="64"></div>'


def _meta_line(p):
    return f'<time datetime="{p["date"]}">{p["date_h"]}</time> · {p["mins"]} min read'


def card(p, level="h3"):
    return f"""<article class="pcard" data-topic="{p["topic"]}">
<a href="/writing/{p["slug"]}">
{_media(p, "pcard-media")}
<span class="pcard-k">{html.escape(p["category"])}</span>
<{level} class="pcard-t">{html.escape(p["title"])}</{level}>
<span class="pcard-d">{_meta_line(p)}</span>
</a>
</article>"""


def feature(p):
    return f"""<article class="pfeature" data-topic="{p["topic"]}">
<a href="/writing/{p["slug"]}">
{_media(p, "pfeature-media")}
<div class="pfeature-text">
<span class="pcard-k">Latest · {html.escape(p["category"])}</span>
<h2 class="pfeature-t">{html.escape(p["title"])}</h2>
<p>{html.escape(p["excerpt"])}</p>
<span class="pcard-d">{_meta_line(p)}</span>
<span class="link-u">Read the article</span>
</div>
</a>
</article>"""


# ---------------------------------------------------------------- Index
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
    pills = "".join(
        f'<button type="button" class="pill" data-topic="{slugify(t)}" aria-pressed="false">{html.escape(t)}</button>'
        for t in TOPICS)
    filters = (f'<div class="topics" role="group" aria-label="Filter by topic" hidden data-topics>'
               f'<button type="button" class="pill" data-topic="" aria-pressed="true">All</button>{pills}</div>'
               '<p class="sr" role="status" data-topic-status></p>')
    lead, rest = (POSTS[0], POSTS[1:]) if POSTS else (None, [])
    archive = (
        head_row("The archive", "Long-form posts",
                 "Written for coaches, for women who lift and for anyone who wants to know why a program is built the way it is.")
        + filters
        + (feature(lead) if lead else "")
        + f'<div class="pgrid">{"".join(card(p) for p in rest)}</div>'
        + f'<p class="feed-link"><a class="link-u" href="{FEED_PATH}">RSS feed →</a></p>'
    )
    return (
        hero("Writing", "Coaching,<br>with the receipts.",
             "Research reviews and coaching notes. Every post lists its sources. Shorter posts go up on LinkedIn every weekday.",
             f'<a class="btn btn-red" href="{LINKEDIN}" rel="noopener">Follow JR on LinkedIn</a>'
             f'<a class="link-u" href="#coaches">For coaches →</a>',
             short=True, size="h-display")
        + sec("light", archive, mark=False, id="archive")
        + NL.block("dark", uid="w")
        + sec("gray", coach, mark=True, id="coaches", tight=True, label="For coaches")
    )


INDEX_SCRIPT = """<script>
/* Topic filter on /writing. Without JavaScript every post shows and the buttons stay hidden. */
(function(){
  var box=document.querySelector('[data-topics]'); if(!box) return;
  var items=document.querySelectorAll('.pcard,.pfeature'), status=document.querySelector('[data-topic-status]');
  var btns=box.querySelectorAll('button');
  function show(t, announce){
    var n=0;
    items.forEach(function(el){ var on=!t||el.getAttribute('data-topic')===t; el.hidden=!on; if(on) n++; });
    btns.forEach(function(b){ b.setAttribute('aria-pressed', String(b.getAttribute('data-topic')===t)); });
    if(announce) status.textContent='Showing '+n+(n===1?' post':' posts');
  }
  btns.forEach(function(b){ b.addEventListener('click',function(){
    var t=b.getAttribute('data-topic'); show(t,true);
    var u=new URL(location.href); if(t){ u.searchParams.set('topic',t); } else { u.searchParams.delete('topic'); }
    history.replaceState(null,'',u);
  }); });
  box.hidden=false;
  var t=new URLSearchParams(location.search).get('topic')||'';
  if(t && box.querySelector('[data-topic="'+t.replace(/[^a-z0-9-]/g,'')+'"]')) show(t,false);
})();
</script>"""


# ---------------------------------------------------------------- Post pages
ICONS = {
    "linkedin": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle>',
    "facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>',
    "x": '<path d="M4 4l16 16M20 4L4 20"></path>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="m22 7-10 6L2 7"></path>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>',
}


def _icon(name):
    return (f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def _share(p):
    from urllib.parse import quote
    url = quote(f"{SITE}/writing/{p['slug']}", safe="")
    title = quote(p["title"], safe="")
    links = [
        ("linkedin", "Share on LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={url}"),
        ("facebook", "Share on Facebook", f"https://www.facebook.com/sharer/sharer.php?u={url}"),
        ("x", "Share on X", f"https://x.com/intent/post?url={url}&amp;text={title}"),
    ]
    out = "".join(
        f'<a class="share-btn" href="{href}" target="_blank" rel="noopener" aria-label="{label} (opens in a new tab)" '
        f'data-track="{label}">{_icon(icon)}</a>' for icon, label, href in links)
    out += (f'<a class="share-btn" href="mailto:?subject={title}&amp;body={url}" aria-label="Share by email" '
            f'data-track="Share by email">{_icon("mail")}</a>')
    out += (f'<button class="share-btn" type="button" data-copy-link aria-label="Copy link to this article">'
            f'{_icon("link")}</button>')
    return f'<div class="share" role="group" aria-label="Share this article">{out}</div>'


def _byline(p):
    upd = (f' · Updated <time datetime="{p["updated"]}">{p["updated_h"]}</time>' if p.get("updated") else "")
    return f"""<div class="byline">
<div class="by">
<img class="avatar" src="{PORTRAIT}" alt="" width="56" height="56">
<div class="by-text">
<span>By <a href="/about">JR Prieto-Romero, CSCS</a></span>
<span class="by-meta">{_meta_line(p)}{upd}</span>
</div>
</div>
{_share(p)}
</div>"""


def _post_hero(p):
    return f"""<section class="hero dark short post-hero">
<img class="watermark" src="/assets/jr-watermark.svg" alt="" aria-hidden="true">
<div class="wrap">
<div class="post-head">
<nav class="crumbs" aria-label="Breadcrumb"><a href="/writing">Writing</a><span aria-hidden="true">/</span><a href="/writing?topic={p["topic"]}">{html.escape(p["category"])}</a></nav>
<h1 class="post-title">{_lines(html.escape(p["title"]))}</h1>
<p class="lead">{html.escape(p["dek"])}</p>
{_byline(p)}
</div>
</div>
</section>"""


def _author():
    return f"""<aside class="author" aria-label="About the author">
<img class="author-photo" src="{PORTRAIT}" alt="JR Prieto-Romero" width="96" height="96" loading="lazy">
<div class="author-text">
<p><strong>JR Prieto-Romero, CSCS</strong> is Director of Personal Training at Timberhill Athletic Club and Director of Performance at G3 Sports &amp; Fitness in Corvallis, Oregon. He has spent 10+ years and roughly 20,000 hours coaching on the floor, and builds The Trainer’s Coach Vault, Built For Her™, TRAINCND and The Credential Standard.</p>
<div class="btns"><a class="link-u" href="/about">About JR →</a><a class="link-u" href="/apply">Apply for coaching →</a><a class="link-u" href="{LINKEDIN}" rel="noopener">LinkedIn →</a></div>
</div>
</aside>"""


def _schema(p):
    import seo as S
    url = f"{SITE}/writing/{p['slug']}"
    post = {
        "@type": "BlogPosting", "@id": f"{url}#post",
        "headline": p["title"], "description": p["excerpt"],
        "datePublished": p["date"], "dateModified": p.get("updated", p["date"]),
        "url": url, "mainEntityOfPage": url,
        "image": SITE + p["image"] if p.get("image") else S.OG_IMAGE,
        "articleSection": p["category"], "wordCount": p["words"], "inLanguage": "en-US",
        "author": {"@id": S.PERSON_ID}, "publisher": {"@id": S.ORG_ID},
    }
    return S.ld(post, S.breadcrumbs([("Home", "/"), ("Writing", "/writing"), (p["title"], f"/writing/{p['slug']}")]))


def post_body(p):
    more = [q for q in POSTS if q["slug"] != p["slug"]]
    same = [q for q in more if q["topic"] == p["topic"]] + [q for q in more if q["audience"] == p["audience"]]
    picks = []
    for q in same + more:
        if q not in picks:
            picks.append(q)
    picks = picks[:3]
    refs = (f'<section class="refs" aria-labelledby="refs-h"><h2 id="refs-h">Sources</h2>{p["refs_html"]}</section>'
            if p["refs_html"] else "")
    draft = ('<p class="draft" role="note"><strong>Draft.</strong> This post isn’t listed on the site or in search. '
             'Delete the “draft: true” line in its file and rebuild to publish it.</p>' if p["draft"] else "")
    fig = (_figure(p["image"], p["image_alt"], p.get("caption", ""), cls="post-figure", eager=True)
           if p.get("image") else "")
    article = f"""<article class="post">
{draft}
{fig}
<div class="prose post-body">
{p["body_html"]}
</div>
{audience_cta(p["audience"])}
{refs}
<p class="post-topic"><a class="pill" href="/writing?topic={p["topic"]}">More on {html.escape(p["category"])}</a></p>
{_author()}
</article>"""
    related = ""
    if picks:
        related = sec("gray", head_row("Keep reading", "More writing", None, size="h-md")
                      + f'<div class="pgrid">{"".join(card(q) for q in picks)}</div>'
                      + '<div class="btns" style="padding-top:40px"><a class="link-u" href="/writing">All writing →</a></div>',
                      mark=False, tight=True, label="More writing")
    return (
        _post_hero(p)
        + sec("light", article, mark=False)
        + related
        + NL.block("dark", uid="p", default={"coach": "coach", "bfh": "women"}.get(p["audience"], "training"))
    )


POST_SCRIPT = """<script>
/* Copy the article link, or the text of a "your move" box. */
(function(){
  var live=document.createElement('p'); live.className='sr'; live.setAttribute('role','status'); document.body.appendChild(live);
  function copy(text, done){
    if(navigator.clipboard&&window.isSecureContext){ navigator.clipboard.writeText(text).then(done,function(){}); return; }
    var t=document.createElement('textarea'); t.value=text; t.setAttribute('readonly',''); t.style.position='absolute'; t.style.left='-9999px';
    document.body.appendChild(t); t.select(); try{ document.execCommand('copy'); done(); }catch(e){} document.body.removeChild(t);
  }
  document.querySelectorAll('[data-copy-link]').forEach(function(b){ b.addEventListener('click',function(){
    copy(location.origin+location.pathname,function(){ live.textContent='Link copied'; b.classList.add('done'); setTimeout(function(){ b.classList.remove('done'); live.textContent=''; },2000); });
    if(window.va) window.va('event',{name:'Share',data:{via:'copy link',page:location.pathname}});
  }); });
  document.querySelectorAll('[data-copy]').forEach(function(b){ b.addEventListener('click',function(){
    var el=document.querySelector(b.getAttribute('data-copy')); if(!el) return;
    var items=el.querySelectorAll('li'), text=items.length?Array.prototype.map.call(items,function(li,i){ return (i+1)+'. '+li.textContent.trim(); }).join('\\n'):el.innerText.trim();
    var label=b.querySelector('span'), old=label.textContent;
    copy(text,function(){ label.textContent='Copied'; live.textContent='Copied to clipboard'; setTimeout(function(){ label.textContent=old; live.textContent=''; },2000); });
  }); });
})();
</script>"""


def _head(p):
    tags = [f'<meta property="article:published_time" content="{p["date"]}">',
            f'<meta property="article:section" content="{html.escape(p["category"])}">',
            f'<meta property="article:author" content="{SITE}/about">']
    if p.get("updated"):
        tags.append(f'<meta property="article:modified_time" content="{p["updated"]}">')
    return "\n".join(tags) + "\n" + FEED_LINK + "\n" + _schema(p)


def page_specs():
    specs = []
    for p in ALL:
        title = p["title"] if len(p["title"]) > 42 else f"{p['title']} | JR Strength & Fitness"
        specs.append(dict(
            path=f"/writing/{p['slug']}", file=f"writing/{p['slug']}.html", active="",
            title=title, description=p["excerpt"], body=post_body(p), script=POST_SCRIPT,
            og_type="article", head=_head(p), sitemap=not p["draft"], noindex=p["draft"],
            og_image=SITE + p["image"] if p.get("image") else None,
            og_image_alt=html.escape(p["image_alt"]) if p.get("image") else None))
    return specs


# ---------------------------------------------------------------- RSS
def feed_xml():
    def esc(s):
        return html.escape(s, quote=False)
    items = []
    for p in POSTS[:30]:
        when = dt.datetime.combine(p["date_obj"], dt.time(12, 0), tzinfo=dt.timezone.utc)
        url = f"{SITE}/writing/{p['slug']}"
        items.append(f"""<item><title>{esc(p["title"])}</title><link>{url}</link><guid isPermaLink="true">{url}</guid>
<pubDate>{format_datetime(when)}</pubDate><category>{esc(p["category"])}</category><description>{esc(p["excerpt"])}</description></item>""")
    built = format_datetime(dt.datetime.combine(POSTS[0]["date_obj"], dt.time(12, 0), tzinfo=dt.timezone.utc)) if POSTS else ""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>
<title>JR Strength &amp; Fitness: Writing</title>
<link>{SITE}/writing</link>
<atom:link href="{SITE}{FEED_PATH}" rel="self" type="application/rss+xml"/>
<description>Research reviews and coaching notes from JR Prieto-Romero, CSCS.</description>
<language>en-us</language>
<lastBuildDate>{built}</lastBuildDate>
{"".join(items)}
</channel></rss>
"""
