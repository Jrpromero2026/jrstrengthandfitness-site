"""Shared page shell for jrstrengthandfitness.com."""

SITE = "https://www.jrstrengthandfitness.com"
EMAIL = "jr@jrstrengthandfitness.com"
LINKEDIN = "https://www.linkedin.com/in/jr-prieto-romero-cscs-33850a126/"
INSTAGRAM = "https://www.instagram.com/jrstrengthandfitness/"
YOUTUBE = "https://www.youtube.com/channel/UC3gQzznf26wawqKAFj_yuzQ"
FACEBOOK = "https://www.facebook.com/jrstrengthandfitness"
VAULT = "https://vault.jrstrengthandfitness.com"
LOGO_W, LOGO_H = 928, 240  # set by build.py from the actual file
CSS_VER = "1"  # set by build.py: hash of styles.css, so browsers fetch the new file after each change

NAV = [
    ("/projects", "Projects", "projects"),
    ("/#standard", "The Standard", "standard"),
    ("/train", "Train with JR", "train"),
    ("/about", "About", "about"),
]

GRAIN = (
    '<svg class="grain" aria-hidden="true" focusable="false">'
    '<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/>'
    '<feColorMatrix type="saturate" values="0"/></filter>'
    '<rect width="100%" height="100%" filter="url(#grain)"/></svg>'
)

SCHEMA = """<script type="application/ld+json">{
 "@context":"https://schema.org","@type":"LocalBusiness",
 "name":"JR Strength and Fitness","url":"%s","email":"%s",
 "image":"%s/assets/og-image.png",
 "founder":{"@type":"Person","name":"JR Prieto-Romero","jobTitle":"Strength and Conditioning Coach, CSCS"},
 "address":{"@type":"PostalAddress","streetAddress":"862 SW Adams Ave","addressLocality":"Corvallis","addressRegion":"OR","postalCode":"97333","addressCountry":"US"},
 "areaServed":["Corvallis, OR","Online"],
 "sameAs":["%s","%s","%s","%s"]
}</script>""" % (SITE, EMAIL, SITE, LINKEDIN, INSTAGRAM, YOUTUBE, FACEBOOK)


CONSULT = "/consult"
TAC_PT = "https://timberhillac.com/programs/personal-training"
G3_PT = "https://www.gthreesports.com/personal-training"
FORM_ENDPOINT = "https://formsubmit.co/ajax/jr@jrstrengthandfitness.com"


def closing_cta():
    return f"""<section class="closing" id="start" aria-label="Get started">
<img class="watermark" src="/assets/jr-watermark.png" alt="" aria-hidden="true">
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


def page(*, path, title, description, body, active="", schema=False, script="", closing=True, og_type="website", head="", **_):
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
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="JR Strength &amp; Fitness">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a0a0a">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700&amp;display=swap">
<link rel="stylesheet" href="/assets/styles.css?v={CSS_VER}">
<script>window.va=window.va||function(){{(window.vaq=window.vaq||[]).push(arguments);}};</script>
<script defer src="/_vercel/insights/script.js"></script>
{SCHEMA if schema else ""}
{head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap">
<a class="logo" href="/" aria-label="JR Strength &amp; Fitness home"><img src="/assets/jr-logo.png" alt="JR Strength &amp; Fitness" width="{LOGO_W}" height="{LOGO_H}"></a>
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
<img src="/assets/jr-logo.png" alt="JR Strength &amp; Fitness" width="{LOGO_W}" height="{LOGO_H}">
<span class="motto">Built on standards. Proven through execution.</span>
<a href="mailto:{EMAIL}" style="color:#fff">{EMAIL}</a>
</div>
<nav class="col" aria-label="Projects">
<span class="head">Projects</span>
<a href="/projects/vault">Trainer’s Coach Vault</a>
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
<a href="/writing">Writing</a>
</nav>
</div>
<div class="wrap legal">
<span>© 2026 JR Strength and Fitness LLC</span>
<a href="/privacy-policy">Privacy Policy</a>
<a href="/terms-of-service">Terms of Service</a>
<a href="/refund-policy">Refund Policy</a>
</div>
</footer>
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
