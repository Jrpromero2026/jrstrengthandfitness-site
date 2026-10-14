"""/proof: client reviews (the Review Wall) and client case files told on JR's IAOE scale.

Everything here is real and supplied or approved by JR:
- REVIEWS are copied word for word from Timberhill's Setmore reviews and name JR. Name = first name + last initial.
- CASES are written with the client and published only with their sign-off.

The page stays a hidden preview (noindex, out of the nav and sitemap, with visible slots) until
REVIEWS has at least MIN_REVIEWS entries. Then it goes live automatically on the next build.
"""
import html as _h

from layout import TAC_PT
from ui import hero, sec, head_row, ext, ph


class PENDING(str):
    """A fact JR still has to supply. Renders as a visible placeholder; the build refuses to ship one (see build.py)."""


def _txt(v):
    return ph(v) if isinstance(v, PENDING) else _h.escape(v)


SETMORE = "https://timberhill-personal-training.setmore.com/reviews"  # Timberhill's Setmore reviews page
# As shown on Setmore on 2026-10-12. Update when they move.
CLUB_RATING, CLUB_COUNT = "5.0", 160  # Timberhill Athletic Club overall (every trainer)
NAMED_COUNT = 20                       # reviews that name JR; every one is 5 stars
MIN_REVIEWS = 6

# dict(name="First L.", where="Timberhill" | "G3" | "Online", date="YYYY-MM", text="...as written...", tag="Training" | "Consult",
#      source="site" for reviews from /review; only post those where the client ticked publish_ok)
# Copied word for word from Timberhill's Setmore reviews (all 160 checked 2026-10-12; these name JR).
# Paragraph breaks kept; typos kept. Name = first name + last initial as the reviewer gave it.
# All 20 that name JR are here; JR is reviewing which to keep.
T, C = "Training", "Consult"
REVIEWS = [
    dict(name="Jen A.", date="2026-03", tag=T, text="I can’t say enough good things about JR as a personal trainer.\n\nAfter a hamstring rupture and surgical repair, I wasn’t sure what my recovery—or future strength—would look like. JR has been instrumental in not only helping me recover safely, but in building strength and confidence beyond where I was before the injury.\n\nHe brings a rare combination of deep knowledge, professionalism, and genuine respect for his clients. JR is patient, attentive, and highly intentional in how he programs and coaches. As someone who has been an athlete my entire life, I value being coached—and that’s exactly what this feels like. Every session has purpose, progression, and accountability.\n\nWhat’s been most impressive is his expertise in muscle building and strength development. Thanks to his guidance, I’ve been able to rebuild and even improve my physique—something I didn’t think was possible at age 50, especially after such a significant injury.\n\nIf you’re looking for someone who truly understands how to help you recover, get stronger, and perform at your best, JR is exceptional."),
    dict(name="North", date="2024-05", tag=T, text="JR is a well educated and top notch strength and conditioning coach. He is iterating over a custom strength training plan for me that will fit into my endurance cycling workouts. He understands the difficulties and nuance of combining strength training and endurance training while providing enough recovery. He knows all about progressive overload, training stress scores, macro and micro periodization, block training, and other concepts that many coaches don't understand. I feel lucky to have such a good coach."),
    dict(name="Walt P.", date="2024-11", tag=T, text="I am writing this review of my interactions and training with JR \n\nI have been very impressed with his evaluation of my age, condition, goals for a program to achieve better fitness. \nHis training regimen is focused on making sure my technique is correct to avoid issues and he brings excellent knowledge and encouragement while I ramp into this new phase. \n\nWalt"),
    dict(name="Laura", date="2023-10", tag=T, text="J.R is an awesome trainer!  He has carefully watched my body movements and choreographed strength and stretching exercises to help with these areas. He is patient, kind, and funny! I appreciate him so much! I love Timberhill and everyone who works there. Thank-you all! I have hope that I can improve my strength and balance. My arthritis is even better !"),
    dict(name="Maria", date="2024-03", tag=T, text="JR does a really good job of explaining things - both what is important in movement and posture, as well as in a picture of progression. He is clear but warm, and knowledgable. I'm looking forward to continuing to work with him  - I can already tell this is just the help I need."),
    dict(name="Andrew T.", date="2024-12", tag=T, text="JR is knowledgeable and has a great understanding body mechanics. He works with\nmy limitations and adjust the workout accordingly. He has a positive attitude, which make me look forward to my next training session. Highly recommend!"),
    dict(name="Steve", date="2024-06", tag=T, text="JR is an excellent trainer. I can see definite improvement in my strength and endurance since I started working with him. He’s the first trainer I’ve worked with and wish I had started sooner."),
    dict(name="Jess", date="2024-10", tag=C, text="JR had a consultation with me to discuss the club's personal training options. We asked lots of great questions to get to know my exercise and sports background, was empathetic to my health and injury issues in recent years. He reviewed the different options offered and and paired me up a trainer he felt would be the right match for me. I'm excited to begin with Mason!"),
    dict(name="Brenda R.", date="2026-04", tag=T, text="JR is knowledgeable , explains things well and intentional. You’re not exercising with JR, your training and focusing on muscle groups and getting stronger!"),
    dict(name="Walt P.", date="2025-09", tag=T, text="Today’s training with JR, was exactly the same as every workout. He is the consummate professional, exhibiting knowledge around various issues I have physically to both provide confidence and challenge. I cannot express enough gratitude that he is at Timberhill."),
    dict(name="Jo M.", date="2025-04", tag=T, text="JR has been a great help on my fitness path. He recognizes where I am at and helps me reach my personal goals."),
    dict(name="Deek", date="2024-05", tag=C, text="JR was waiting for me when I arrived and did a great job of explaining my options. He answered my questions clearly and  now have a good idea of how to proceed."),
    dict(name="Steve T.", date="2025-04", tag=T, text="J. R. Is a great trainer. He has helped me immensely getting into a regular exercise routine. I highly recommend him."),
    dict(name="Barb L.", date="2026-02", tag=C, text="From my first day of membership at the club there was this friendly and welcoming feeling. Met with JR and the training sessions were clearly explained and easily set up. Looking forward to more involvement."),
    dict(name="Brenda R.", date="2026-02", tag=C, text="Very intentional and focused…excited to work with JR, having support and a plan to help me reach my goals."),
    dict(name="Diana S.", date="2026-04", tag=C, text="J.R. was polite , knowledgeable and informative of the trainer programs available at TAC"),
    dict(name="Kristin G.", date="2024-11", tag=C, text="JR.  Helped me figure out a fitness plan for me. I was very happy with his advice."),
    dict(name="Chelsea C.", date="2025-10", tag=C, text="I have been training with Kyra since June. My main goal was to feel strong and confident in my body, and Kyra has helped me get there. I’ve made progress each week, with Kyra’s ability to create programs that keep me motivated, engaged and challenged. She is thoughtful, intentional with her coaching, supportive and always checks in to make sure I’m getting the most out of my workouts while staying safe. I’ve been able to accomplish new things while lifting that I never would have pushed myself to do on my own. Thank you to JR for matching me with Kyra!"),
    dict(name="Amanda B.", date="2025-09", tag=T, text="JR is a spectacular trainer. Extremely knowledgeable in anatomy and physiology. Knows how to coach for ideal mind muscle connection and create modifications fine tuned to my own needs/restrictions/injuries. Cannot recommend enough as a trainer. Hoping continued facility improvement and equipment updates are in the plan as well"),
    dict(name="Veronica J.", date="2025-04", tag=T, text="JR and Rebecca listened to my goals and the training (one year now) is fantastic! Rebecca listened and adapted exercises and also inspired me to continue my fitness journey! The best thing is I never felt too sore or there was never an exercise that caused any problems. Super!"),
]
for r in REVIEWS:
    r["where"] = "Timberhill"

# dict(name="First", where="Timberhill", mode="In person", length="6 months",
#      start_tier="Inadequate", to_tier="Optimal",      # two of: Inadequate, Adequate, Optimal, Enhanced
#      start="...their words...", plan="...what we changed...", now="...their words...",
#      results=["...", "...", "..."], photo="/assets/photos/....webp" (optional, with consent))
CASES = [
    # Yiğit O. Words are his, sent to JR on Instagram (Oct 14, 2026), posted as written. Photo supplied by JR.
    # Yiğit OK'd his name (first name + last initial), words and photo (confirmed by JR, Oct 14, 2026). Facts from JR.
    dict(name="Yiğit O.", where="Timberhill", mode="In person", length="3+ years",
         start_tier="Inadequate", to_tier="Enhanced",
         start=("Before I started training with JR, I had little to no experience with the gym or living a healthy lifestyle. "
                "I had worked with a few personal trainers back in my home country, but they never really pushed me into serious strength training.\n\n"
                "I had never deadlifted before, couldn’t do a single pull-up without resistance bands, and I still remember my legs shaking during "
                "lower-body exercises as I struggled just to keep my balance.\n\n"
                "I wasn’t necessarily starting from zero, but I was pretty close to it."),
         plan=("Our plan was simple: get stronger.\n\n"
               "I never showed JR pictures of someone whose physique I wanted to achieve. I never asked him to make me look like a particular person. "
               "I just told him one thing: I wanted to be strong.\n\n"
               "And that happened to be one of his greatest strengths as a trainer: knowing how to build real strength through the right training, "
               "proper technique, and consistent progression.\n\n"
               "We started training four times a week, eventually increasing to five sessions a week about a year later. The goal was always the same: "
               "keep getting stronger, keep pushing my limits, and keep improving.\n\n"
               "The physical transformation, healthier eating habits, and everything else? Those came along as welcome bonuses."),
         now=("These days, one of the first things I think about when I wake up is training. It has become such a natural part of my life "
              "that I can’t really imagine my routine without it.\n\n"
              "Of course, it comes with its own funny little downsides. Every time I eat, I find myself thinking about calories. But then again, "
              "I train more so I can eat more. And the more I train, the stronger I get. So I guess it all works out!\n\n"
              "But beyond the physical progress, training has completely changed my outlook on life.\n\n"
              "I’ve come to realize that working out isn’t something you do for a few months or years and then quit once you’re happy with the results. "
              "It’s a lifestyle. It’s about constantly challenging yourself, discovering what you’re capable of, and realizing that there’s always room to improve.\n\n"
              "And if you’re wondering when you finally reach that point where you’re completely satisfied?\n\n"
              "That’s the neat part. You don’t."),
         results=["Started at four sessions a week, now five", "Healthier eating habits", "3+ years of training, still getting stronger"],
         photo="/assets/photos/cases/yigit-o.webp", photo_alt="Yiğit O. standing on the training floor in a black long-sleeve shirt",
         photo_pos="50% 20%",
         quote="I just told him one thing: I wanted to be strong.",
         # Home-page excerpt: two of his sentences, verbatim; `key` is the phrase highlighted inside it.
         excerpt="I never asked him to make me look like a particular person. I just told him one thing: I wanted to be strong.",
         key="I wanted to be strong."),
]

# Every excerpt must be a word-for-word slice of the client's own story, and its key phrase must sit inside it.
for _c in CASES:
    if _c.get("excerpt"):
        assert any(_c["excerpt"] in _c[f] for f in ("start", "plan", "now")), f'{_c["name"]}: excerpt is not verbatim'
        assert _c.get("key") and _c["key"] in _c["excerpt"], f'{_c["name"]}: key phrase missing from excerpt'

LIVE = len(REVIEWS) >= MIN_REVIEWS
TIERS = ("Inadequate", "Adequate", "Optimal", "Enhanced")
STARS = '<span class="pf-stars" role="img" aria-label="5 out of 5 stars">★★★★★</span>'


def _slot(label, cls=""):
    return f'<span class="pf-slot {cls}">{label}</span>'


# ---------------------------------------------------------------- Review wall
SEAL = f"""<a class="pf-seal" href="{SETMORE}"{ext(SETMORE)} data-track="Setmore reviews (proof seal)">
<span class="pf-seal-n">5.0</span>{STARS}
<span class="pf-seal-c">{NAMED_COUNT} reviews name me</span>
<span class="pf-seal-s">Every one of them 5 stars. Timberhill overall: {CLUB_RATING} from {CLUB_COUNT}. See them on Setmore →</span></a>"""


def _review(r):
    tag = f' data-where="{r["where"]}"' + (f' data-tag="{r["tag"]}"' if r.get("tag") else "")
    paras = "".join(f"<p>{_h.escape(' '.join(x.split()))}</p>" for x in r["text"].split("\n\n") if x.strip())
    y, m = r["date"].split("-")
    when = f'{("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")[int(m) - 1]} {y}'
    return (f'<figure class="pf-rc"{tag}>{STARS}<blockquote>{paras}</blockquote>'
            f'<figcaption><b>{_h.escape(r["name"])}</b><span>{r["where"]} · {when}</span></figcaption></figure>')


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
    if len(places) < 2:
        places = []
    names = {"Training": "Training with JR", "Consult": "Consults"}
    chips = "".join(f'<button type="button" data-f="{f}" aria-pressed="false">{names.get(f, f)}</button>' for f in places + tags)
    filt = (f'<div class="pf-chips" role="group" aria-label="Filter reviews">'
            f'<button type="button" data-f="" aria-pressed="true">All</button>{chips}</div>') if len(places + tags) > 1 else ""
    more = (f'<p class="pf-more">Every Timberhill review is public on Setmore. '
            f'<a class="link-u" href="{SETMORE}"{ext(SETMORE)} data-track="Setmore reviews (proof wall)">Read them all →</a></p>'
            '<p class="pf-more">Trained with me? <a class="link-u" href="/review">Leave a review →</a></p>')
    return head_row("Client reviews", "In their words.",
                    "Copied word for word from Timberhill’s booking page, typos and all. Last names shortened to an initial.") + \
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


def _paras(text):
    return "".join(f"<p>{_h.escape(x.strip())}</p>" for x in text.split("\n\n") if x.strip())


def _case(c, n):
    alt = _h.escape(c.get("photo_alt") or f'{c["name"]}, client case file')
    pos = f' style="object-position:{c["photo_pos"]}"' if c.get("photo_pos") else ""
    photo = (f'<img src="{c["photo"]}" alt="{alt}" loading="lazy"{pos}>'
             if c.get("photo") else '<img class="mark" src="/assets/jr-mark.svg" alt="">')
    res = "".join(f"<li>{_txt(x)}</li>" for x in c["results"])
    long = " long" if max(len(c["start"]), len(c["plan"]), len(c["now"])) > 400 else ""
    return f"""<article class="pf-case{long}">
<div class="pf-case-ph">{photo}</div>
<div class="pf-case-b">
<div class="pf-tags"><span>Case file {n:02d}</span><span>{_txt(c["where"])}</span><span>{_txt(c["mode"])}</span><span>{_txt(c["length"])}</span></div>
<h3>{_h.escape(c["name"])}</h3>
{_track(c["start_tier"], c["to_tier"])}
{f'<blockquote class="pf-quote"><p>“{_h.escape(c["quote"])}”</p></blockquote>' if c.get("quote") else ""}
<ul class="pf-res">{res}</ul>
<details class="pf-story"><summary>Read {_h.escape(c["name"].split()[0])}’s full story</summary>
<div class="pf-steps"><div><b>Starting point</b>{_paras(c["start"])}</div><div><b>The plan</b>{_paras(c["plan"])}</div><div><b>Where now</b>{_paras(c["now"])}</div></div>
<p class="pf-src">In {_h.escape(c["name"].split()[0])}’s own words, as written.</p>
</details>
</div></article>"""


def home_excerpt():
    """Small pull from the newest case file with an excerpt, for the home page. Empty if there isn't one."""
    c = next((c for c in reversed(CASES) if c.get("excerpt")), None)
    if not c:
        return ""
    ex, key = _h.escape(c["excerpt"]), _h.escape(c["key"])
    ex = ex.replace(key, f"<mark>{key}</mark>", 1)
    first = _h.escape(c["name"].split()[0])
    meta = " · ".join(_h.escape(x) for x in (c["where"], c["length"]))
    return f"""<figure class="hx">
<blockquote><p>“{ex}”</p></blockquote>
<figcaption><b>{_h.escape(c["name"])}</b><span>{meta}</span><span>{c["start_tier"]} → {c["to_tier"]}</span></figcaption>
<a class="link-u" href="/proof#case-files">Read {first}’s case file →</a>
</figure>"""


def _case_slot(n=1):
    return f"""<article class="pf-case">
<div class="pf-case-ph">{_slot("Client photo<br>(with consent)", "fill")}</div>
<div class="pf-case-b">
<div class="pf-tags"><span>Case file {n:02d}</span><span>Facility</span><span>In person / Online</span><span>Duration</span></div>
<h3>Client first name</h3>
{_track("Adequate", "Optimal")}
<div class="pf-steps"><div><b>Starting point</b>{_slot("Their words")}</div><div><b>The plan</b>{_slot("What we changed")}</div><div><b>Where now</b>{_slot("Their words")}</div></div>
{_slot("A line in their words")}<div class="pf-res-slots">{_slot("Real result")}{_slot("Real result")}{_slot("Real result")}</div>
</div></article>"""


def _cases():
    head = head_row("Case files", "Where they started.<br>Where they are now.",
                    'Each client is placed on the same <a class="link-u" href="/#standard">Inadequate → Enhanced scale</a> I coach to. '
                    "Adequate is a real win, and it’s marked as one.")
    if CASES:
        import os
        extra = "".join(_case_slot(len(CASES) + k + 1) for k in range(int(os.environ.get("PREVIEW_CASE_SLOTS", "0"))))
        return head + "".join(_case(c, i + 1) for i, c in enumerate(CASES)) + extra
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
         ("Every review here names me, was written by a client on Timberhill’s booking page or my review form, and is posted as written."
          if any(r.get("source") == "site" for r in REVIEWS) else
          "Every review here names me, was written by a client on Timberhill’s booking page, and is posted as written."),
         f'<a class="btn btn-red" href="/consult">Book a free consult</a>'
         f'<a class="btn btn-line" href="{SETMORE}"{ext(SETMORE)} data-track="Setmore reviews (proof hero)">Read them on Setmore</a>',
         side=SEAL)
    + sec("dark", _cases(), id="case-files")
    + sec("gray", _wall(), id="reviews")
)
