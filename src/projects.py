"""Project pages: /projects and /projects/<slug>.

Facts come from each product's own live site. "Why" sections are drafts for JR to rewrite in his own words.
"""
from layout import VAULT, EMAIL

PROJECTS = [
    dict(
        slug="vault",
        name="The Trainer’s Coach Vault",
        chip=("live", "Live · founding membership soon"),
        audience="For trainers &amp; coaches",
        tagline="The operating library for professional trainers and coaches.",
        card="Consultation systems, programming frameworks and client-management tools built from real coaching practice.",
        what="A searchable, versioned library of systems, methods, frameworks, templates, tools, SOPs and AI workflows from hands-on coaching work. It isn’t a certification and it isn’t a consumer fitness app.",
        inside=[
            "34 systems and frameworks, 26 tools and 11 workflows",
            "Initial Consultation System, Hypertrophy Progression Framework, JR Coaching Audit Method",
            "Every resource states the problem it solves, who it’s for and how to implement it",
            "Versioned and updated as methods evolve",
        ],
        why="Most coaches build their consultation process, programming model and client systems from scratch, on their own. I’ve built and refined mine across two facilities. The Vault packages them so a working coach can put them to use this week.",
        iaoe="IAOE runs through the Vault’s frameworks, so coaches can match the intervention to the client in front of them.",
        status=[
            ("Free account", "Open now: selected resources, previews, search and saved favorites."),
            ("Founding membership", "Opens soon: $29/month or $249/year for the full library."),
        ],
        cta=("Create a free account", VAULT + "/signup"),
        cta2=("Explore resources", VAULT + "/explore"),
    ),
    dict(
        slug="built-for-her",
        name="Built For Her",
        chip=("live", "Live · 7-day free trial"),
        audience="For women 18+",
        tagline="Strength training built for women. Stronger by design.",
        card="A coach-built training app for women: structured programs, set-by-set logging, nutrition targets and progress tracking.",
        what="A coach-built training app for women. Programs are organized into phases, weeks and workouts, with a target for every set, technique videos for every lift, and nutrition that matches the training.",
        inside=[
            "Coach-built programs organized into phases, weeks and workouts",
            "Set-by-set logging with suggested targets and coach cues",
            "Demo videos and the reasoning behind every exercise",
            "Calorie and macro targets with meal logging",
            "Progress tracking: body weight, strength, measurements, PRs and private photos",
            "The Built For Her Score: training, fuel and standards over seven days",
        ],
        why="Most fitness apps for women are content libraries. Built For Her is a training system: the same structure, progression and coaching standard I use with clients on the floor, built into an app.",
        iaoe="",
        status=[
            ("App Access · $19.99/mo", "Self-guided training."),
            ("Membership · $49.99/mo", "Adds the community, Learning Hub, courses and challenges."),
            ("Coaching · $249/mo", "Adds a dedicated coach, weekly check-ins and program adjustments."),
        ],
        cta=("Start your free trial", "https://app.builtforher.io/pricing"),
        cta2=("Visit builtforher.io", "https://www.builtforher.io"),
    ),
    dict(
        slug="traincnd",
        name="TRAINCND",
        chip=("dev", "In pilot · signups soon"),
        audience="For coaches &amp; training businesses",
        tagline="The all-in-one operating platform for modern fitness coaches and training businesses.",
        card="One platform to run a coaching business, from the first invitation to the season’s last session.",
        what="One platform to run a coaching business, from the first invitation to the season’s last session: onboarding, programming, scheduling, check-ins and coach communication in one place.",
        inside=[
            "Client onboarding and intake",
            "Program building and scheduling",
            "Readiness check-ins and progress tracking",
            "Coach messaging and a review queue for what needs attention",
            "Plans and billing for your business",
        ],
        why="I run personal training across two facilities, with coaches who work at one location or both. TRAINCND is the system I wanted for that: every client, program and coach in one place, held to one coaching standard.",
        iaoe="",
        status=[
            ("Pilot", "Running now with a small group."),
            ("Signups", "Open soon. TRAINCND isn’t taking new gyms just yet."),
        ],
        cta=("Visit traincnd.com", "https://traincnd.com"),
        cta2=("Ask about the pilot", f"mailto:{EMAIL}?subject=TRAINCND%20pilot"),
    ),
    dict(
        slug="credential-standard",
        name="The Credential Standard",
        chip=("dev", "In development"),
        audience="For coaches, trainers &amp; fitness employers",
        tagline="The reference for professional fitness credentials.",
        card="Which fitness credentials are accredited, what they require and what renewal takes, with every fact cited to its source.",
        what="An independent register of fitness and coaching credentials: who issues them, whether they’re accredited, what the exam and prerequisites are, and what renewal and CEUs take. Every fact is cited to its source.",
        inside=[
            "Accreditation checked against accreditor directories such as NCCA and NBHWC",
            "CEU and renewal requirements from official sources",
            "Side-by-side credential comparisons",
            "Verification status based on official provider pages, not marketing claims",
            "Organization Mode: set role standards, track staff credentials and renewals, and review candidates",
        ],
        why="I hire and manage trainers across two facilities. Telling an accredited certification from a weekend certificate means digging through marketing pages. The Credential Standard does that digging once, with sources, for every coach and employer.",
        iaoe="Organizations define role standards, such as Personal Trainer or Performance Coach, the same distinctions IAOE draws between coach types.",
        status=[
            ("Credential register", "In development."),
            ("Organization pilots", "Coming for gyms and training businesses."),
        ],
        cta=("Get notified at launch", f"mailto:{EMAIL}?subject=The%20Credential%20Standard"),
        cta2=None,
    ),
]

BY_SLUG = {p["slug"]: p for p in PROJECTS}


def chip(p):
    cls, text = p["chip"]
    return f'<span class="chip {cls}">{text}</span>'


def card(p, heading="h3"):
    return f"""<a class="card" href="/projects/{p['slug']}">
{chip(p)}
<{heading} class="h-card">{p['name']}</{heading}>
<div class="rule sm"></div>
<p class="intro">{p['card']}</p>
<span class="eyebrow">{p['audience']}</span>
<div class="grow"></div>
<span class="link-arrow">Learn more <span>→</span></span>
</a>"""


def ext(href):
    return "" if href.startswith(("/", "mailto:")) else ' rel="noopener"'


def project_page(p):
    i = PROJECTS.index(p)
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    inside = "".join(f"<li>{x}</li>" for x in p["inside"])
    status = "".join(
        f'<div class="card" style="gap:8px"><h3 class="h-card it" style="font-size:20px">{t}</h3><p class="muted">{d}</p></div>'
        for t, d in p["status"]
    )
    iaoe = (
        f'<p class="intro" style="color:#fff"><strong style="font-style:normal;color:var(--red)">IAOE · </strong>{p["iaoe"]}</p>'
        if p["iaoe"] else ""
    )
    cta2 = (
        f'<a class="btn btn-ghost" href="{p["cta2"][1]}"{ext(p["cta2"][1])}>{p["cta2"][0]}</a>' if p["cta2"] else ""
    )
    return f"""
<section class="wrap" style="padding-top:72px;padding-bottom:56px">
<div class="stack center" style="gap:22px">
<div class="btns" style="gap:10px;justify-content:center">{chip(p)}<span class="chip">{p['audience']}</span></div>
<h1 class="h-page">{p['name']}</h1>
<div class="rule"></div>
<p class="lead">{p['tagline']}</p>
<div class="btns" style="padding-top:8px">
<a class="btn btn-red" href="{p['cta'][1]}"{ext(p['cta'][1])}>{p['cta'][0]}</a>
{cta2}
</div>
</div>
</section>

<section class="wrap" style="padding-bottom:40px">
<div class="grid wide">
<article class="card" style="gap:16px">
<h2 class="h-card it">What it is</h2>
<div class="rule sm"></div>
<p>{p['what']}</p>
</article>
<article class="card" style="gap:16px">
<h2 class="h-card it">What’s inside</h2>
<div class="rule sm"></div>
<ul class="dots plain">{inside}</ul>
</article>
</div>
</section>

<section class="wrap section">
<div class="split" style="align-items:flex-start">
<div class="side stack" style="gap:14px">
<h2 class="h-section">Why I built it</h2>
<div class="rule"></div>
</div>
<div class="main prose">
<p style="font-size:20px;color:#fff">{p['why']}</p>
{iaoe}
<p class="muted">— JR Prieto-Romero, CSCS</p>
</div>
</div>
</section>

<section class="wrap section">
<div class="stack" style="gap:28px">
<h2 class="h-section" style="text-align:center">Where it stands</h2>
<div class="rule" style="align-self:center"></div>
<div class="grid">{status}</div>
</div>
</section>

<section class="wrap section" style="padding-bottom:104px">
<div class="split">
<div class="main card stack center" style="gap:18px;padding:40px">
<h2 class="h-card it">{p['name']}</h2>
<p class="muted">{p['tagline']}</p>
<div class="btns"><a class="btn btn-red" href="{p['cta'][1]}"{ext(p['cta'][1])}>{p['cta'][0]}</a></div>
</div>
<a class="side card" href="/projects/{nxt['slug']}" style="padding:32px">
<span class="eyebrow">Next project</span>
<h2 class="h-card">{nxt['name']}</h2>
<span class="link-arrow">See it <span>→</span></span>
</a>
</div>
</section>
"""


def projects_index():
    feature = PROJECTS[0]
    rest = "".join(card(p) for p in PROJECTS[1:])
    return f"""
<section class="wrap section"><div class="stack center">
<h1 class="h-page">Projects</h1><div class="rule"></div>
<p class="intro">Four projects, one coaching standard. Each one started as a problem I kept solving by hand at TAC or G3.</p>
</div></section>
<section class="wrap" style="padding-bottom:104px">
<div class="stack" style="gap:20px">
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr))">{card(feature)}{rest}</div>
</div>
</section>
"""
