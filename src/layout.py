"""Shared page shell for jrstrengthandfitness.com."""

SITE = "https://www.jrstrengthandfitness.com"
EMAIL = "jr@jrstrengthandfitness.com"
LINKEDIN = "https://www.linkedin.com/in/jr-prieto-romero-cscs-33850a126/"
INSTAGRAM = "https://www.instagram.com/jrstrengthandfitness/"
YOUTUBE = "https://www.youtube.com/channel/UC3gQzznf26wawqKAFj_yuzQ"
FACEBOOK = "https://www.facebook.com/jrstrengthandfitness"
VAULT = "https://vault.jrstrengthandfitness.com"
# Business mailing address for everything public (site, legal pages, Kit emails).
ADDRESS_LINES = ("JR Strength and Fitness LLC", "5441 S Macadam Ave, Suite 6590", "Portland, OR 97239")
ADDRESS = ", ".join(ADDRESS_LINES)
LOGO_W, LOGO_H = 928, 240  # set by build.py from the actual file
CSS_VER = "1"  # set by build.py: hash of styles.css, so browsers fetch the new file after each change

NAV = [
    ("/projects", "Projects", "projects"),
    ("/#standard", "The Standard", "standard"),
    ("/train", "Train with JR", "train"),
    ("/about", "About", "about"),
]

# Film-grain overlay removed: it read as rough/noisy over the dark hero.
GRAIN = ""

SCHEMA = """<script type="application/ld+json">{
 "@context":"https://schema.org","@type":"LocalBusiness",
 "name":"JR Strength and Fitness","url":"%s","email":"%s",
 "image":["%s/assets/og-jr-romero-square.jpg","%s/assets/og-jr-romero.jpg"],"logo":"%s/assets/icon-512.png",
 "founder":{"@type":"Person","name":"JR Romero","jobTitle":"Strength and Conditioning Coach, CSCS"},
 "address":{"@type":"PostalAddress","streetAddress":"5441 S Macadam Ave, Suite 6590","addressLocality":"Portland","addressRegion":"OR","postalCode":"97239","addressCountry":"US"},
 "areaServed":["Corvallis, OR","Online"],
 "sameAs":["%s","%s","%s","%s"]
}</script>""" % (SITE, EMAIL, SITE, SITE, SITE, LINKEDIN, INSTAGRAM, YOUTUBE, FACEBOOK)


CONSULT = "/consult"
# Timberhill free consult: JR's Setmore booking page (opens on the time-slot step for the consult service)
TAC_PT = "https://timberhill-personal-training.setmore.com/jrprietoromero?step=time-slot&amp;products=8aff2d32-3927-4531-a6ba-f12c9e5ab214&amp;type=service&amp;staff=91f71610-48fd-4e00-bd4e-2017f4f4a65b&amp;staffSelected=false"
G3_PT = "https://www.gthreesports.com/personal-training"
FORM_ENDPOINT = "https://formsubmit.co/ajax/jr@jrstrengthandfitness.com"


def closing_cta():
    return f"""<section class="closing" id="start" aria-label="Get started">
<img class="watermark" src="/assets/jr-watermark.svg" alt="" aria-hidden="true">
<div class="wrap">
<div class="tagline"><b>Start training yesterday.</b><span>You’ll thank yourself tomorrow.</span>
<a class="link-u" href="{VAULT}/signup" rel="noopener" data-track="Free Vault account (closing)" style="align-self:flex-start;margin-top:22px;color:#fff">Coach or trainer? Get a free Vault account →</a></div>
<div class="cta-card">
<h2 class="h-md" style="color:#121212">Ready to train?</h2>
<p>Local to Corvallis? Start with a free consult at Timberhill or G3. Anywhere else, apply for online coaching.</p>
<div class="btns" style="padding-top:4px"><a class="btn btn-red" href="{CONSULT}">Book a free consult</a><a class="mail" href="/apply">Apply for online coaching</a></div>
</div>
</div>
</section>"""


from motion import MOTION_JS  # noqa: E402
from seo import SITE_GRAPH, HOME_PAGE, OG_IMAGE  # noqa: E402


def page(*, path, title, description, body, active="", schema=False, script="", closing=True, og_type="website", head="", noindex=False, og_image=None, og_image_alt=None, og_image_size=None, **_):
    og_img = og_image or OG_IMAGE
    og_alt = og_image_alt or "JR Romero, CSCS, strength coach in Corvallis, Oregon"
    ow, oh = og_image_size or ((1200, 630) if not og_image else (None, None))
    og_dims = f'\n<meta property="og:image:width" content="{ow}">\n<meta property="og:image:height" content="{oh}">' if ow else ""
    nav = "\n".join(
        f'<a href="{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a>'
        for href, label, key in NAV
    )
    canonical = SITE + (path if path != "/" else "/")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>/* Motion on only when it can finish and the visitor hasn't asked for less. */
if('IntersectionObserver' in window && !(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches)) document.documentElement.classList.add('m');</script>
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="JR Strength &amp; Fitness">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
{'<meta name="robots" content="noindex, follow">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">'}
<meta property="og:image" content="{og_img}">
<meta property="og:image:alt" content="{og_alt}">{og_dims}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_img}">
<meta name="theme-color" content="#0a0a0a">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-96.png" sizes="96x96" type="image/png">
<link rel="icon" href="/assets/favicon-48.png" sizes="48x48" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/jost-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/jost-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts/fonts.css">
<link rel="stylesheet" href="/assets/styles.css?v={CSS_VER}">
<script>window.va=window.va||function(){{(window.vaq=window.vaq||[]).push(arguments);}};</script>
<script defer src="/_vercel/insights/script.js"></script>
{SITE_GRAPH}{HOME_PAGE if path == "/" else ""}
{head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap">
<a class="logo" href="/" aria-label="JR Strength &amp; Fitness home"><img src="/assets/jr-logo.svg" alt="JR Strength &amp; Fitness" width="845" height="268"></a>
<nav class="site-nav" aria-label="Main">
{nav}
<a class="btn btn-line" href="/projects/vault" data-track="For coaches (header)">For coaches</a>
<a class="btn btn-red" href="{CONSULT}">Book a free consult</a>
</nav>
</div>
</header>
<main id="main">
{body}
</main>
{closing_cta() if closing else ""}
<footer class="site-footer">
<div class="wrap cols">
<div class="brand">
<img src="/assets/jr-logo.svg" alt="JR Strength &amp; Fitness" width="845" height="268">
<span class="motto">Built on standards. Proven through execution.</span>
<a href="mailto:{EMAIL}" style="color:#fff">{EMAIL}</a>
<address class="addr">{"<br>".join(ADDRESS_LINES)}</address>
</div>
<nav class="col" aria-label="Projects">
<span class="head">Projects</span>
<a href="/projects/vault">Trainer’s Coach Vault</a>
<a href="/exam-prep">Exam Prep</a>
<a href="/projects/built-for-her">Built For Her™</a>
<a href="/projects/traincnd">TRAINCND</a>
<a href="/projects/credential-standard">The Credential Standard</a>
</nav>
<nav class="col" aria-label="Train">
<span class="head">Train</span>
<a href="/train">Train with JR</a>
<a href="/online-training">Online coaching</a>
<a href="/apply">Apply</a>
<a href="/about">About JR</a>
</nav>
<div class="col">
<span class="head">Train in Corvallis</span>
<span>Timberhill Athletic Club</span>
<span>G3 Sports &amp; Fitness</span>
<span>Online, anywhere</span>
</div>
<nav class="col" aria-label="Follow">
<span class="head">Follow</span>
<a href="{LINKEDIN}">LinkedIn</a>
<a href="{INSTAGRAM}">Instagram</a>
<a href="{YOUTUBE}">YouTube</a>
<a href="{FACEBOOK}">Facebook</a>
<a href="/notes">Notes from the Floor</a>
<a href="/newsletter">Newsletter</a>
<a href="/resources">Free resources</a>
</nav>
</div>
<div class="wrap legal">
<span>© 2026 JR Strength and Fitness LLC</span>
<a href="/privacy-policy">Privacy Policy</a>
<a href="/terms-of-service">Terms of Service</a>
<a href="/refund-policy">Refund Policy</a>
<a href="/accessibility">Accessibility</a>
</div>
</footer>
{MOTION_JS}
{script}
<script>
/* Button and outbound-link click tracking for Vercel Web Analytics (2 properties max per event). */
document.addEventListener('click',function(e){{
  var a=e.target.closest('a'); if(!a) return;
  var label=(a.getAttribute('data-track')||a.textContent||'').replace(/\\s+/g,' ').trim().slice(0,60);
  var url; try{{ url=new URL(a.href, location.href); }}catch(x){{ return; }}
  if(url.protocol==='mailto:'){{ window.va('event',{{name:'Email click',data:{{label:label,page:location.pathname}}}}); return; }}
  if(url.host!==location.host){{ window.va('event',{{name:'Outbound click',data:{{to:url.host+url.pathname,label:label}}}}); return; }}
  if(a.classList.contains('btn')||a.classList.contains('link-u')){{ window.va('event',{{name:'CTA click',data:{{label:label,page:location.pathname}}}}); }}
}});
</script>
</body>
</html>
"""
