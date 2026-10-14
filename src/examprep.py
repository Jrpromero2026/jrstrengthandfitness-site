"""/projects/vault/exam-prep: NASM-CPT Exam Prep, a product sold inside The Trainer's Coach Vault.

Source: the Vault chat's handoff (EXAM-PREP-WEBSITE-HANDOFF.md, 2026-10-14). Prices checked against
vault.jrstrengthandfitness.com/pricing on 2026-10-14. The Vault pricing page is the source of truth:
if JR changes a price there, change OFFER here.

Hard rules from the product's liability check (do not loosen):
- Never call it official, NASM-approved, endorsed or partnered. No NASM logo, colours or fonts.
- Never call the questions real, actual, recalled, leaked or "from the exam".
- No pass guarantee, pass rates or "pass first time". No invented testimonials, counts or results.
- Practice Readiness is a study signal, never a score, prediction or probability of passing.
- Don't claim expert or credentialed review of the question bank (still in progress).
- OPT is NASM's model: only ever to describe what the exam covers.
- The tutor is an "AI study tutor" and its answers can be wrong.
- DISCLAIMER goes, word for word, on every page that mentions NASM or NASM-CPT.
"""
import html as _h

from layout import VAULT
from ui import sec, head_row, rows, GRAIN

PATH = "/projects/vault/exam-prep"
BUY = VAULT + "/pricing#exam-prep"
TERMS = VAULT + "/terms"

# Word for word. Do not edit.
DISCLAIMER = ("This independent exam-preparation product is not affiliated with, endorsed by, or sponsored by the "
              "National Academy of Sports Medicine (NASM). NASM and NASM-CPT are used only to identify the certification "
              "exam this product is designed to help users prepare for.")

OFFER = dict(price=79, days=180, bundle_month=39, bundle_year=299)

TITLE = "NASM-CPT Exam Prep | The Trainer's Coach"
DESCRIPTION = ("Independent NASM-CPT exam practice: 1,322 original questions, timed 120-question mocks, concept cards "
               "and an AI study tutor. 180 days for $79.")

# NASM's public domain blueprint weights.
DOMAINS = [
    ("Exercise Technique and Training Instruction", 24),
    ("Program Design", 20),
    ("Assessment", 16),
    ("Basic and Applied Sciences and Nutritional Concepts", 15),
    ("Client Relations and Behavioral Coaching", 15),
    ("Professional Development and Responsibility", 10),
]
assert sum(w for _, w in DOMAINS) == 100

FAQ = [
    ("Is this affiliated with NASM?", "No. " + DISCLAIMER),
    ("Are these real exam questions?",
     "No. They are original practice questions written against NASM’s public exam blueprint."),
    ("How long do I have access?",
     f"{OFFER['days']} days from purchase. It doesn’t renew automatically. If you buy the Vault + Exam Prep bundle instead, "
     "Exam Prep stays open for as long as the bundle is active. The bundle is a recurring membership, billed monthly or yearly."),
    ("Does it work on my phone?",
     "Yes. It installs to your home screen and works offline. Your answers sync when the connection comes back."),
    ("What is the AI tutor?",
     "An AI study tutor that explains answers, compares the answer choices and writes new practice questions, up to 15 a day. "
     "It can make mistakes, so check anything important against your study materials."),
    ("What is Practice Readiness?",
     "A study signal built from your own practice. It is not an official NASM score or a probability of passing."),
    ("Can I get a refund?",
     f'Refunds follow the Vault’s terms. <a class="link-inline" href="{TERMS}" rel="noopener">Read the Vault terms</a>.'),
]


def _buy_btn(where):
    return (f'<a class="btn btn-red" href="{BUY}" rel="noopener" data-track="Exam Prep buy ({where})">'
            f'Get Exam Prep — ${OFFER["price"]}</a>')


def _bundle_link(where):
    return (f'<a class="link-u" href="{BUY}" rel="noopener" data-track="Exam Prep bundle ({where})">'
            "Or bundle it with the Vault →</a>")


OFFER_CARD = f"""<div class="info-card xp-offer">
<span class="k">Two ways to get it</span>
<div class="it"><b>Exam Prep · ${OFFER['price']} one-time</b><span>{OFFER['days']} days of access. Pay once, no auto-renewal. AI study tutor included.</span></div>
<div class="it"><b>The Vault + Exam Prep · ${OFFER['bundle_month']}/mo or ${OFFER['bundle_year']}/yr</b><span>A recurring membership, billed monthly or yearly. The full Vault library too, and Exam Prep stays open while the bundle is active.</span></div>
</div>"""

# App screenshots: live Vault, test account, 390x844 at 3x (captured by the Vault chat, 2026-10-14).
# Demo data only: the account's history came from a scripted diagnostic. Never present the numbers as a member's results.
# Resized to 640px wide WebP with all metadata stripped. Alt text is the Vault chat's, word for word.
SHOTS = {
    "question": "A practice question on a phone about using a 30-minute session well, with answer B marked correct and the explanation below it.",
    "readiness": "The Exam Prep progress screen on a phone, showing a Practice Readiness study signal of 55 and accuracy for each of the six exam domains.",
    "sort": "A sort activity on a phone where \"a sprinter trains short maximal efforts\" is placed under Specificity and marked as the right place, with the reason shown.",
    "concept": "A concept card on a phone for \"Overload and the other training principles\", with its summary, an Ask the tutor button and the learner's level of understanding.",
}


def _phone(key, lazy=True):
    return (f'<div class="xp-phone"><img src="/assets/exam-prep/{key}.webp" width="640" height="1385" '
            f'alt="{_h.escape(SHOTS[key])}"{" loading=\"lazy\"" if lazy else ""} decoding="async"></div>')


GALLERY = f"""<div class="xp-gallery" role="region" aria-label="Exam Prep screens" tabindex="0">
<figure>{_phone("readiness")}<figcaption><b>Progress</b><span>Practice Readiness and accuracy by domain</span></figcaption></figure>
<figure>{_phone("sort")}<figcaption><b>Sort</b><span>Place each idea where it belongs</span></figcaption></figure>
<figure>{_phone("concept")}<figcaption><b>Concept cards</b><span>Repetition, Categorization, Association</span></figcaption></figure>
</div>
<p class="muted xp-demo">Screens from the live app, using a demo account. Practice Readiness is a study signal, not a score.</p>"""

HERO = f"""<section class="hero dark short xp-hero">
{GRAIN}
<img class="watermark" src="/assets/jr-watermark.svg" alt="" aria-hidden="true">
<div class="wrap split">
<div class="main stack" style="gap:24px">
<span class="eyebrow">The Trainer’s Coach · Vault</span>
<h1 class="h-hero"><span class="ln" style="--i:0"><span>NASM-CPT</span></span> <span class="ln" style="--i:1"><span>Exam Prep</span></span></h1>
<p class="lead">Independent practice for the NASM-CPT exam. 1,322 original questions, timed mocks, concept cards and an AI study tutor, on your phone.</p>
<div class="btns" style="padding-top:6px">{_buy_btn("hero")}{_bundle_link("hero")}</div>
<p class="xp-legal">{DISCLAIMER}</p>
</div>
<div class="side xp-hero-side">{_phone("question", lazy=False)}</div>
</div>
</section>"""

INSIDE = rows([
    ("01", "Practice questions", "1,322 questions",
     "1,022 at the exam standard, across all six blueprint domains. 300 more go deeper: Optimal questions ask what fits one "
     "particular client best, and Enhanced questions go beyond the exam."),
    ("02", "Concept cards", "150 cards",
     "Flashcard review on every card, plus 151 sort sets and 416 scenarios and connections between concepts."),
    ("03", "Diagnostic and mock", "60 + 120 questions",
     "A 60-question diagnostic and a 120-question timed mock, both weighted to the public blueprint. The mock runs "
     "120 questions in 2 hours, the same length as the public exam format."),
    ("04", "AI study tutor", "Up to 15 a day",
     "Explains answers, compares the answer choices and writes new practice questions. It can be wrong, so check what matters."),
    ("05", "Progress tools", "Know what to study next",
     "Practice Readiness, accuracy by domain and competency, a missed-question queue, bookmarks and a study plan built "
     "from your exam date."),
    ("06", "On your phone", "Works offline",
     "Installs to your home screen and keeps working without a connection. Answers sync when you’re back online."),
])


def _weights():
    top = max(w for _, w in DOMAINS)
    items = "".join(
        f'<li><span class="xp-d">{_h.escape(n)}</span><span class="xp-p">{w}%</span>'
        f'<span class="xp-bar" aria-hidden="true"><i style="width:{w / top * 100:.1f}%"></i></span></li>'
        for n, w in DOMAINS)
    return f'<ul class="xp-weights" aria-label="Exam domains and their public weights">{items}</ul>'


MODEL = f"""<div class="split top xp-model">
<div class="main stack" style="gap:22px">
{head_row("The blueprint", "Six domains.<br>Weighted to match.",
          "Practice is weighted to NASM’s public domain percentages, so you spend your time where the exam does.")}
{_weights()}
</div>
<div class="side stack" style="gap:18px">
<span class="eyebrow">How you learn it</span>
<h3 class="h-cell">Every concept, three ways.</h3>
<ul class="ticks"><li><b>Repetition.</b> Flashcard review until it sticks.</li><li><b>Categorization.</b> Sort sets that make you place each idea where it belongs.</li><li><b>Association.</b> Scenarios that connect one concept to the next.</li></ul>
<p class="body">Knowledge is tiered the way I coach: <a class="link-inline" href="/#standard">Inadequate, Adequate, Optimal and Enhanced</a>. The 1,022 exam-standard questions are the core. The Optimal and Enhanced questions are there when you want more.</p>
</div>
</div>"""

STEPS = rows([
    ("01", "Diagnose", "Take the 60-question diagnostic.", "Find out where you stand across all six domains before you study."),
    ("02", "Practice", "Work on where you’re weakest.", "Accuracy by domain and the missed-question queue show you what to do next."),
    ("03", "Mock", "Sit a full 120-question timed mock.", "Two hours, the same length as the public exam format."),
])

PRICE = f"""<div class="xp-price">
<span class="eyebrow">Get it</span>
<div class="xp-amt"><b>${OFFER['price']}</b><span>one-time</span></div>
<p class="body">{OFFER['days']} days of access. Pay once, no auto-renewal.</p>
<div class="btns">{_buy_btn("price")}</div>
<p class="body xp-bundle">Already want the Vault? Get both for ${OFFER['bundle_month']} a month or ${OFFER['bundle_year']} a year. It’s a recurring membership, billed monthly or yearly, and Exam Prep stays open while it’s active. {_bundle_link("price")}</p>
<p class="muted xp-note">Checkout and your account live in the Vault. If you aren’t signed in, you’ll create a free account first, then come straight back to Exam Prep.</p>
</div>"""


def _faq():
    items = "".join(f'<details class="faq-q"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    return f'<div class="faq">{items}</div>'


BODY = (
    HERO
    + sec("light", head_row("What’s inside", "What you<br>study with.",
                            "Original practice questions, written against NASM’s public exam blueprint.") + GALLERY + INSIDE)
    + sec("dark", MODEL)
    + sec("light", f"""<div class="split top">
<div class="main stack" style="gap:22px">{head_row("How it works", "Diagnose.<br>Practice. Mock.", level="h2")}{STEPS}</div>
<div class="side">{PRICE}</div>
</div>""", id="get")
    + sec("gray", head_row("Questions", "Before you<br>buy.", "Straight answers about access, the tutor and what this is.", size="h-md")
          + _faq() + f'<p class="xp-legal xp-legal-foot">{DISCLAIMER}</p>', id="faq", label="Frequently asked questions")
)


def _plain(s):
    import re
    return _h.unescape(re.sub(r"<[^>]+>", "", s))


def schema(site, person_id, org_id):
    return [
        {"@type": "WebApplication", "name": "NASM-CPT Exam Prep", "url": site + PATH,
         "description": "Independent practice for the NASM-CPT exam: 1,322 original practice questions written against NASM's "
                        "public exam blueprint, a 60-question diagnostic, 120-question timed mocks, concept cards and an AI study tutor. "
                        + DISCLAIMER,
         "applicationCategory": "EducationalApplication", "operatingSystem": "Web, iOS, Android (installable web app)",
         "isPartOf": {"@type": "WebApplication", "name": "The Trainer's Coach Vault", "url": site + "/projects/vault"},
         "creator": {"@id": person_id}, "publisher": {"@id": org_id},
         "offers": [
             {"@type": "Offer", "name": "Exam Prep (180 days)", "price": str(OFFER["price"]), "priceCurrency": "USD", "url": BUY},
             {"@type": "Offer", "name": "The Vault + Exam Prep (monthly)", "price": str(OFFER["bundle_month"]), "priceCurrency": "USD", "url": BUY,
              "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(OFFER["bundle_month"]), "priceCurrency": "USD", "unitText": "MONTH"}},
             {"@type": "Offer", "name": "The Vault + Exam Prep (yearly)", "price": str(OFFER["bundle_year"]), "priceCurrency": "USD", "url": BUY,
              "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(OFFER["bundle_year"]), "priceCurrency": "USD", "unitText": "ANN"}},
         ]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": _plain(q), "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}} for q, a in FAQ]},
    ]


# Short block for the Vault's own project page (it mentions NASM, so the disclaimer goes with it).
VAULT_BLOCK = f"""<div class="split xp-vault">
<div class="main stack" style="gap:18px">
<span class="eyebrow">Also in the Vault</span>
<h2 class="h-md">NASM-CPT Exam Prep</h2>
<p class="lead">Independent practice for the NASM-CPT exam: 1,322 original questions, a 60-question diagnostic, 120-question timed mocks, concept cards and an AI study tutor. ${OFFER['price']} for {OFFER['days']} days, or bundled with the Vault.</p>
<div class="btns"><a class="btn btn-red" href="{PATH}">See Exam Prep</a></div>
<p class="xp-legal">{DISCLAIMER}</p>
</div>
</div>"""

# Guard: the banned words must never reach the page.
_BANNED = ("official", "guarantee", "pass first", "real exam question", "actual exam", "recalled", "leaked",
           "endorsed by nasm", "nasm-approved", "approved by nasm", "pass rate", "what's on the test", "what’s on the test")
# The FAQ is checked by hand: it has to name these things in order to deny them.
_check = (HERO + GALLERY + INSIDE + MODEL + STEPS + PRICE + VAULT_BLOCK + TITLE + DESCRIPTION).lower().replace(DISCLAIMER.lower(), "")
for _w in _BANNED:
    assert _w not in _check, f"Exam Prep copy uses a banned phrase: {_w!r}"
assert BODY.count(DISCLAIMER) >= 1 and DISCLAIMER in VAULT_BLOCK
