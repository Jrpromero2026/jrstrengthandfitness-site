"""Search and AI-search structured data, FAQ content, robots.txt and llms.txt.

Every fact here is already stated on the site (or by JR). Keep them in sync with the pages.
"""
import html
import json

from layout import SITE, EMAIL, LINKEDIN, INSTAGRAM, YOUTUBE, FACEBOOK, ADDRESS_LINES

OG_IMAGE = f"{SITE}/assets/og-jr-romero.jpg"
PORTRAIT = f"{SITE}/assets/photos/jr-portrait.webp"
PERSON_ID = f"{SITE}/#jr"
ORG_ID = f"{SITE}/#org"
G3_BIO = "https://www.gthreesports.com/coaches/jr-romero"
SAME_AS = [LINKEDIN, INSTAGRAM, YOUTUBE, FACEBOOK, G3_BIO]

# Facility addresses: Timberhill from its Setmore booking page; G3 from its Google listing (Oct 2026).
TAC_PLACE = {"@type": "SportsActivityLocation", "name": "Timberhill Athletic Club", "url": "https://timberhillac.com/",
             "hasMap": "https://www.google.com/maps/search/?api=1&query=Timberhill+Athletic+Club&query_place_id=ChIJPSGRNnI_wFQR961D-CQzDxg",
             "address": {"@type": "PostalAddress", "streetAddress": "2855 NW 29th St", "addressLocality": "Corvallis", "addressRegion": "OR", "postalCode": "97330", "addressCountry": "US"}}
G3_PLACE = {"@type": "SportsActivityLocation", "name": "G3 Sports & Fitness", "url": "https://www.gthreesports.com/",
            "hasMap": "https://www.google.com/maps/search/?api=1&query=G3+Sports+%26+Fitness&query_place_id=ChIJIaXvKtY_wFQRP2aDGqS60kE",
            "telephone": "+1-541-207-3508", "address": {"@type": "PostalAddress", "streetAddress": "5520 NW Highway 99W", "addressLocality": "Corvallis", "addressRegion": "OR", "postalCode": "97330", "addressCountry": "US"}}

PERSON = {
    "@type": "Person", "@id": PERSON_ID, "name": "JR Romero", "alternateName": ["JR Romero, CSCS", "JR Prieto-Romero", "JR Prieto-Romero, CSCS"],
    "givenName": "JR", "familyName": "Prieto-Romero",
    "url": f"{SITE}/about", "image": PORTRAIT,
    "jobTitle": "Director of Personal Training, Timberhill Athletic Club; Director of Performance, G3 Sports & Fitness",
    "description": "Strength and conditioning coach (CSCS) in Corvallis, Oregon, with roughly 20,000 hours of coaching. "
                   "Builder of The Trainer's Coach Vault, Built For Her, TRAINCND and The Credential Standard.",
    "worksFor": [TAC_PLACE, G3_PLACE],
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Oregon State University"},
    "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "name": "Certified Strength and Conditioning Specialist (CSCS)",
         "credentialCategory": "certification", "recognizedBy": {"@type": "Organization", "name": "National Strength and Conditioning Association"}},
        {"@type": "EducationalOccupationalCredential", "name": "B.S., Exercise and Sport Science", "credentialCategory": "degree",
         "recognizedBy": {"@type": "CollegeOrUniversity", "name": "Oregon State University"}},
    ],
    "knowsAbout": ["Strength and conditioning", "Personal training", "Hypertrophy training", "Youth athletic development",
                   "Strength training for women", "Online coaching", "Coaching systems and consultations"],
    "homeLocation": {"@type": "Place", "name": "Corvallis, Oregon"},
    "hasOccupation": [
        {"@type": "Occupation", "name": "Personal trainer", "occupationLocation": {"@type": "City", "name": "Corvallis, Oregon"}},
        {"@type": "Occupation", "name": "Strength and conditioning coach", "occupationLocation": {"@type": "City", "name": "Corvallis, Oregon"}},
    ],
    "sameAs": [u for u in SAME_AS if u != G3_BIO],
}
ORG = {
    "@type": "Organization", "@id": ORG_ID, "name": "JR Strength and Fitness LLC", "alternateName": "JR Strength & Fitness",
    "url": SITE + "/", "email": EMAIL, "logo": f"{SITE}/assets/jr-logo.png", "image": OG_IMAGE,
    "founder": {"@id": PERSON_ID},
    "address": {"@type": "PostalAddress", "streetAddress": ADDRESS_LINES[1], "addressLocality": "Portland",
                "addressRegion": "OR", "postalCode": "97239", "addressCountry": "US"},
    "sameAs": SAME_AS,
}
WEBSITE = {"@type": "WebSite", "@id": f"{SITE}/#site", "name": "JR Strength & Fitness", "url": SITE + "/",
           "publisher": {"@id": ORG_ID}, "inLanguage": "en-US"}


def ld(*nodes):
    data = {"@context": "https://schema.org", "@graph": list(nodes)}
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


SITE_GRAPH = ld(WEBSITE, ORG, PERSON)


def breadcrumbs(trail):
    """trail: [(name, path), ...] ending with the current page."""
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(trail)]}


# ---------------------------------------------------------------- Services
def _monthly(name, price):
    return {"@type": "Offer", "name": name, "price": str(price), "priceCurrency": "USD",
            "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(price), "priceCurrency": "USD",
                                   "unitText": "MONTH", "billingDuration": "P1M"},
            "url": f"{SITE}/apply"}


ONLINE_SERVICE = {
    "@type": "Service", "name": "Online training and nutrition coaching", "serviceType": "Online personal training",
    "provider": {"@id": PERSON_ID}, "url": f"{SITE}/online-training",
    "description": "Individualized online training and nutrition coaching with JR Romero, CSCS: assess, build, execute, refine. Every package includes training and nutrition.",
    "offers": [_monthly("Essentials Coaching", 199), _monthly("Core Coaching", 249), _monthly("Premium Coaching", 319)],
}
IN_PERSON_SERVICE = {
    "@type": "Service", "name": "Personal training in Corvallis, Oregon", "serviceType": "Personal training",
    "provider": {"@id": PERSON_ID}, "url": f"{SITE}/train",
    "areaServed": [{"@type": "City", "name": "Corvallis", "containedInPlace": {"@type": "State", "name": "Oregon"}},
                   {"@type": "City", "name": "Albany"}, {"@type": "City", "name": "Philomath"}],
    "availableChannel": [{"@type": "ServiceChannel", "name": f"Personal training at {pl['name']}", "serviceLocation": pl,
                          "serviceUrl": f"{SITE}/consult"} for pl in (TAC_PLACE, G3_PLACE)],
    "description": "In-person personal training at Timberhill Athletic Club and G3 Sports & Fitness in Corvallis. Every client starts with a free 30-minute consult; no membership needed.",
    "offers": {"@type": "Offer", "name": "Free 30-minute consult", "price": "0", "priceCurrency": "USD", "url": f"{SITE}/consult"},
}

# ---------------------------------------------------------------- FAQ (shown on /train, and as FAQPage data)
FAQ = [
    ("How do I start personal training with JR in Corvallis?",
     "Book a free 30-minute consult at Timberhill Athletic Club or G3 Sports &amp; Fitness. We cover your goals, training history, "
     "limitations, barriers and preferences, then I match you with the right coach, facility and program. Sometimes that coach isn’t me."),
    ("Do I need a gym membership to book a consult?",
     "No. You don’t need to be a member of Timberhill or G3 to book a free consult."),
    ("Should I train at Timberhill Athletic Club or G3 Sports &amp; Fitness?",
     "Timberhill is built around health, general fitness and longevity for adults at every starting point. G3 focuses on youth athletic "
     "development, adult human performance, and tactical, team and organization training. Not sure? Pick either one; one consult covers both."),
    ("Can I train with JR if I don’t live in Corvallis?",
     "Yes. Online coaching gives you individualized training and nutrition through the coaching app, with check-ins and adjustments. "
     "It starts with an application: I reply within 2 business days, and if it’s a fit we do a short call before you get your app invite."),
    ("How much does online coaching cost?",
     "Essentials is $199 a month, Core is $249 a month and Premium is $319 a month. Three- and six-month terms lower the monthly rate. "
     "Every package includes both training and nutrition coaching."),
    ("Do you train beginners?",
     "Yes. Plenty of my clients had never worked with a trainer. We start with technique and a plan you can follow on your own schedule."),
    ("Can you help me get strong again after an injury?",
     "Yes. Once rehab is done, I build a plan around the injury that rebuilds strength and confidence, progressed as you’re ready."),
    ("Do you train high school and college athletes?",
     "Yes, at G3 Sports &amp; Fitness: strength, speed and conditioning for athletes heading into college sport. Athletes I’ve coached have "
     "gone on to play at the University of Oregon, the University of Nevada, George Fox, Houston Christian, Saint Anselm and Eastern Illinois."),
    ("Where are the sessions?",
     "In person at Timberhill Athletic Club, 2855 NW 29th St, or G3 Sports &amp; Fitness, 5520 NW Highway 99W, both in Corvallis. "
     "Online coaching works anywhere."),
    ("Who is JR Romero?",
     "JR Romero, CSCS, is Director of Personal Training at Timberhill Athletic Club and Director of Performance at "
     "G3 Sports &amp; Fitness in Corvallis, Oregon. He earned his degree in Exercise &amp; Sport Science at Oregon State and has roughly "
     "20,000 hours of coaching on the floor."),
]


def _plain(s):
    return html.unescape(s)


FAQ_LD = {"@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": _plain(q), "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}} for q, a in FAQ]}


def faq_html():
    items = "".join(f'<details class="faq-q"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    return f'<div class="faq">{items}</div>'


# ---------------------------------------------------------------- Projects
def project_ld(p):
    kinds = {"vault": "WebApplication", "built-for-her": "MobileApplication", "traincnd": "WebApplication",
             "credential-standard": "WebApplication"}
    node = {"@type": kinds.get(p["slug"], "SoftwareApplication"), "name": _plain(p["name"]),
            "description": _plain(p["what"]), "url": f"{SITE}/projects/{p['slug']}",
            "applicationCategory": "HealthApplication" if p["slug"] == "built-for-her" else "BusinessApplication",
            "creator": {"@id": PERSON_ID}, "publisher": {"@id": ORG_ID}}
    if p["slug"] == "vault":
        node["offers"] = {"@type": "Offer", "name": "Free account", "price": "0", "priceCurrency": "USD"}
    if p["slug"] == "built-for-her":
        node["offers"] = [_monthly("App Access", "19.99"), _monthly("Membership", "49.99"), _monthly("Coaching", "249")]
        for o in node["offers"]:
            o["url"] = "https://app.builtforher.io/pricing"
        node["operatingSystem"] = "iOS, Android, Web"
    return node


# ---------------------------------------------------------------- robots.txt and llms.txt
AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
           "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot"]


def robots_txt():
    bots = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in AI_BOTS)
    return f"# Search engines and AI assistants are welcome to read and cite this site.\n\nUser-agent: *\nAllow: /\n\n{bots}Sitemap: {SITE}/sitemap.xml\n"


def llms_txt(projects, posts):
    import examprep as XP
    proj = "\n".join(f"- [{_plain(p['name'])}]({SITE}/projects/{p['slug']}): {_plain(p['card'])}" for p in projects)
    writing = "\n".join(f"- [{p['title']}]({SITE}/notes/{p['slug']}): {p['excerpt']}" for p in posts)
    faq = "\n\n".join(f"### {_plain(q)}\n{_plain(a)}" for q, a in FAQ)
    xp_lines = "\n".join(
        f"- [{p['name']}]({SITE}{p['path']}): {p['llms']} (up to 15 questions a day; its answers can be wrong). "
        f"$79 one-time for 180 days, no auto-renewal, or $39/month or $299/year bundled with the Vault. Sold at {p['buy']}. "
        f"No pass guarantee; Practice Readiness is a study signal, not a score or prediction.\n- {p['disclaimer']}"
        for p in (XP.NASM, XP.ACE))
    return f"""# JR Strength & Fitness

> JR Romero, CSCS (full name JR Prieto-Romero), is a strength and conditioning coach in Corvallis, Oregon: Director of Personal Training at Timberhill Athletic Club and Director of Performance at G3 Sports & Fitness. Founder of four coaching products. He coaches in person in Corvallis and online, and builds tools for coaches and athletes.

- Credentials: Certified Strength and Conditioning Specialist (CSCS); B.S. in Exercise & Sport Science, Oregon State University; roughly 20,000 hours of coaching.
- Coaching standard: IAOE (Inadequate, Adequate, Optimal, Enhanced). Match the intervention to the person; adequate is a legitimate target.
- Contact: {EMAIL}

## Train with JR

- [Train with JR]({SITE}/train): in-person personal training in Corvallis at Timberhill Athletic Club or G3 Sports & Fitness. Every client starts with a free 30-minute consult; no membership needed.
- Who JR trains in person: people rebuilding strength after an injury, adults 50 and up, endurance athletes, high school and college athletes (at G3), and first-time lifters.
- Leave a review: {SITE}/review (Google reviews of the gyms: {SITE}/review/timberhill and {SITE}/review/g3).
- [Book a free consult]({SITE}/consult): choose Timberhill (health, fitness, longevity) or G3 (youth development, adult performance, tactical and teams).
- [Online coaching]({SITE}/online-training): individualized training and nutrition. Essentials $199/month, Core $249/month, Premium $319/month; 3- and 6-month terms lower the rate.
- [Apply for online coaching]({SITE}/apply): JR replies within 2 business days; if it's a fit, a short call, then the coaching app invite.

## Projects

{proj}

### Personal Trainer Exam Prep (part of The Trainer's Coach Vault)

- [Personal Trainer Exam Prep]({SITE}{XP.HUB}): lists both exam-prep products.
{xp_lines}

## Notes from the Floor (articles)

{writing}

## FAQ

{faq}

## Optional

- [About JR]({SITE}/about)
- [Newsletter]({SITE}/newsletter)
- [LinkedIn]({LINKEDIN})
- [Instagram]({INSTAGRAM})
"""
