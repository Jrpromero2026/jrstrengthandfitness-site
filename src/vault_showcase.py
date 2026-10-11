"""Home page "Featured project" block: The Trainer's Coach Vault, in the Vault's own brand.

The phone screens are real captures of vault.jrstrengthandfitness.com at phone width (see tools/vault_screens.py).
The floating cards repeat real Featured Systems cards from the Vault home page. Nothing here is invented.
"""
import json
import os

from layout import VAULT
from projects import VAULT_LOCKUP

META = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "vault_screens.json")))
PHONE_W, PHONE_H = 390, 844  # the CSS viewport the screens were captured at
STATUS = 44  # status bar above the page, in CSS px of that viewport (matches .vs-scroll margin-top)

# Real Featured Systems cards from the Vault home page (title, resource name, type · category).
CARDS = [
    ("How do I run the whole consultation, start to finish?", "Initial Consultation System", "System · Client Systems"),
    ("How do I judge a coach across weeks, not one workout?", "JR Coaching Audit Method", "System · JR Methods"),
]


def _phone(name, cls, delay="0s"):
    m = META[name]
    screen_h = m["w"] * (PHONE_H - STATUS) / PHONE_W  # visible page height at the capture's scale
    shift = max(0.0, (m["body"] - screen_h) / m["body"] * 100)  # % of the image's own height to scroll
    return (f'<div class="vs-phone {cls}"><div class="vs-screen">'
            f'<img class="vs-scroll" src="/assets/vault/{name}-body.webp" width="{m["w"]}" height="{m["body"]}" alt="" '
            f'loading="lazy" decoding="async" style="--shift:{shift:.2f}%;animation-delay:{delay}">'
            f'</div><span class="vs-island"></span></div>')


def _card(i, title, name, meta):
    return (f'<div class="vs-card vs-card-{i}"><span class="vs-card-q">{title}</span>'
            f'<span class="vs-card-n">{name}</span><span class="vs-card-m">{meta}<i>◆ Featured</i></span></div>')


def block():
    second = _phone("resource", "vs-phone-b", "-9s") if "resource" in META else ""
    cards = "".join(_card(i + 1, *c) for i, c in enumerate(CARDS))
    stage_label = ("The Trainer’s Coach Vault on a phone: the Vault home page scrolling through its featured systems"
                   + (", next to the Initial Consultation System page" if second else ""))
    return f"""<section class="sec gray vs-sec" aria-label="Featured project"><div class="wrap">
<div class="vs proj-vault{' vs-two' if second else ''}" data-vs>
<div class="vs-copy">
<span class="vs-eyebrow">Featured project</span>
{VAULT_LOCKUP}
<h2 class="vs-h">The operating library for coaches.</h2>
<p class="vs-lead">Consultation systems, programming frameworks and client-management tools I built and run across two facilities, packaged so a working coach can use them this week.</p>
<div class="vs-stats"><div><b data-count="34">34</b><span>Systems &amp; frameworks</span></div><div><b data-count="26">26</b><span>Tools</span></div><div><b data-count="11">11</b><span>Workflows</span></div></div>
<div class="btns"><a class="btn btn-pa" href="{VAULT}/signup" rel="noopener" data-track="Free Vault account (home)">Create a free account</a><a class="link-u" href="/projects/vault">About the Vault →</a></div>
</div>
<div class="vs-stage" role="img" aria-label="{stage_label}">
<div class="vs-glow" aria-hidden="true"></div>
<div aria-hidden="true">{second}{_phone("home", "vs-phone-a")}{cards}</div>
</div>
</div>
</div></section>
<script>
(function(){{
  var el=document.querySelector('[data-vs]'); if(!el) return;
  var still=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(still||!('IntersectionObserver' in window)) return;
  el.classList.add('armed');
  var nums=el.querySelectorAll('[data-count]');
  nums.forEach(function(n){{ n.textContent='0'; }});
  function count(){{ nums.forEach(function(n){{ var end=+n.getAttribute('data-count'), t0=null;
    function step(t){{ if(!t0) t0=t; var p=Math.min(1,(t-t0)/1400); n.textContent=Math.round(end*(1-Math.pow(1-p,3))); if(p<1) requestAnimationFrame(step); }}
    requestAnimationFrame(step); }}); }}
  var io=new IntersectionObserver(function(es){{ es.forEach(function(e){{
    if(e.isIntersecting){{ if(!el.classList.contains('in')){{ el.classList.add('in'); count(); }} el.classList.remove('paused'); }}
    else if(el.classList.contains('in')){{ el.classList.add('paused'); }}
  }}); }},{{threshold:0.25}});
  io.observe(el);
}})();
</script>"""
