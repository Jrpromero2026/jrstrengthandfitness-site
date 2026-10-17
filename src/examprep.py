"""Exam Prep: NASM-CPT and ACE-CPT Exam Prep, two products sold inside The Trainer's Coach Vault, plus the
/exam-prep hub that lists both.

Sources: the Vault chat's handoffs (EXAM-PREP-WEBSITE-HANDOFF.md, 2026-10-14, for NASM-CPT;
ACE-EXAM-PREP-WEBSITE-HANDOFF.md, 2026-10-17, for ACE-CPT). Prices checked against
vault.jrstrengthandfitness.com/pricing on 2026-10-14 (NASM) and 2026-10-17 (ACE). The Vault pricing page is the
source of truth: if JR changes a price there, change OFFER here.

Hard rules from the products' liability checks (do not loosen):
- Never call either product official, approved, endorsed or partnered. No NASM or ACE logo, colours or fonts,
  and never put NASM or ACE inside JR's own logo or lockup.
- Never call the questions real, actual, recalled, leaked or "from the exam".
- No pass guarantee, pass rates or "pass first time". No invented testimonials, counts or results.
- Practice Readiness is a study signal, never a score, prediction or probability of passing.
- Don't claim expert or credentialed review of either question bank.
- OPT (NASM) and the ACE IFT Model, Mover Method and ABC Approach belong to their owners: only ever to describe
  what an exam covers, never as JR's branding.
- The tutor is an "AI study tutor" and its answers can be wrong.
- ACE only: never state the exam's time limit or its scored/unscored split (unconfirmed on an ACE page).
- Each disclaimer goes, word for word, on every page that mentions that certifier. A page that links to the
  other exam's page by name carries both.
"""
import html as _h
import re

from layout import VAULT
from ui import sec, head_row, rows, GRAIN

TERMS = VAULT + "/terms"
OFFER = dict(price=79, days=180, bundle_month=39, bundle_year=299)
HUB = "/exam-prep"

# Word for word. Do not edit.
NASM_DISCLAIMER = ("This independent exam-preparation product is not affiliated with, endorsed by, or sponsored by the "
                   "National Academy of Sports Medicine (NASM). NASM and NASM-CPT are used only to identify the certification "
                   "exam this product is designed to help users prepare for.")
ACE_DISCLAIMER = ("This independent exam-preparation product is not affiliated with, endorsed by, or sponsored by the "
                  "American Council on Exercise (ACE). ACE and ACE Certified Personal Trainer are used only to identify the "
                  "certification exam this product is designed to help users prepare for.")

# Words that must never reach the marketing copy (titles, hero, rows, steps, price box, blocks).
# The FAQ is checked by hand: it has to name some of these in order to deny them.
_BANNED = ("official", "guarantee", "pass first", "real exam question", "actual exam", "recalled", "leaked",
           "endorsed by", "approved", "partner", "pass rate", "what's on the test", "what’s on the test",
           "expert-reviewed", "reviewed by")

PRODUCTS = {
    "nasm": dict(
        key="nasm", exam="NASM-CPT", org="NASM", poss="NASM’s",
        name="NASM-CPT Exam Prep",
        path="/projects/vault/exam-prep",
        buy=VAULT + "/pricing#exam-prep",
        btn="Get Exam Prep",
        disclaimer=NASM_DISCLAIMER,
        title="NASM-CPT Exam Prep: NASM Personal Trainer Practice Questions | The Trainer's Coach",
        description=("Independent NASM-CPT exam practice: 1,322 original questions, timed 120-question mocks, concept cards "
                     "and an AI study tutor. 180 days for $79."),
        hero_lead="Independent practice for the NASM-CPT exam. 1,322 original questions, timed mocks, concept cards and an AI study tutor, on your phone.",
        outline="public exam blueprint",
        outline_eyebrow="The blueprint",
        n_domains="Six",
        core="1,022",
        # NASM's public domain blueprint weights.
        domains=[
            ("Exercise Technique and Training Instruction", 24),
            ("Program Design", 20),
            ("Assessment", 16),
            ("Basic and Applied Sciences and Nutritional Concepts", 15),
            ("Client Relations and Behavioral Coaching", 15),
            ("Professional Development and Responsibility", 10),
        ],
        inside=[
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
        ],
        steps=[
            ("01", "Diagnose", "Take the 60-question diagnostic.", "Find out where you stand across all six domains before you study."),
            ("02", "Practice", "Work on where you’re weakest.", "Accuracy by domain and the missed-question queue show you what to do next."),
            ("03", "Mock", "Sit a full 120-question timed mock.", "Two hours, the same length as the public exam format."),
        ],
        # App screenshots: live Vault, test account, 390x844 at 3x (captured by the Vault chat, 2026-10-14).
        # Demo data only. Resized to 640px wide WebP, metadata stripped. Alt text is the Vault chat's, word for word.
        img_dir="",
        shots={
            "question": "A practice question on a phone about using a 30-minute session well, with answer B marked correct and the explanation below it.",
            "readiness": "The Exam Prep progress screen on a phone, showing a Practice Readiness study signal of 55 and accuracy for each of the six exam domains.",
            "sort": "A sort activity on a phone where \"a sprinter trains short maximal efforts\" is placed under Specificity and marked as the right place, with the reason shown.",
            "concept": "A concept card on a phone for \"Overload and the other training principles\", with its summary, an Ask the tutor button and the learner's level of understanding.",
        },
        gallery=["readiness", "sort", "concept"],
        refund=f'Refunds follow the Vault’s terms. <a class="link-inline" href="{TERMS}" rel="noopener">Read the Vault terms</a>.',
        schema_desc=("Independent practice for the NASM-CPT exam: 1,322 original practice questions written against NASM's "
                     "public exam blueprint, a 60-question diagnostic, 120-question timed mocks, concept cards and an AI study tutor."),
        card="1,322 original questions, a 60-question diagnostic, 120-question timed mocks, concept cards and an AI study tutor.",
        llms=("independent practice for the NASM-CPT exam. 1,322 original practice questions written against NASM's public exam "
              "blueprint, a 60-question diagnostic, 120-question timed mocks, 150 concept cards and an AI study tutor"),
        banned_extra=(),
    ),
    "ace": dict(
        key="ace", exam="ACE-CPT", org="ACE", poss="ACE’s",
        name="ACE-CPT Exam Prep",
        path="/projects/vault/ace-cpt-exam-prep",
        buy=VAULT + "/pricing#ace-cpt-exam-prep",
        btn="Get ACE-CPT Exam Prep",
        disclaimer=ACE_DISCLAIMER,
        title="ACE-CPT Exam Prep: ACE Personal Trainer Practice Questions | The Trainer's Coach",
        description=("Independent ACE-CPT exam practice: 1,300 original questions, a timed 150-question mock, concept cards "
                     "and an AI study tutor. 180 days for $79."),
        hero_lead=("Independent practice for the ACE Certified Personal Trainer exam. 1,300 original questions, a timed "
                   "150-question mock, concept cards and an AI study tutor, on your phone."),
        outline="public exam content outline",
        outline_eyebrow="The content outline",
        n_domains="Four",
        core="1,000",
        # ACE's public exam content outline weights, in the outline's own order (the app lists them D1 to D4).
        domains=[
            ("Client Onboarding and Assessments", 23),
            ("Program Design and Implementation", 31),
            ("Program Modification and Progression", 27),
            ("Risk Management, Professional Conduct, and Ethical Business Practices", 19),
        ],
        inside=[
            ("01", "Practice questions", "1,300 questions",
             "1,000 at the exam standard, across all four domains of ACE’s public exam content outline. 300 more go deeper: "
             "Optimal questions ask what fits one particular client best, and Enhanced questions go beyond the exam."),
            ("02", "Concept cards", "150 cards",
             "Flashcard review on every card, plus 94 sort sets and 334 scenarios and connections between concepts."),
            ("03", "Diagnostic and mock", "75 + 150 questions",
             "A 75-question diagnostic and a 150-question timed practice mock, both weighted to ACE’s public domain "
             "percentages. The mock has 150 questions, the same number as the public exam."),
            ("04", "AI study tutor", "Up to 15 a day",
             "Explains answers, compares the answer choices and writes new practice questions. It can be wrong, so check what matters."),
            ("05", "Progress tools", "Know what to study next",
             "Practice Readiness, accuracy by domain and task, a missed-question queue, bookmarks and a study plan built "
             "from your exam date."),
            ("06", "On your phone", "Works offline",
             "Installs to your home screen and keeps working without a connection. Answers sync when you’re back online."),
        ],
        steps=[
            ("01", "Diagnose", "Take the 75-question diagnostic.", "Find out where you stand across all four domains before you study."),
            ("02", "Practice", "Work on where you’re weakest.", "Accuracy by domain and the missed-question queue show you what to do next."),
            ("03", "Mock", "Sit a full 150-question timed mock.", "150 questions, the same number as the public exam."),
        ],
        # App screenshots: live Vault, test account, 390x844 at 3x (captured by the Vault chat, 2026-10-17).
        # Demo data only: a script took the diagnostic at about 75% correct. Never present the numbers as a
        # member's results. Alt text is the Vault chat's (ALT-TEXT.md), word for word.
        img_dir="ace/",
        shots={
            "question": "A practice question on a phone about moving a cable pulley for a biceps curl, with answer D, line of pull, marked correct and the explanation below it.",
            "readiness": "The Exam Prep progress screen on a phone, showing a Practice Readiness study signal of 58 and accuracy for each of the four exam domains.",
            "sort": "A sort activity on a phone where \"squatting down to reach a low cupboard\" is placed under Bend-and-lift, one of five primary movement patterns, and marked as the right place, with the reason shown.",
        },
        gallery=["readiness", "sort"],
        refund=(f'Payments aren’t refundable, except where the law requires it. '
                f'<a class="link-inline" href="{TERMS}" rel="noopener">Read the Vault terms</a>.'),
        schema_desc=("Independent practice for the ACE Certified Personal Trainer exam: 1,300 original practice questions written "
                     "against ACE's public exam content outline, a 75-question diagnostic, a 150-question timed practice mock, "
                     "concept cards and an AI study tutor."),
        card="1,300 original questions, a 75-question diagnostic, a timed 150-question mock, concept cards and an AI study tutor.",
        llms=("independent practice for the ACE Certified Personal Trainer exam. 1,300 original practice questions written against "
              "ACE's public exam content outline, a 75-question diagnostic, a 150-question timed practice mock, 150 concept cards "
              "and an AI study tutor"),
        # The ACE exam's time limit is unconfirmed: no hours, minutes or "time limit" anywhere in the ACE copy.
        banned_extra=("hour", "minute", "time limit", "125 scored", "unscored"),
    ),
}
for _p in PRODUCTS.values():
    assert sum(w for _, w in _p["domains"]) == 100, _p["key"]

OTHER = {"nasm": "ace", "ace": "nasm"}

# Back-compat names used elsewhere in the build (NASM was the first product).
NASM, ACE = PRODUCTS["nasm"], PRODUCTS["ace"]
PATH, DISCLAIMER, TITLE, DESCRIPTION = NASM["path"], NASM_DISCLAIMER, NASM["title"], NASM["description"]


def _faq_items(p):
    return [
        (f"Is this affiliated with {p['org']}?", "No. " + p["disclaimer"]),
        ("Are these real exam questions?",
         f"No. They are original practice questions written against {p['poss']} {p['outline']}."),
        ("How long do I have access?",
         f"{OFFER['days']} days from purchase. It doesn’t renew automatically. If you buy the Vault + Exam Prep bundle instead, "
         "Exam Prep stays open for as long as the bundle is active. The bundle is a recurring membership, billed monthly or yearly."),
        ("Does it work on my phone?",
         "Yes. It installs to your home screen and works offline. Your answers sync when the connection comes back."),
        ("What is the AI tutor?",
         "An AI study tutor that explains answers, compares the answer choices and writes new practice questions, up to 15 a day. "
         "It can make mistakes, so check anything important against your study materials."),
        ("What is Practice Readiness?",
         f"A study signal built from your own practice. It is not an official {p['org']} score or a probability of passing."),
        ("Can I get a refund?", p["refund"]),
    ]


def _buy_btn(p, where):
    return (f'<a class="btn btn-red" href="{p["buy"]}" rel="noopener" data-track="{p["exam"]} Exam Prep buy ({where})">'
            f'{p["btn"]} — ${OFFER["price"]}</a>')


def _bundle_link(p, where):
    return (f'<a class="link-u" href="{p["buy"]}" rel="noopener" data-track="{p["exam"]} Exam Prep bundle ({where})">'
            "Or bundle it with the Vault →</a>")


def _phone(p, key, lazy=True):
    return (f'<div class="xp-phone"><img src="/assets/exam-prep/{p["img_dir"]}{key}.webp" width="640" height="1385" '
            f'alt="{_h.escape(p["shots"][key])}"{" loading=\"lazy\"" if lazy else ""} decoding="async"></div>')


_CAPTIONS = {
    "readiness": ("Progress", "Practice Readiness and accuracy by domain"),
    "sort": ("Sort", "Place each idea where it belongs"),
    "concept": ("Concept cards", "Repetition, Categorization, Association"),
}


def _gallery(p):
    figs = "".join(f'<figure>{_phone(p, k)}<figcaption><b>{_CAPTIONS[k][0]}</b><span>{_CAPTIONS[k][1]}</span></figcaption></figure>'
                   for k in p["gallery"])
    n = len(p["gallery"])
    return (f'<div class="xp-gallery{" n2" if n == 2 else ""}" role="region" aria-label="{p["name"]} screens" tabindex="0">\n{figs}\n</div>\n'
            '<p class="muted xp-demo">Screens from the live app, using a demo account. Practice Readiness is a study signal, not a score.</p>')


def _hero(p):
    return f"""<section class="hero dark short xp-hero">
{GRAIN}
<img class="watermark" src="/assets/jr-watermark.svg" alt="" aria-hidden="true">
<div class="wrap split">
<div class="main stack" style="gap:24px">
<span class="eyebrow">The Trainer’s Coach · Vault</span>
<h1 class="h-hero"><span class="ln" style="--i:0"><span>{p['exam']}</span></span> <span class="ln" style="--i:1"><span>Exam Prep</span></span></h1>
<p class="lead">{p['hero_lead']}</p>
<div class="btns" style="padding-top:6px">{_buy_btn(p, "hero")}{_bundle_link(p, "hero")}</div>
<p class="xp-legal">{p['disclaimer']}</p>
</div>
<div class="side xp-hero-side">{_phone(p, "question", lazy=False)}</div>
</div>
</section>"""


def _weights(p):
    top = max(w for _, w in p["domains"])
    items = "".join(
        f'<li><span class="xp-d">{_h.escape(n)}</span><span class="xp-p">{w}%</span>'
        f'<span class="xp-bar" aria-hidden="true"><i style="width:{w / top * 100:.1f}%"></i></span></li>'
        for n, w in p["domains"])
    return f'<ul class="xp-weights" aria-label="Exam domains and their public weights">{items}</ul>'


def _model(p):
    return f"""<div class="split top xp-model">
<div class="main stack" style="gap:22px">
{head_row(p['outline_eyebrow'], f"{p['n_domains']} domains.<br>Weighted to match.",
          f"Practice is weighted to {p['poss']} public domain percentages, so you spend your time where the exam does.")}
{_weights(p)}
</div>
<div class="side stack" style="gap:18px">
<span class="eyebrow">How you learn it</span>
<h3 class="h-cell">Every concept, three ways.</h3>
<ul class="ticks"><li><b>Repetition.</b> Flashcard review until it sticks.</li><li><b>Categorization.</b> Sort sets that make you place each idea where it belongs.</li><li><b>Association.</b> Scenarios that connect one concept to the next.</li></ul>
<p class="body">Knowledge is tiered the way I coach: <a class="link-inline" href="/#standard">Inadequate, Adequate, Optimal and Enhanced</a>. The {p['core']} exam-standard questions are the core. The Optimal and Enhanced questions are there when you want more.</p>
</div>
</div>"""


def _price(p):
    return f"""<div class="xp-price">
<span class="eyebrow">Get it</span>
<div class="xp-amt"><b>${OFFER['price']}</b><span>one-time</span></div>
<p class="body">{OFFER['days']} days of access. Pay once, no auto-renewal.</p>
<div class="btns">{_buy_btn(p, "price")}</div>
<p class="body xp-bundle">Already want the Vault? Get both for ${OFFER['bundle_month']} a month or ${OFFER['bundle_year']} a year. It’s a recurring membership, billed monthly or yearly, and Exam Prep stays open while it’s active. {_bundle_link(p, "price")}</p>
<p class="muted xp-note">Checkout and your account live in the Vault. If you aren’t signed in, you’ll create a free account first, then come straight back to {p['name']}.</p>
</div>"""


def _faq(p):
    items = "".join(f'<details class="faq-q"><summary>{q}</summary><p>{a}</p></details>' for q, a in _faq_items(p))
    return f'<div class="faq">{items}</div>'


def _other_link(p):
    o = PRODUCTS[OTHER[p["key"]]]
    return (f'<p class="body xp-other">Studying for the {o["exam"]} instead? <a class="link-inline" href="{o["path"]}">{o["name"]}</a> '
            f'is the same product, written against {o["poss"]} {o["outline"]}.</p>')


def body(p):
    o = PRODUCTS[OTHER[p["key"]]]
    return (
        _hero(p)
        + sec("light", head_row("What’s inside", "What you<br>study with.",
                                f"Original practice questions, written against {p['poss']} {p['outline']}.") + _gallery(p) + rows(p["inside"]))
        + sec("dark", _model(p))
        + sec("light", f"""<div class="split top">
<div class="main stack" style="gap:22px">{head_row("How it works", "Diagnose.<br>Practice. Mock.", level="h2")}{rows(p["steps"])}</div>
<div class="side">{_price(p)}</div>
</div>""", id="get")
        + sec("gray", head_row("Questions", "Before you<br>buy.", "Straight answers about access, the tutor and what this is.", size="h-md")
              + _faq(p) + _other_link(p)
              + f'<p class="xp-legal xp-legal-foot">{p["disclaimer"]}</p><p class="xp-legal xp-legal-foot">{o["disclaimer"]}</p>',
              id="faq", label="Frequently asked questions")
    )


def _plain(s):
    return _h.unescape(re.sub(r"<[^>]+>", "", s))


def schema(p, site, person_id, org_id):
    return [
        {"@type": "WebApplication", "name": p["name"], "url": site + p["path"],
         "description": p["schema_desc"] + " " + p["disclaimer"],
         "applicationCategory": "EducationalApplication", "operatingSystem": "Web, iOS, Android (installable web app)",
         "isPartOf": {"@type": "WebApplication", "name": "The Trainer's Coach Vault", "url": site + "/projects/vault"},
         "creator": {"@id": person_id}, "publisher": {"@id": org_id},
         "offers": [
             {"@type": "Offer", "name": f"{p['name']} (180 days)", "price": str(OFFER["price"]), "priceCurrency": "USD", "url": p["buy"]},
             {"@type": "Offer", "name": f"The Vault + {p['name']} (monthly)", "price": str(OFFER["bundle_month"]), "priceCurrency": "USD", "url": p["buy"],
              "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(OFFER["bundle_month"]), "priceCurrency": "USD", "unitText": "MONTH"}},
             {"@type": "Offer", "name": f"The Vault + {p['name']} (yearly)", "price": str(OFFER["bundle_year"]), "priceCurrency": "USD", "url": p["buy"],
              "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(OFFER["bundle_year"]), "priceCurrency": "USD", "unitText": "ANN"}},
         ]},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": _plain(q), "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}} for q, a in _faq_items(p)]},
    ]


# ------------------------------------------------------------------ /exam-prep hub (names both certifiers: both disclaimers)
HUB_TITLE = "Personal Trainer Exam Prep: NASM-CPT and ACE-CPT | The Trainer's Coach"
HUB_DESCRIPTION = ("Independent practice for the NASM-CPT and ACE-CPT personal trainer exams: original practice questions, "
                   "timed mocks, concept cards and an AI study tutor. $79 each for 180 days.")


def _hub_cell(p):
    return f"""<div class="cell xp-cell"><div class="bar"></div><span class="tag live">Live · ${OFFER['price']} for {OFFER['days']} days</span>
<h3 class="h-cell">{p['name']}</h3>
<p>{p['card']}</p>
<p class="muted xp-cell-note">Written against {p['poss']} {p['outline']}.</p>
<div class="grow"></div>
<div class="btns" style="padding-top:10px"><a class="btn btn-red" href="{p['path']}">See {p['name']}</a></div>
</div>"""


HUB_BODY = (
    f"""<section class="hero dark short xp-hero">
{GRAIN}
<img class="watermark" src="/assets/jr-watermark.svg" alt="" aria-hidden="true">
<div class="wrap">
<div class="main stack" style="gap:24px;max-width:1040px">
<span class="eyebrow">The Trainer’s Coach · Vault</span>
<h1 class="h-hero"><span class="ln" style="--i:0"><span>Personal Trainer</span></span> <span class="ln" style="--i:1"><span>Exam Prep</span></span></h1>
<p class="lead">Independent practice for the NASM-CPT and ACE-CPT exams. Original questions, timed mocks, concept cards and an AI study tutor, on your phone. Pick the exam you’re sitting.</p>
</div>
</div>
</section>"""
    + sec("light", head_row("Choose your exam", "Two exams.<br>One way to study.",
                            "Both products work the same way: a diagnostic, practice weighted to the public domain percentages, "
                            "concept cards, a full timed mock and an AI study tutor. Each is $79 for 180 days, or bundled with the Vault.")
          + f'<div class="panel">{_hub_cell(NASM)}{_hub_cell(ACE)}</div>'
          + f'<p class="xp-legal xp-legal-foot">{NASM_DISCLAIMER}</p><p class="xp-legal xp-legal-foot">{ACE_DISCLAIMER}</p>')
)


def hub_schema(site):
    return [{"@type": "ItemList", "name": "Personal Trainer Exam Prep", "url": site + HUB,
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": p["name"], "url": site + p["path"]}
                                 for i, p in enumerate((NASM, ACE))]}]


# Short block for the Vault's own project page (it names both certifiers, so both disclaimers go with it).
VAULT_BLOCK = f"""<div class="split xp-vault">
<div class="main stack" style="gap:18px">
<span class="eyebrow">Also in the Vault</span>
<h2 class="h-md">Personal Trainer Exam Prep</h2>
<p class="lead">Independent practice for the NASM-CPT and ACE-CPT exams: original questions, a diagnostic, a full timed mock, concept cards and an AI study tutor. ${OFFER['price']} each for {OFFER['days']} days, or bundled with the Vault.</p>
<div class="btns"><a class="btn btn-red" href="{NASM['path']}">NASM-CPT Exam Prep</a><a class="btn btn-red" href="{ACE['path']}">ACE-CPT Exam Prep</a></div>
<p class="xp-legal">{NASM_DISCLAIMER}</p>
<p class="xp-legal">{ACE_DISCLAIMER}</p>
</div>
</div>"""

BODY = body(NASM)
ACE_BODY = body(ACE)


# ------------------------------------------------------------------ guards
def _check(text, banned, label):
    low = text.lower()
    for d in (NASM_DISCLAIMER, ACE_DISCLAIMER):
        low = low.replace(d.lower(), "")
    for w in banned:
        assert w not in low, f"{label} uses a banned phrase: {w!r}"


for _p in PRODUCTS.values():
    _faq_free = body(_p).split('<div class="faq">')[0] + _p["title"] + _p["description"] + " ".join(_p["shots"].values())
    _check(_faq_free, _BANNED + _p["banned_extra"], _p["name"])
    _b = body(_p)
    assert _b.count(_p["disclaimer"]) >= 2, _p["key"]                       # near first mention and at the foot
    assert PRODUCTS[OTHER[_p["key"]]]["disclaimer"] in _b, _p["key"]        # names the other exam, so carries its wording
    for _href in re.findall(r'class="btn btn-red" href="([^"]+)"', _b):
        assert _href == _p["buy"], (_p["key"], _href)                          # every buy button goes to its own pricing anchor
_check(HUB_BODY + VAULT_BLOCK + HUB_TITLE + HUB_DESCRIPTION, _BANNED, "Exam Prep hub / Vault block")
assert NASM_DISCLAIMER in HUB_BODY and ACE_DISCLAIMER in HUB_BODY
assert NASM_DISCLAIMER in VAULT_BLOCK and ACE_DISCLAIMER in VAULT_BLOCK
assert ACE["buy"] == "https://vault.jrstrengthandfitness.com/pricing#ace-cpt-exam-prep"
