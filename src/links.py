"""/links: the Instagram link-in-bio page. Phone-first menu on JR's own domain.

Not in the main nav and noindex: it exists for the bio link only, so Search keeps sending people to the real pages.
Bio link: https://www.jrstrengthandfitness.com/links?utm_source=ig&utm_medium=social&utm_content=link_in_bio

Composition: one dark room. JR's photo up top, then the Sunday email, then a list of everything else where each
row shows the real thing behind it (the audit's cover, the Vault's screen, the exam question screen) before you tap.
Only real offers and facts from the rest of the site. When an offer changes on its own page, change it here too.
"""
import os
from PIL import Image

import layout as L
import examprep as XP

# source (under public/assets) -> crop box in pixels of the source, or None for the whole image
PICS = {
    "consult": ("photos/jr-portrait.webp", (0, 90, 832, 1130)),
    "online": ("photos/jr-portrait.webp", (176, 70, 656, 670)),
    "audit": ("resources/training-progress-audit-p1.webp", (0, 0, 600, 750)),
    "guide": ("resources/program-troubleshooting-field-guide-p1.webp", (0, 0, 600, 750)),
    "vault": ("vault/home-body.webp", (0, 0, 585, 731)),
    "exam": ("exam-prep/question.webp", (0, 0, 640, 800)),
}


def build_thumbs(assets):
    """4:5 crops for the list's lit picture, written to public/assets/links/. Never upscaled."""
    out = os.path.join(assets, "links")
    os.makedirs(out, exist_ok=True)
    for key, (src, box) in PICS.items():
        im = Image.open(os.path.join(assets, src)).convert("RGB").crop(box)
        if im.width > 800:
            im = im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS)
        im.save(os.path.join(out, f"{key}.webp"), "WEBP", quality=84)


ROWS = [  # (href, name, right-hand detail, description, picture, external, analytics label)
    (L.CONSULT, "Free consult", "30 min",
     "In person at Timberhill Athletic Club or G3 Sports &amp; Fitness in Corvallis. Every client starts here.",
     "consult", False, "Book a free consult"),
    ("/online-training", "Online coaching", "Apply",
     "Training and nutrition coaching wherever you are. It starts with a short application.",
     "online", False, None),
    ("/resources/training-progress-audit", "Training Progress Audit", "Free",
     "Six short worksheets for when progress stalls: what you expected, what you did, and what to do next.",
     "audit", False, None),
    ("/resources/program-troubleshooting-field-guide", "Program Troubleshooting Field Guide", "Free",
     "For coaches. The review I run before changing a stalled client’s program. Ends with one written adjustment.",
     "guide", False, None),
    (L.VAULT, "The Trainer’s Coach Vault", "Free account",
     "Systems, methods and tools for professional trainers and coaches.", "vault", True, None),
    (XP.HUB, "NASM-CPT and ACE-CPT exam prep", f"${XP.OFFER['price']}",
     f"Independent practice: 1,300+ original questions, timed mocks and concept cards, on your phone. {XP.OFFER['days']} days of access.",
     "exam", False, None),
]
PIC_ALT = {
    "consult": "JR Romero in the gym, arms crossed",
    "online": "JR Romero, close up",
    "audit": "Cover of the Training Progress Audit",
    "guide": "Cover of the Program Troubleshooting Field Guide",
    "vault": "The Trainer’s Coach Vault home screen",
    "exam": "A practice question in the exam prep app",
}


def rows():
    out = []
    for i, (href, name, detail, desc, pic, ext, track) in enumerate(ROWS):
        rel = ' rel="noopener"' if ext else ""
        out.append(
            f'<li><a class="lk-row{" on" if i == 0 else ""}" href="{href}"{rel} data-pic="{pic}" data-track="{track or name} (links)">'
            f'<span class="lk-name">{name}</span><span class="lk-detail">{detail}</span>'
            f'<span class="lk-desc">{desc}</span></a></li>')
    return "\n".join(out)


def pics():
    return "\n".join(
        f'<img class="lk-pic{" on" if i == 0 else ""}" data-pic="{k}" src="/assets/links/{k}.webp" alt="{PIC_ALT[k]}" '
        f'width="800" height="1000"{"" if i == 0 else " loading=\"lazy\""}>'
        for i, k in enumerate(PICS))


def lanes():
    return "".join(
        f'<label class="lk-lane"><input type="radio" name="interest" value="{k}"{" checked" if i == 0 else ""}><span>{t}</span></label>'
        for i, (k, t) in enumerate([("training", "My own training"), ("coach", "Coaching others"), ("women", "Women’s strength")]))


CSS = """<style>
body.lk-page { --ground: #0a0a0a; --step: #161616; --step2: #222; --ink: #F6F6F6; --soft: #B9B9B6;
  background: var(--ground); color: var(--ink); font-size: 17px; line-height: 1.6; }
.lk-wrap { max-width: 1240px; margin: 0 auto; padding: 0 20px; }
.lk-sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Top bar: the logo and one way out */
.lk-bar { display: flex; justify-content: space-between; align-items: center; padding-top: 20px; }
.lk-bar img { width: 104px; height: auto; display: block; }
.lk-bar a.out { font-size: 17px; font-weight: 500; color: var(--ink); padding: 10px 0; text-decoration: underline; text-decoration-color: var(--red); text-decoration-thickness: 2px; text-underline-offset: 6px; }

/* Hero: one lit photograph, the name under it */
.lk-hero { text-align: center; padding: 28px 0 0; }
.lk-photo { width: min(70vw, 300px); aspect-ratio: 4 / 5; margin: 0 auto; overflow: hidden; background: #111; }
.lk-photo img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 14%; display: block; filter: brightness(.92) contrast(1.04); }
.lk-hero h1 { margin-top: 22px; font-weight: 800; font-size: clamp(44px, 14.5vw, 88px); line-height: .92; letter-spacing: -.01em; }
.lk-hero .say { margin: 14px auto 0; font-size: 22px; line-height: 1.4; max-width: 24ch; }
.lk-row3 { margin-top: 22px; display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 14px 0; font-size: 14px; color: var(--soft); }
.lk-row3 .btn { order: -1; flex-basis: 100%; max-width: 300px; margin: 0 calc(50% - 150px); }
.lk-row3 .c1::after { content: "  ·  "; }

/* The Sunday email */
.lk-notes { padding-top: 96px; display: grid; gap: 26px; }
.lk-notes > div:first-child { display: grid; gap: 18px; }
.lk-notes h2 { font-weight: 800; font-size: clamp(40px, 10vw, 56px); line-height: .95; letter-spacing: -.01em; }
.lk-notes .say { font-size: 22px; line-height: 1.55; max-width: 34ch; }
.lk-form { background: var(--step); padding: 22px 20px 20px; display: flex; flex-direction: column; gap: 14px; }
.lk-form label.em { font-size: 17px; font-weight: 500; }
.lk-form input[type=email] { background: var(--ground); color: var(--ink); border: 1px solid #4a4a4a; min-height: 54px; font-size: 17px; }
.lk-form input[type=email]:focus { border-color: var(--ink); }
.lk-form legend { font-size: 17px; font-weight: 500; margin-bottom: 8px; }
.lk-lanes { display: grid; gap: 6px; }
.lk-lane { position: relative; cursor: pointer; }
.lk-lane input { position: absolute; inset: 0; opacity: 0; margin: 0; cursor: pointer; }
.lk-lane span { display: flex; align-items: center; min-height: 48px; padding: 0 16px; background: var(--step2); color: var(--soft); font-size: 17px; transition: background .15s, color .15s, transform .12s; }
.lk-lane span::before { content: ""; width: 10px; height: 10px; border-radius: 50%; margin-right: 12px; background: #555; flex-shrink: 0; }
.lk-lane input:checked + span { background: #343434; color: var(--ink); font-weight: 500; }
.lk-lane input:checked + span::before { background: var(--red); }
.lk-lane input:focus-visible + span { outline: 2px solid var(--ink); outline-offset: 2px; }
.lk-lane:active span { transform: scale(.985); }
.lk-form .btn { width: 100%; margin-top: 4px; }
.lk-form .fine { font-size: 14px; color: var(--soft); }
.lk-form .fine a { color: var(--ink); text-decoration: underline; text-decoration-color: var(--red); text-underline-offset: 3px; }
.lk-form .form-status { background: var(--step2); color: var(--ink); }

/* Everything else: a list, and the real thing behind the row you're on */
.lk-list { padding-top: 110px; }
.lk-list h2 { font-weight: 800; font-size: clamp(40px, 10vw, 56px); line-height: .95; letter-spacing: -.01em; margin-bottom: 18px; }
.lk-stage { position: sticky; top: 0; z-index: 2; height: 38svh; margin: 0 -20px; background: var(--ground); overflow: hidden; }
.lk-pic { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 0; opacity: 0; transition: opacity .3s ease; }
.lk-pic[data-pic=consult], .lk-pic[data-pic=online] { object-position: 50% 20%; }
.lk-pic.on { opacity: 1; }
.lk-items { list-style: none; margin: 0; padding: 10px 0 0; }
.lk-row { display: grid; grid-template-columns: 1fr auto; column-gap: 16px; align-items: baseline; padding: 15px 0; min-height: 56px; }
.lk-name { font-size: 22px; font-weight: 500; line-height: 1.25; color: var(--soft); transition: color .2s, transform .2s; }
.lk-detail { font-size: 14px; color: var(--soft); white-space: nowrap; }
.lk-desc { grid-column: 1 / -1; font-size: 17px; line-height: 1.5; color: var(--ink); max-width: 36ch; margin-top: 8px; }
.lk-row.on .lk-name, .lk-row:hover .lk-name, .lk-row:focus-visible .lk-name { color: var(--ink); }
.lk-row.on .lk-detail { color: var(--ink); }
html.js .lk-row .lk-desc { display: none; }
html.js .lk-row.on .lk-desc { display: block; }
.lk-row:active .lk-name { transform: translateX(4px); }

/* The close */
.lk-close { padding: 24svh 0 12svh; }
.lk-close p { font-size: 22px; line-height: 1.5; max-width: 34ch; }
.lk-close a { display: inline-block; margin-top: 20px; font-size: 17px; font-weight: 600; padding: 8px 0; text-decoration: underline; text-decoration-color: var(--red); text-decoration-thickness: 2px; text-underline-offset: 7px; }
.lk-foot { padding: 0 0 40px; display: flex; flex-wrap: wrap; gap: 10px 24px; font-size: 17px; }
.lk-foot a { color: var(--ink); padding: 6px 0; }
.lk-foot small { flex-basis: 100%; margin-top: 18px; font-size: 14px; color: var(--soft); }

@media (min-width: 900px) {
  .lk-wrap { padding: 0 32px; }
  .lk-bar { padding-top: 32px; }
  .lk-bar img { width: 132px; }
  .lk-hero { padding-top: 8px; }
  .lk-photo { width: auto; height: 56svh; max-height: 640px; }
  .lk-hero h1 { font-size: clamp(64px, 7vw, 104px); margin-top: 26px; }
  .lk-hero .say { max-width: none; }
  .lk-row3 { flex-wrap: nowrap; gap: 48px; }
  .lk-row3 .btn { order: 0; flex-basis: auto; margin: 0; }
  .lk-row3 .c1::after { content: none; }
  .lk-notes { padding-top: 180px; grid-template-columns: 5fr 1fr 6fr; align-items: start; }
  .lk-notes > div:first-child { grid-column: 1; gap: 24px; }
  .lk-form { grid-column: 3; padding: 32px; }
  .lk-list { padding-top: 200px; display: grid; grid-template-columns: 5fr 1fr 6fr; }
  .lk-list h2 { grid-column: 3; grid-row: 1; }
  .lk-stage { grid-column: 1; grid-row: 1 / span 2; position: sticky; top: 12vh; height: auto; aspect-ratio: 4 / 5; margin: 0; align-self: start; }
  .lk-items { grid-column: 3; grid-row: 2; padding: 0; }
  .lk-row { padding: 16px 0; }
  .lk-close { padding: 30svh 0 16svh; }
}

/* Motion: everything is visible without it; html.m is set only when it can finish and isn't unwanted */
@keyframes lk-in { from { opacity: 0; transform: translateY(22px); } to { opacity: 1; transform: none; } }
@keyframes lk-settle { from { transform: scale(1.07); } to { transform: scale(1); } }
html.m .lk-photo img { animation: lk-settle 2.4s cubic-bezier(.2,.7,.2,1) both; }
html.m .lk-hero h1, html.m .lk-hero .say, html.m .lk-row3 { animation: lk-in .8s cubic-bezier(.2,.7,.2,1) both; }
html.m .lk-hero h1 { animation-delay: .15s; } html.m .lk-hero .say { animation-delay: .23s; } html.m .lk-row3 { animation-delay: .31s; }
html.m .lk-up { opacity: 0; transform: translateY(24px); transition: opacity .7s cubic-bezier(.2,.7,.2,1), transform .7s cubic-bezier(.2,.7,.2,1); }
html.m .lk-up.in { opacity: 1; transform: none; }
.btn:active { transform: scale(.98); }
@media (prefers-reduced-motion: reduce) {
  .lk-pic, .lk-name, .lk-lane span { transition: none; }
  .btn:active, .lk-row:active .lk-name, .lk-lane:active span { transform: none; }
}
</style>"""

SCRIPT = """<script>
(function(){
  var root=document.documentElement; root.classList.add('js');
  /* The list: one row is "on"; its picture is lit. Hover or focus picks a row; on a phone, scrolling does. */
  var rows=[].slice.call(document.querySelectorAll('.lk-row')), pics=document.querySelectorAll('.lk-pic');
  function pick(r){ if(r.classList.contains('on')) return;
    rows.forEach(function(x){ x.classList.toggle('on', x===r); });
    pics.forEach(function(p){ p.classList.toggle('on', p.getAttribute('data-pic')===r.getAttribute('data-pic')); }); }
  rows.forEach(function(r){ r.addEventListener('mouseenter',function(){ pick(r); }); r.addEventListener('focus',function(){ pick(r); }); });
  var stage=document.querySelector('.lk-stage');
  function onScroll(){ if(innerWidth>=900||!stage) return;
    var line=stage.getBoundingClientRect().bottom+70, best=null, d=1e9;
    rows.forEach(function(r){ var b=r.getBoundingClientRect(), x=Math.abs(b.top-line); if(x<d){ d=x; best=r; } });
    if(best) pick(best); }
  var t=0; addEventListener('scroll',function(){ if(!t){ t=requestAnimationFrame(function(){ t=0; onScroll(); }); } },{passive:true});
  /* Entrances: the parts of each section rise in, in order, once. */
  if(!root.classList.contains('m')) return;
  var ups=[].slice.call(document.querySelectorAll('.lk-notes h2, .lk-notes .say, .lk-form, .lk-list h2, .lk-items li, .lk-close > *'))
    .filter(function(el){ return el.getBoundingClientRect().top > innerHeight*0.9; });
  var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(!e.isIntersecting) return;
    var el=e.target, sib=[].slice.call(el.parentNode.children).filter(function(c){ return c.classList.contains('lk-up'); });
    el.style.transitionDelay=Math.min(Math.max(sib.indexOf(el),0),6)*70+'ms'; el.classList.add('in'); io.unobserve(el); }); },{rootMargin:'0px 0px -6% 0px'});
  ups.forEach(function(el){ el.classList.add('lk-up'); io.observe(el); });
})();
</script>"""


def body():
    return f"""<div class="lk-wrap">
<div class="lk-bar"><a href="/" aria-label="JR Strength &amp; Fitness home"><img src="/assets/jr-logo.svg" alt="JR Strength &amp; Fitness" width="845" height="268"></a>
<a class="out" href="/">Full site</a></div>

<section class="lk-hero" aria-label="JR Romero">
<div class="lk-photo"><img src="/assets/photos/jr-portrait.webp" alt="JR Romero, arms crossed, in the gym" width="832" height="1248" fetchpriority="high"></div>
<h1>JR Romero</h1>
<p class="say">Strength coach in Corvallis, Oregon, and online.</p>
<div class="lk-row3"><span class="c1">CSCS</span><a class="btn btn-red" href="#notes">Get the Sunday email</a><span class="c2">20,000 hours on the floor</span></div>
</section>

<section class="lk-notes" id="notes" aria-labelledby="lk-notes-h">
<div><h2 id="lk-notes-h">Notes from the&nbsp;Floor</h2>
<p class="say">One email every Sunday: something I keep seeing with clients and coaches, and a tool you can use that week.</p></div>
<form class="lk-form" method="post" action="/newsletter" novalidate data-newsletter>
<div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
<label class="em" for="lk-email">Your email</label>
<input id="lk-email" name="email_address" type="email" autocomplete="email" required>
<fieldset><legend>Send me the version for</legend><div class="lk-lanes">{lanes()}</div></fieldset>
<div class="form-status" role="status" hidden></div>
<button class="btn btn-red" type="submit">Join the list</button>
<p class="fine">Free. Unsubscribe anytime. <a href="/privacy-policy">Privacy Policy</a></p>
</form>
</section>

<section class="lk-list" aria-labelledby="lk-list-h">
<h2 id="lk-list-h">Everything else</h2>
<div class="lk-stage" aria-hidden="true">
{pics()}
</div>
<ul class="lk-items">
{rows()}
</ul>
</section>

<section class="lk-close" aria-label="The full site">
<p>Want the longer version? The full site has my writing, what I’m building and how I coach.</p>
<a href="/">Visit jrstrengthandfitness.com</a>
</section>

<footer class="lk-foot">
<a href="/notes">Articles</a><a href="{L.INSTAGRAM}" rel="noopener">Instagram</a><a href="{L.YOUTUBE}" rel="noopener">YouTube</a><a href="{L.LINKEDIN}" rel="noopener">LinkedIn</a><a href="{L.FACEBOOK}" rel="noopener">Facebook</a><a href="mailto:{L.EMAIL}">Email</a>
<small>© 2026 JR Strength and Fitness LLC</small>
</footer>
</div>"""
