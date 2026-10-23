"""/links: the Instagram link-in-bio page. Phone-first menu on JR's own domain.

Not in the main nav and noindex: it exists for the bio link only, so Search keeps sending people to the real pages.
Bio link: https://www.jrstrengthandfitness.com/links?utm_source=ig&utm_medium=social&utm_content=link_in_bio

Layout: full-bleed photo of JR with his name, the Sunday email, two training tiles, branded cards for the free
resources (real cover, then name > what it is > price and format > action), then every project in the same branded
card the site's Projects page uses (projects.cell), plus Exam Prep in the Vault's card. Only real offers and facts from the rest of the site; when an offer changes there, change it here.
"""
import os
import re
from PIL import Image

import layout as L
import examprep as XP
from projects import VAULT_LOCKUP, BY_SLUG, cell

# source (under public/assets) -> crop box in source pixels (None = whole image). Never upscaled.
PICS = {
    "audit": ("resources/training-progress-audit-p1.webp", None),
    "guide": ("resources/program-troubleshooting-field-guide-p1.webp", None),
}


def build_thumbs(assets):
    out = os.path.join(assets, "links")
    os.makedirs(out, exist_ok=True)
    for key, (src, box) in PICS.items():
        im = Image.open(os.path.join(assets, src)).convert("RGB")
        if box:
            im = im.crop(box)
        im.save(os.path.join(out, f"{key}.webp"), "WEBP", quality=86)
    for old in ("consult", "online", "vault", "exam"):  # used by earlier drafts
        p = os.path.join(out, f"{old}.webp")
        if os.path.exists(p):
            os.remove(p)


def text_tile(href, title, desc, act, track):
    return (f'<a class="lk-tile lk-t" href="{href}" data-track="{track} (links)">'
            f'<b>{title}</b><span>{desc}</span><em>{act}</em></a>')


# Brand marks. JRSF uses its own logo file; Vault products use the Vault's header lockup (same build as projects.py).
BRAND = {
    "jrsf": '<img class="lk-jrsf" src="/assets/jr-logo.svg" alt="JR Strength &amp; Fitness" width="845" height="268">',
    "vault": VAULT_LOCKUP,
    "exam": VAULT_LOCKUP.replace('<span class="v-vault">Vault</span>', '<span class="v-vault">Exam Prep</span>'),
}


def card(href, brand, pic, alt, title, desc, price, fmt, cta, ext=False, track=None):
    rel = ' rel="noopener"' if ext else ""
    skin = "j" if brand == "jrsf" else "v"
    w, h = {"audit": (600, 776), "guide": (600, 776)}[pic]
    track = track or re.sub(r"<[^>]+>|&shy;", "", title).replace("&amp;", "&")
    return (f'<a class="lk-card {skin}" href="{href}"{rel} data-track="{track} (links)">'
            f'<span class="lk-brand">{BRAND[brand]}</span>'
            f'<span class="lk-cbody"><img src="/assets/links/{pic}.webp" alt="{alt}" width="{w}" height="{h}" loading="lazy">'
            f'<span class="lk-ctxt"><b class="t">{title}</b><span class="d">{desc}</span>'
            f'<span class="m"><strong>{price}</strong> · {fmt}</span><em class="c">{cta}</em></span></span></a>')


def exam_cell():
    """Exam Prep is sold inside the Vault, so it wears the Vault's card with its own app name in the lockup."""
    return f"""<a class="cell brand-vault" href="{XP.HUB}">
<div class="bar"></div>
<div class="top"><h3 class="h-cell">{BRAND['exam']}</h3><span class="tag live">${XP.OFFER['price']} · {XP.OFFER['days']} days</span></div>
<span class="sig">NASM-CPT<i> · </i>ACE-CPT</span>
<p>Independent exam practice: original questions, timed mocks and concept cards, on your phone.</p>
<div class="grow"></div>
<span class="more">Learn more</span>
</a>"""


def projects():
    """All four projects, in the same branded cards the site's Projects page uses, plus Exam Prep under the Vault."""
    cells = [cell(BY_SLUG["vault"]), exam_cell()] + [cell(BY_SLUG[k]) for k in ("built-for-her", "traincnd", "credential-standard")]
    return f'<section class="lk-group" aria-label="Projects"><h2>Projects</h2><div class="panel brands lk-proj">{"".join(cells)}</div></section>'


def cards(title, *items):
    return f'<section class="lk-group" aria-label="{title}"><h2>{title}</h2><div class="lk-cards">{"".join(items)}</div></section>'


def group(title, *tiles):
    return f'<section class="lk-group" aria-label="{title}"><h2>{title}</h2><div class="lk-tiles">{"".join(tiles)}</div></section>'


def lanes():
    return "".join(
        f'<label class="lk-lane"><input type="radio" name="interest" value="{k}"{" checked" if i == 0 else ""}><span>{t}</span></label>'
        for i, (k, t) in enumerate([("training", "My training"), ("coach", "I coach"), ("women", "Women’s strength")]))


CSS = """<style>
body.lk-page { --cell: #151515; --cell-hover: #1c1c1c; --fg: #F6F6F6; --body: rgba(255,255,255,.84); --muted: rgba(255,255,255,.62);
  --line: rgba(255,255,255,.14); --eyebrow: #FF5A5F; --ground: #0a0a0a; --step: #151515; --step2: #222; --ink: #F6F6F6; --soft: #BDBDBA; background: var(--ground); }
.lk { min-height: 100svh; }
.lk-sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Hero: the photo is the page's first screen, name set into its lower edge */
.lk-hero { position: relative; height: min(70svh, 620px); min-height: 480px; overflow: hidden; background: #111; }
.lk-hero img.ph { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 16%; filter: grayscale(1) contrast(1.08) brightness(.95); }
.lk-hero::after { content: ""; position: absolute; inset: 0;  /* scrim so the name reads on the photo */
  background: linear-gradient(180deg, rgba(10,10,10,.5) 0%, rgba(10,10,10,0) 20%, rgba(10,10,10,0) 48%, rgba(10,10,10,.9) 84%, #0a0a0a 100%); }
.lk-top { position: absolute; z-index: 2; top: 18px; left: 20px; right: 20px; display: flex; justify-content: space-between; align-items: center; }
.lk-top img { width: 112px; height: auto; display: block; }
.lk-top a.site { font-weight: 500; font-size: 16px; color: #fff; padding: 8px 0; text-decoration: underline; text-decoration-color: var(--red); text-decoration-thickness: 2px; text-underline-offset: 6px; }
.lk-id { position: absolute; z-index: 2; left: 20px; right: 20px; bottom: 24px; }
.lk-id h1 { font-weight: 800; font-size: clamp(46px, 14vw, 72px); line-height: .92; letter-spacing: -.01em; }
.lk-id .cred { margin-top: 10px; font-size: 16px; font-weight: 500; color: var(--ink); }
.lk-id .cred span { color: var(--red); padding: 0 6px; }
.lk-id p.say { margin-top: 8px; font-size: 17px; line-height: 1.45; color: var(--soft); max-width: 32ch; }

.lk-col { padding: 6px 20px 40px; max-width: 580px; margin: 0 auto; }

/* The Sunday email: a solid panel, nothing drawn around it */
.lk-nl { margin-top: 6px; padding: 24px 20px 20px; background: var(--step); }
.lk-nl h2 { font-weight: 800; font-size: 34px; line-height: .98; }
.lk-nl > p { margin-top: 12px; color: var(--ink); font-size: 17px; line-height: 1.5; }
.lk-nl form { margin-top: 18px; display: flex; flex-direction: column; gap: 10px; }
.lk-nl input[type=email] { background: var(--ground); color: var(--ink); border: 1px solid #454545; min-height: 54px; }
.lk-nl input[type=email]::placeholder { color: #8d8d8a; }
.lk-nl input[type=email]:focus { border-color: var(--ink); }
.lk-lanes { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; }
.lk-lane { position: relative; cursor: pointer; }
.lk-lane input { position: absolute; inset: 0; opacity: 0; margin: 0; cursor: pointer; }
.lk-lane span { display: flex; align-items: center; justify-content: center; text-align: center; min-height: 48px; padding: 4px 6px;
  background: var(--step2); color: var(--soft); font-size: 14px; font-weight: 500; line-height: 1.2; transition: background .15s, color .15s, transform .12s; }
.lk-lane input:checked + span { background: #f6f6f6; color: #0a0a0a; font-weight: 600; }
.lk-lane input:focus-visible + span { outline: 2px solid var(--red); outline-offset: 2px; }
.lk-lane:active span { transform: scale(.97); }
.lk-nl .btn { width: 100%; margin-top: 4px; }
.lk-fine { font-size: 14px; color: var(--soft); }
.lk-fine a { color: var(--ink); text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.lk-nl .form-status { background: var(--step2); color: var(--ink); }

/* Groups of tiles */
.lk-group { margin-top: 44px; }
.lk-group h2 { font-weight: 800; font-size: 22px; line-height: 1.1; margin-bottom: 14px; }
.lk-tiles { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.lk-tile { display: flex; flex-direction: column; background: var(--step); color: var(--ink); transition: background .15s, transform .15s; }
.lk-tile:hover { background: #1d1d1d; }
.lk-tile:active { transform: scale(.985); }
.lk-tile b { font-weight: 700; font-size: 18px; line-height: 1.2; }
.lk-tile span { font-size: 15px; line-height: 1.45; color: var(--soft); }
.lk-t { padding: 18px 16px 16px; gap: 8px; min-height: 196px; }
.lk-t em { margin-top: auto; padding-top: 10px; font-style: normal; font-weight: 600; font-size: 15px; align-self: flex-start;
  text-decoration: underline; text-decoration-color: var(--red); text-decoration-thickness: 2px; text-underline-offset: 5px; }

/* Resource and project cards: brand mark, then the real cover or screen beside name > what > price > action */
.lk-cards { display: grid; gap: 10px; }
.lk-card { position: relative; display: block; overflow: hidden; padding: 16px 16px 18px; background: var(--step); color: var(--ink); transition: background .15s, transform .15s; }
.lk-card:hover { background: #1c1c1c; }
.lk-card:active { transform: scale(.99); }
.lk-brand { display: flex; align-items: center; min-height: 34px; margin-bottom: 14px; }
.lk-jrsf { width: 92px; height: auto; display: block; }
.lk-card .v-lockup { display: inline-flex; align-items: center; gap: 9px; }
.lk-card .v-lockup img { width: 30px; height: auto; }
.lk-card .v-stack { display: flex; flex-direction: column; gap: 2px; }
.lk-card .v-brand { font-family: "Inter", sans-serif; font-weight: 600; font-size: 8px; letter-spacing: .2em; text-transform: uppercase; color: #C9A24B; }
.lk-card .v-name { font-family: "Montserrat", sans-serif; font-weight: 700; font-size: 11px; text-transform: uppercase; color: #CFCFCB; line-height: 1; }
.lk-card .v-vault { font-family: "Montserrat", sans-serif; font-weight: 800; font-size: 17px; text-transform: uppercase; color: #C9A24B; line-height: .95; }
.lk-cbody { display: grid; grid-template-columns: 108px 1fr; gap: 16px; align-items: start; }
.lk-cbody img { width: 100%; height: auto; display: block; outline: 1px solid rgba(255,255,255,.14); outline-offset: -1px; }
.lk-ctxt { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.lk-ctxt .t { font-weight: 800; font-size: 20px; line-height: 1.05; text-transform: uppercase; letter-spacing: .01em; hyphens: manual; }
.lk-ctxt .nw { white-space: nowrap; }
.lk-ctxt .d { font-size: 15px; line-height: 1.45; color: var(--soft); }
.lk-ctxt .m { margin-top: 4px; font-size: 15px; color: var(--soft); }
.lk-ctxt .m strong { font-weight: 700; color: #FF6B70; }
.lk-ctxt .c { margin-top: 6px; align-self: flex-start; font-style: normal; font-weight: 600; font-size: 15px;
  text-decoration: underline; text-decoration-color: var(--red); text-decoration-thickness: 2px; text-underline-offset: 5px; }
/* Vault products: the Vault's own card (#141414, #262626 edge, gold folded corner, gold accents) */
.lk-card.v { background: #141414; box-shadow: inset 0 0 0 1px #262626; }
.lk-card.v:hover { background: #181818; }
.lk-card.v::after { content: ""; position: absolute; top: 0; right: 0; width: 46px; height: 46px; background: linear-gradient(225deg, #C9A24B 0%, #C9A24B 48%, rgba(0,0,0,0) 48%); opacity: .3; pointer-events: none; }
.lk-card.v .m strong { color: #C9A24B; }
.lk-card.v .c { text-decoration-color: #C9A24B; }

/* Projects: the site's own branded project cards, tightened for a phone */
.lk-proj.panel { grid-template-columns: 1fr; gap: 10px; }
.lk-proj .cell { padding: 22px 20px 20px; gap: 10px; min-height: 0; }
.lk-proj .cell p { font-size: 16px; line-height: 1.5; }
.lk-proj .cell .tag { white-space: nowrap; }

.lk-full { display: block; margin-top: 44px; padding: 22px 20px; background: var(--step); }
.lk-full b { display: block; font-weight: 700; font-size: 18px; }
.lk-full span { display: block; margin-top: 4px; font-size: 15px; color: var(--soft); }
.lk-full:hover { background: #1d1d1d; }
.lk-foot { margin-top: 36px; display: flex; flex-wrap: wrap; gap: 6px 22px; font-size: 16px; }
.lk-foot a { color: var(--ink); padding: 6px 0; }
.lk-foot small { flex-basis: 100%; margin-top: 12px; font-size: 14px; color: var(--soft); }

@media (min-width: 960px) {
  .lk { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); }
  .lk-hero { position: sticky; top: 0; height: 100svh; max-height: none; }
  .lk-top { top: 32px; left: 40px; right: 40px; }
  .lk-top img { width: 140px; }
  .lk-id { left: 40px; right: 40px; bottom: 48px; }
  .lk-id h1 { font-size: 88px; }
  .lk-id .cred { font-size: 18px; }
  .lk-id p.say { font-size: 18px; }
  .lk-col { padding: 64px 56px 48px; margin: 0; max-width: 640px; }
  .lk-nl { margin-top: 0; padding: 32px 28px 26px; }
  .lk-nl h2 { font-size: 44px; }
  .lk-card { padding: 20px 20px 22px; }
  .lk-cbody { grid-template-columns: 150px 1fr; gap: 22px; }
  .lk-ctxt .t { font-size: 24px; hyphens: none; }
  .lk-ctxt .d, .lk-ctxt .m, .lk-ctxt .c { font-size: 16px; }
}

/* Motion: content is visible without it; html.m is set only when it can finish and isn't unwanted */
@keyframes lk-settle { from { transform: scale(1.06); } to { transform: scale(1); } }
@keyframes lk-in { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: none; } }
html.m .lk-hero img.ph { animation: lk-settle 2.4s cubic-bezier(.2,.7,.2,1) both; }
html.m .lk-id > * { animation: lk-in .7s cubic-bezier(.2,.7,.2,1) both; }
html.m .lk-id .cred { animation-delay: .08s; } html.m .lk-id .say { animation-delay: .16s; }
html.m .lk-up { opacity: 0; transform: translateY(22px); transition: opacity .6s cubic-bezier(.2,.7,.2,1), transform .6s cubic-bezier(.2,.7,.2,1); }
html.m .lk-up.in { opacity: 1; transform: none; }
.btn:active { transform: scale(.98); }
@media (prefers-reduced-motion: reduce) {
  .lk-tile, .lk-card, .lk-lane span { transition: none; }
  .lk-tile:active, .lk-card:active, .lk-lane:active span, .btn:active { transform: none; }
}
</style>"""

SCRIPT = """<script>
(function(){
  var root=document.documentElement; if(!root.classList.contains('m')) return;
  /* Groups rise in as they arrive, tiles one after another. */
  var ups=[].slice.call(document.querySelectorAll('.lk-nl, .lk-group h2, .lk-tile, .lk-card, .lk-proj .cell, .lk-full'))
    .filter(function(el){ return el.getBoundingClientRect().top > innerHeight*0.92; });
  var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(!e.isIntersecting) return;
    var el=e.target, i=[].indexOf.call(el.parentNode.children, el);
    el.style.transitionDelay=(el.classList.contains('lk-tile')||el.classList.contains('lk-card')||el.classList.contains('cell')? Math.min(i,4)*80 : 0)+'ms'; el.classList.add('in'); io.unobserve(el); }); },{rootMargin:'0px 0px -6% 0px'});
  ups.forEach(function(el){ el.classList.add('lk-up'); io.observe(el); });
})();
</script>"""


def body():
    return f"""<div class="lk">
<header class="lk-hero">
<img class="ph" src="/assets/photos/jr-portrait.webp" alt="JR Romero, arms crossed, in the gym" width="832" height="1248" fetchpriority="high">
<div class="lk-top"><a href="/" aria-label="JR Strength &amp; Fitness home"><img src="/assets/jr-logo.svg" alt="JR Strength &amp; Fitness" width="845" height="268"></a>
<a class="site" href="/">Full site</a></div>
<div class="lk-id"><h1>JR Romero</h1>
<p class="cred">CSCS<span aria-hidden="true">/</span>20,000 hours on the floor</p>
<p class="say">I coach at Timberhill and G3 in Corvallis, Oregon, and online.</p></div>
</header>
<div class="lk-col">
<section class="lk-nl" aria-labelledby="lk-nl-h">
<h2 id="lk-nl-h">Notes from<br>the Floor</h2>
<p>My email, every Sunday morning. What I keep seeing with clients and coaches, plus one tool you can use that week.</p>
<form method="post" action="/newsletter" novalidate data-newsletter>
<div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
<label class="lk-sr" for="lk-email">Email</label>
<input id="lk-email" name="email_address" type="email" autocomplete="email" placeholder="Your email" required>
<fieldset><legend class="lk-sr">Send me the version for</legend><div class="lk-lanes">{lanes()}</div></fieldset>
<div class="form-status" role="status" hidden></div>
<button class="btn btn-red" type="submit">Join the list</button>
<p class="lk-fine">Free. Unsubscribe anytime. <a href="/privacy-policy">Privacy Policy</a></p>
</form>
</section>
{group("Train with me",
    text_tile(L.CONSULT, "Free consult", "30 minutes, in person at Timberhill or G3 in Corvallis.", "Book a time", "Book a free consult"),
    text_tile("/online-training", "Online coaching", "Training and nutrition coaching, wherever you are.", "Apply", "Online coaching"))}
{cards("Free resources",
    card("/resources/training-progress-audit", "jrsf", "audit", "Cover of the Training Progress Audit",
         "Training Progress Audit", "Six short worksheets for when your progress stalls. Work out what happened before you change the plan.",
         "Free", "PDF, 7 pages", "Get the audit"),
    card("/resources/program-troubleshooting-field-guide", "vault", "guide", "Cover of the Program Troubleshooting Field Guide",
         "Program Trouble&shy;shooting Field Guide", "For coaches: the review I run before changing a stalled client’s program.",
         "Free", "PDF, 8 pages", "Get the Field Guide"))}
{projects()}
<a class="lk-full" href="/"><b>Visit the full site</b><span>My writing, what I’m building and how I coach.</span></a>
<footer class="lk-foot">
<a href="/notes">Articles</a><a href="{L.INSTAGRAM}" rel="noopener">Instagram</a><a href="{L.YOUTUBE}" rel="noopener">YouTube</a><a href="{L.LINKEDIN}" rel="noopener">LinkedIn</a><a href="{L.FACEBOOK}" rel="noopener">Facebook</a><a href="mailto:{L.EMAIL}">Email</a>
<small>© 2026 JR Strength and Fitness LLC</small>
</footer>
</div>
</div>"""
