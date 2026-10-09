"""Project pages: /projects and /projects/<slug>.

Facts come from each product's own live site. "Why" sections are drafts for JR to rewrite in his own words.
"""
from layout import VAULT, EMAIL, CONSULT, FORM_ENDPOINT
from ui import hero, sec, ext

PROJECTS = [
    dict(
        slug="vault",
        name="The Trainer’s Coach Vault",
        chip=("live", "Live · founding membership soon"),
        tag=("live", "Live"),
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
        name="Built For Her™",
        chip=("live", "Live · 7-day free trial"),
        tag=("live", "Live · free trial"),
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
            "The Built For Her™ Score: training, fuel and standards over seven days",
        ],
        why="Most fitness apps for women are content libraries. Built For Her™ is a training system: the same structure, progression and coaching standard I use with clients on the floor, built into an app.",
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
        tag=("", "In pilot"),
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
        cta=("Join the waitlist", "#waitlist"),
        cta2=("Visit traincnd.com", "https://traincnd.com"),
        waitlist="Get an email when TRAINCND opens to new coaches and gyms.",
    ),
    dict(
        slug="credential-standard",
        name="The Credential Standard",
        chip=("dev", "In development"),
        tag=("", "In development"),
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
        cta=("Join the waitlist", "#waitlist"),
        cta2=None,
        waitlist="Get an email when The Credential Standard opens, for coaches and for gyms that hire.",
    ),
]

BY_SLUG = {p["slug"]: p for p in PROJECTS}


def cell(p, heading="h3"):
    cls, tag = p["tag"]
    return f"""<a class="cell" href="/projects/{p['slug']}">
<div class="bar"></div>
<div class="top"><{heading} class="h-cell">{p['name']}</{heading}><span class="tag {cls}">{tag}</span></div>
<p>{p['card']}</p>
<div class="grow"></div>
<span class="more">Learn more</span>
</a>"""


def panel():
    return f'<div class="panel">{"".join(cell(p) for p in PROJECTS)}</div>'


FOR_ROW = """<div class="for-row"><span class="eyebrow">Built for</span><span>Trainers &amp; coaches</span><span>Women who lift</span><span>Coaching businesses</span><span>Gyms that hire</span></div>"""


def next_step(p, btns):
    return f"""<div class="main stack"><span class="eyebrow">Next step</span><h2 class="h-md">{p['cta'][0]}</h2><p class="body">{p['tagline']}</p><div class="btns">{btns}</div></div>"""


def waitlist_block(p):
    name = p["name"]
    return f"""<div class="main stack" id="waitlist"><span class="eyebrow">Waitlist</span><h2 class="h-md">Be first in.</h2><p class="body">{p['waitlist']}</p>
<form class="inline-form" novalidate data-form="waitlist" data-done="You’re on the list. You’ll get an email when {name} opens.">
<input type="hidden" name="_subject" value="Waitlist signup: {name}">
<input type="hidden" name="project" value="{name}">
<input type="hidden" name="_autoresponse" value="You’re on the {name} waitlist. I’ll email you as soon as it opens. JR Prieto-Romero, JR Strength &amp; Fitness">
<div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
<label class="sr" for="wl-{p['slug']}">Email address</label>
<input id="wl-{p['slug']}" type="email" name="email" placeholder="you@example.com" autocomplete="email" required>
<button class="btn btn-red" type="submit">Join the waitlist</button>
<div class="form-status" role="status" hidden></div>
</form></div>"""


def project_page(p):
    i = PROJECTS.index(p)
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    btns = f'<a class="btn btn-red" href="{p["cta"][1]}"{ext(p["cta"][1])}>{p["cta"][0]}</a>'
    if p["cta2"]:
        btns += f'<a class="link-u" href="{p["cta2"][1]}"{ext(p["cta2"][1])}>{p["cta2"][0]} →</a>'
    status = "".join(f'<div class="it"><b>{t}</b><span>{d}</span></div>' for t, d in p["status"])
    side = f'<div class="info-card"><span class="k">Where it stands</span>{status}</div>'
    iaoe = f'<p class="body"><strong style="color:var(--fg)">IAOE · </strong>{p["iaoe"]}</p>' if p["iaoe"] else ""
    return (
        hero(f"Project · {p['audience']}", p["name"], p["tagline"], btns, side, short=True, size="h-display")
        + sec("light", f"""<div class="split top">
<div class="main stack"><span class="eyebrow">What it is</span><p style="font-size:clamp(21px,2.1vw,26px);line-height:1.5;color:var(--fg)">{p['what']}</p></div>
<div class="side"><span class="eyebrow" style="padding-bottom:18px">What’s inside</span><ul class="ticks">{"".join(f"<li>{x}</li>" for x in p["inside"])}</ul></div>
</div>""")
        + sec("dark", f"""<div class="split top">
<div class="side stack" style="gap:18px"><span class="eyebrow">From the floor</span><h2 class="h-display">Why I built it</h2></div>
<div class="main stack"><p class="quote">{p['why']}</p>{iaoe}<p class="muted">JR Prieto-Romero, CSCS</p></div>
</div>""")
        + sec("gray", f"""<div class="split">
{waitlist_block(p) if p.get('waitlist') else next_step(p, btns)}
<div class="side"><a class="cell" href="/projects/{nxt['slug']}" style="border:1px solid var(--line)"><div class="bar"></div><span class="tag">Next project</span><h3 class="h-cell">{nxt['name']}</h3><p>{nxt['card']}</p><span class="more">See it</span></a></div>
</div>""", mark=False)
    )


def projects_index():
    return (
        hero("Projects", "Four projects.<br>One coaching standard.",
             "Each one started as a problem I kept solving by hand at Timberhill Athletic Club or G3. Now they’re tools any coach, athlete or gym can use.",
             '<a class="link-u" href="#list">See the projects ↓</a>', short=True, size="h-display")
        + sec("light", panel() + FOR_ROW, id="list")
    )
