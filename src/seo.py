"""Search and AI-search structured data, FAQ content, robots.txt and llms.txt.

Every fact here is already stated on the site (or by JR). Keep them in sync with the pages.
"""
import html
import json

from layout import SITE, EMAIL, LINKEDIN, INSTAGRAM, YOUTUBE, FACEBOOK, ADDRESS_LINES

OG_IMAGE = f"{SITE}/assets/og-jr.jpg"
PORTRAIT = f"{SITE}/assets/photos/jr-portrait.webp"
PERSON_ID = f"{SITE}/#jr"
ORG_ID = f"{SITE}/#org"
SAME_AS = [LINKEDIN, INSTAGRAM, YOUTUBE, FACEBOOK]

PERSON = {
    "@type": "Person", "@id": PERSON_ID, "name": "JR Prieto-Romero", "alternateName": ["JR Romero", "JR Romero, CSCS"],
    "givenName": "JR", "familyName": "Prieto-Romero",
    "url": f"{SITE}/about", "image": PORTRAIT,
    "jobTitle": "Director of Training, Timberhill Athletic Club; Director of Personal Training and Performance, G3 Sports & Fitness",
    "description": "Strength and conditioning coach (CSCS) in Corvallis, Oregon, with roughly 20,000 hours of coaching. "
                   "Builder of The Trainer's Coach Vault, Built For Her, TRAINCND and The Credential Standard.",
    "worksFor": [{"@type": "SportsActivityLocation", "name": "Timberhill Athletic Club", "address": {"@type": "PostalAddress", "addressLocality": "Corvallis", "addressRegion": "OR", "addressCountry": "US"}},
                 {"@type": "SportsActivityLocation", "name": "G3 Sports & Fitness", "address": {"@type": "PostalAddress", "addressLocality": "Corvallis", "addressRegion": "OR", "addressCountry": "US"}}],
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
    "sameAs": SAME_AS,
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
    "description": "Individualized online training and nutrition coaching with JR Prieto-Romero, CSCS: assess, build, execute, refine. Every package includes training and nutrition.",
    "offers": [_monthly("Essentials Coaching", 129), _monthly("Core Coaching", 179), _monthly("Premium Coaching", 249)],
}
IN_PERSON_SERVICE = {
    "@type": "Service", "name": "Personal training in Corvallis, Oregon", "serviceType": "Personal training",
    "provider": {"@id": PERSON_ID}, "url": f"{SITE}/train",
    "areaServed": {"@type": "City", "name": "Corvallis", "containedInPlace": {"@type": "State", "name": "Oregon"}},
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
     "Essentials is $129 a month, Core is $179 a month and Premium is $249 a month. Three- and six-month terms lower the monthly rate. "
     "Every package includes both training and nutrition coaching."),
    ("Who is JR Prieto-Romero?",
     "JR Prieto-Romero, CSCS, known on the floor as JR Romero, is Director of Training at Timberhill Athletic Club and Director of Personal Training and Performance at "
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
    proj = "\n".join(f"- [{_plain(p['name'])}]({SITE}/projects/{p['slug']}): {_plain(p['card'])}" for p in projects)
    writing = "\n".join(f"- [{p['title']}]({SITE}/writing/{p['slug']}): {p['excerpt']}" for p in posts)
    faq = "\n\n".join(f"### {_plain(q)}\n{_plain(a)}" for q, a in FAQ)
    return f"""# JR Strength & Fitness

> JR Prieto-Romero, CSCS (known professionally as JR Romero), is a strength and conditioning coach in Corvallis, Oregon: Director of Training at Timberhill Athletic Club and Director of Personal Training and Performance at G3 Sports & Fitness. He coaches in person in Corvallis and online, and builds tools for coaches and athletes.

- Credentials: Certified Strength and Conditioning Specialist (CSCS); B.S. in Exercise & Sport Science, Oregon State University; roughly 20,000 hours of coaching.
- Coaching standard: IAOE (Inadequate, Adequate, Optimal, Enhanced). Match the intervention to the person; adequate is a legitimate target.
- Contact: {EMAIL}

## Train with JR

- [Train with JR]({SITE}/train): in-person personal training in Corvallis at Timberhill Athletic Club or G3 Sports & Fitness. Every client starts with a free 30-minute consult; no membership needed.
- [Book a free consult]({SITE}/consult): choose Timberhill (health, fitness, longevity) or G3 (youth development, adult performance, tactical and teams).
- [Online coaching]({SITE}/online-training): individualized training and nutrition. Essentials $129/month, Core $179/month, Premium $249/month; 3- and 6-month terms lower the rate.
- [Apply for online coaching]({SITE}/apply): JR replies within 2 business days; if it's a fit, a short call, then the coaching app invite.

## Projects

{proj}

## Writing

{writing}

## FAQ

{faq}

## Optional

- [About JR]({SITE}/about)
- [Newsletter]({SITE}/newsletter)
- [LinkedIn]({LINKEDIN})
- [Instagram]({INSTAGRAM})
"""
