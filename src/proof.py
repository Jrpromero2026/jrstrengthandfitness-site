"""/proof: client reviews (the Review Wall) and client case files told on JR's IAOE scale.

Everything here is real and supplied or approved by JR:
- REVIEWS are copied word for word from JR's Setmore booking page. Name = first name + last initial.
- CASES are written with the client and published only with their sign-off.

The page stays a hidden preview (noindex, out of the nav and sitemap, with visible slots) until
REVIEWS has at least MIN_REVIEWS entries. Then it goes live automatically on the next build.
"""
import html as _h

from layout import TAC_PT
from ui import hero, sec, head_row, ext

SETMORE = TAC_PT.split("?")[0]  # JR's Setmore booking page, where the reviews live
RATING, REVIEW_COUNT = "5.0", 160  # as shown on Setmore; update when it moves
MIN_REVIEWS = 6

# dict(name="First L.", where="Timberhill" | "G3" | "Online", text="...as written...", tag="Athlete" (optional))
REVIEWS = []

# dict(name="First", where="Timberhill", mode="In person", length="6 months",
#      start_tier="Inadequate", to_tier="Optimal",      # two of: Inadequate, Adequate, Optimal, Enhanced
#      start="...their words...", plan="...what we changed...", now="...their words...",
#      results=["...", "...", "..."], photo="/assets/photos/....webp" (optional, with consent))
CASES = []

LIVE = len(REVIEWS) >= MIN_REVIEWS
TIERS = ("Inadequate", "Adequate", "Optimal", "Enhanced")
STARS = '<span class="pf-stars" role="img" aria-label="5 out of 5 stars">★★★★★</span>'


def _slot(label, cls=""):
    return f'<span class="pf-slot {cls}">{label}</span>'


# ---------------------------------------------------------------- Review wall
SEAL = f"""<a class="pf-seal" href="{SETMORE}"{ext(SETMORE)} data-track="Setmore reviews (proof seal)">
<span class="pf-seal-n">{RATING}</span>{STARS}
<span class="pf-seal-c">{REVIEW_COUNT} client reviews</span>
<span class="pf-seal-s">On my Setmore booking page →</span></a>"""


def _review(r):
    tag = f' data-where="{r["where"]}"' + (f' data-tag="{r["tag"]}"' if r.get("tag") else "")
    return (f'<figure class="pf-rc"{tag}>{STARS}<blockquote>{_h.escape(r["text"])}</blockquote>'
            f'<figcaption><b>{_h.escape(r["name"])}</b><span>{r["where"]}</span></figcaption></figure>')


def _review_slot(i, where):
    h = (96, 60, 120, 74, 104, 62)[i % 6]
    return (f'<figure class="pf-rc" data-where="{where}">{STARS}{_slot("Real Setmore review", "")}'
            f'<figcaption><b>First name, last initial</b><span>{where}</span></figcaption></figure>'
            ).replace('class="pf-slot "', f'class="pf-slot" style="min-height:{h}px"')


def _wall():
    if REVIEWS:
        cards = "".join(_review(r) for r in REVIEWS)
        places = [w for w in ("Timberhill", "G3", "Online") if any(r["where"] == w for r in REVIEWS)]
        tags = sorted({r["tag"] for r in REVIEWS if r.get("tag")})
    else:
        cards = "".join(_review_slot(i, w) for i, w in enumerate(("Timberhill", "G3", "Timberhill", "Online", "G3", "Timberhill")))
        places, tags = ["Timberhill", "G3", "Online"], []
    chips = "".join(f'<button type="button" data-f="{f}" aria-pressed="false">{f}</button>' for f in places + tags)
    filt = (f'<div class="pf-chips" role="group" aria-label="Filter reviews">'
            f'<button type="button" data-f="" aria-pressed="true">All</button>{chips}</div>') if len(places + tags) > 1 else ""
    more = (f'<p class="pf-more">Showing {len(REVIEWS) or "a few"} of {REVIEW_COUNT}. '
            f'<a class="link-u" href="{SETMORE}"{ext(SETMORE)} data-track="Setmore reviews (proof wall)">Read every review on Setmore →</a></p>')
    return head_row("Client reviews", "In their words.",
                    "Copied word for word from my booking page. Nothing trimmed, nothing paraphrased.") + \
        f'{filt}<div class="pf-wall" data-pf-wall>{cards}</div>{more}'


# ---------------------------------------------------------------- Case files
def _track(a, b):
    i, j = TIERS.index(a), TIERS.index(b)
    out = []
    for k, t in enumerate(TIERS):
        cls = "from" if k == i else "to" if k == j else "path" if i < k < j else ""
        out.append(f'<span class="{cls}" style="--i:{max(0, k - i)}">{t}</span>')
    return (f'<div class="pf-track" role="img" aria-label="Moved from {a} to {b} on the IAOE scale">'
            + "".join(out) + "</div>")


def _case(c, n):
    photo = (f'<img src="{c["photo"]}" alt="{_h.escape(c["name"])}, client case file" loading="lazy">'
             if c.get("photo") else '<img class="mark" src="/assets/jr-mark.png" alt="">')
    res = "".join(f"<li>{_h.escape(x)}</li>" for x in c["results"])
    return f"""<article class="pf-case">
<div class="pf-case-ph">{photo}</div>
<div class="pf-case-b">
<div class="pf-tags"><span>Case file {n:02d}</span><span>{c["where"]}</span><span>{c["mode"]}</span><span>{c["length"]}</span></div>
<h3>{_h.escape(c["name"])}</h3>
{_track(c["start_tier"], c["to_tier"])}
<div class="pf-steps"><div><b>Starting point</b><p>{_h.escape(c["start"])}</p></div><div><b>The plan</b><p>{_h.escape(c["plan"])}</p></div><div><b>Where now</b><p>{_h.escape(c["now"])}</p></div></div>
<ul class="pf-res">{res}</ul>
</div></article>"""


def _case_slot():
    return f"""<article class="pf-case">
<div class="pf-case-ph">{_slot("Client photo<br>(with consent)", "fill")}</div>
<div class="pf-case-b">
<div class="pf-tags"><span>Case file 01</span><span>Facility</span><span>In person / Online</span><span>Duration</span></div>
<h3>Client first name</h3>
{_track("Adequate", "Optimal")}
<div class="pf-steps"><div><b>Starting point</b>{_slot("Their words")}</div><div><b>The plan</b>{_slot("What we changed")}</div><div><b>Where now</b>{_slot("Their words")}</div></div>
<div class="pf-res-slots">{_slot("Real result")}{_slot("Real result")}{_slot("Real result")}</div>
</div></article>"""


def _cases():
    head = head_row("Case files", "Where they started.<br>Where they are now.",
                    'Each client is placed on the same <a class="link-u" href="/#standard">Inadequate → Enhanced scale</a> I coach to. '
                    "Adequate is a real win, and it’s marked as one.")
    if CASES:
        return head + "".join(_case(c, i + 1) for i, c in enumerate(CASES))
    if not LIVE:
        return head + _case_slot()
    scale = "".join(f"<span>{t}</span>" for t in TIERS)
    return head + f"""<div class="pf-soon">
<div class="pf-track pf-track-static" aria-hidden="true">{scale}</div>
<p><b>The first case files are being written now.</b> Each one is told in the client’s own words and published only with their sign-off.
Training with me now and want yours told? Ask at your next session.</p></div>"""


SCRIPT = """<script>
(function(){
  var g=document.querySelector('.pf-chips'), w=document.querySelector('[data-pf-wall]'); if(!g||!w) return;
  g.addEventListener('click',function(e){
    var b=e.target.closest('button'); if(!b) return; var f=b.getAttribute('data-f');
    [].forEach.call(g.children,function(x){ x.setAttribute('aria-pressed', x===b); });
    [].forEach.call(w.children,function(c){
      c.hidden = !!f && c.getAttribute('data-where')!==f && c.getAttribute('data-tag')!==f;
    });
  });
})();
</script>"""

BODY = (
    ("" if LIVE else '<div class="pf-preview" role="note">Preview: dashed boxes are slots for real reviews and case files. '
     'This page stays hidden until they are filled.</div>')
    + hero("Proof", "Don’t take<br>my word<br>for it.",
         "Every review here was written by a client on my booking page and is posted as written. "
         "The case files show where clients started and where they are now, on the same scale I coach to.",
         f'<a class="btn btn-red" href="/consult">Book a free consult</a>'
         f'<a class="btn btn-line" href="{SETMORE}"{ext(SETMORE)} data-track="Setmore reviews (proof hero)">Read all {REVIEW_COUNT} on Setmore</a>',
         side=SEAL)
    + sec("gray", _wall(), id="reviews")
    + sec("dark", _cases(), id="case-files")
)
