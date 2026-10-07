"""Page content for jrstrengthandfitness.com. Bracketed [text] marks copy JR still needs to supply."""

from layout import VAULT, LINKEDIN, EMAIL


def ph(text):
    """Visible placeholder for copy JR still needs to send."""
    return f'<span class="placeholder">[{text}]</span>'


def head(title, intro=None, level="h-section"):
    tag = "h1" if level != "h-section" else "h2"
    intro_html = f'<p class="intro">{intro}</p>' if intro else ""
    return f'<div class="stack center"><{tag} class="{level}">{title}</{tag}><div class="rule"></div>{intro_html}</div>'


def page_head(title, intro=None):
    """Top-of-page heading block for inner pages."""
    intro_html = f'<p class="intro">{intro}</p>' if intro else ""
    return f'<section class="wrap section"><div class="stack center"><h1 class="h-page">{title}</h1><div class="rule"></div>{intro_html}</div></section>'


# ---------------------------------------------------------------- Home
HOME = f"""
<section class="wrap" style="padding-top:88px;padding-bottom:96px">
<div class="stack center" style="gap:26px">
<h1 class="h-hero">Built on the floor.<br>Now built for coaches.</h1>
<p class="lead">I’m JR Prieto-Romero, CSCS. I direct training at Timberhill Athletic Club and lead personal training and performance at G3 Sports &amp; Fitness. After 20,000 hours coaching, I’m turning what works on the floor into tools for coaches and athletes.</p>
<div class="btns" style="padding-top:10px">
<a class="btn btn-red" href="#projects">See what I’m building</a>
<a class="btn btn-ghost" href="/train">Train with JR</a>
</div>
<div class="creds">
<span>CSCS</span><span class="dot">•</span>
<span>B.S. Exercise &amp; Sport Science, Oregon State</span><span class="dot">•</span>
<span>~20,000 coaching hours</span><span class="dot">•</span>
<span>Director of Training, TAC</span><span class="dot">•</span>
<span>Director of Personal Training &amp; Performance, G3</span>
</div>
</div>
</section>

<section id="projects" class="wrap section">
<div class="stack" style="gap:40px">
{head("What I’m building", "Four projects, one coaching standard. Each one started as a problem I kept solving by hand at TAC or G3.")}

<a class="card feature" href="{VAULT}">
<div class="main">
<span class="chip live">Live · founding rate</span>
<h3 class="h-card lg">The Trainer’s Coach Vault</h3>
<div class="rule sm"></div>
<p class="intro">The operating library for professional trainers and coaches. Consultation systems, programming frameworks and client-management tools built from real coaching practice.</p>
<span class="link-arrow">Explore the Vault <span>→</span></span>
</div>
<div class="side">
<div class="stat"><b>34</b><span>Systems &amp; frameworks</span></div>
<div class="stat"><b>26</b><span>Tools</span></div>
<div class="stat"><b>11</b><span>Workflows</span></div>
<span class="muted" style="font-size:15px">Founding membership: <strong style="color:#fff">$29/mo</strong> or <strong style="color:#fff">$249/yr</strong></span>
</div>
</a>

<div class="grid">
<article class="card" id="built-for-her">
<span class="chip dev">In development</span>
<h3 class="h-card">Built For Her</h3>
<div class="rule sm"></div>
<p class="intro">Training, nutrition and progress tracking in one app. {ph("Who it’s for, in one line")}</p>
<div class="grow"></div>
<a class="link-arrow" href="#built-for-her">{ph("Waitlist link")} <span>→</span></a>
</article>

<article class="card" id="traincnd">
<span class="chip">{ph("Status")}</span>
<h3 class="h-card">TRAINCND</h3>
<div class="rule sm"></div>
<p class="intro">{ph("One line: what TRAINCND does and who it’s for")}</p>
<div class="grow"></div>
<a class="link-arrow" href="#traincnd">{ph("Link")} <span>→</span></a>
</article>

<article class="card" id="credential-standard">
<span class="chip">{ph("Status")}</span>
<h3 class="h-card">The Credential Standard</h3>
<div class="rule sm"></div>
<p class="intro">{ph("One line: what The Credential Standard does and who it’s for")}</p>
<div class="grow"></div>
<a class="link-arrow" href="#credential-standard">{ph("Link")} <span>→</span></a>
</article>
</div>
</div>
</section>

<section id="standard" class="wrap section">
<div class="stack" style="gap:36px">
{head("The standard underneath", "Every project runs on IAOE. Adequate is a legitimate target, not a failure: safe, effective and progressing is the right outcome for many clients.")}
<div class="tiers">
<div class="tier dim"><b>I</b><span class="name">Inadequate</span><span class="who">Below the line</span></div>
<div class="tier"><b>A</b><span class="name">Adequate</span><span class="who">Fitness trainer</span></div>
<div class="tier"><b>O</b><span class="name">Optimal</span><span class="who">Fitness coach</span></div>
<div class="tier top"><b>E</b><span class="name">Enhanced</span><span class="who">Performance coach · where I coach</span></div>
</div>
</div>
</section>

<section id="train" class="wrap section">
<div class="stack" style="gap:36px">
{head("Train with JR", "Every client starts with a free 30-minute consult. From there I choose the facility, the coach and the program — sometimes that coach isn’t me.")}
<div class="grid wide">
<article class="card">
<h3 class="h-card it">In person · Corvallis</h3>
<div class="rule sm"></div>
<ul class="dots">
<li>Timberhill Athletic Club: health, fitness, longevity</li>
<li>G3: youth athletes, adult performance, tactical, teams</li>
<li>No membership required at either</li>
</ul>
<div class="grow"></div>
<div class="btns"><a class="btn btn-red" href="/apply?path=in-person">Book a free consult</a></div>
</article>
<article class="card">
<h3 class="h-card it">Online coaching</h3>
<div class="rule sm"></div>
<div class="prices">
<div class="price"><div class="tier-name">Essentials</div><div class="amt">$129<small>/mo</small></div></div>
<div class="price pick"><div class="tier-name">Core</div><div class="amt">$179<small>/mo</small></div></div>
<div class="price"><div class="tier-name">Premium</div><div class="amt">$249<small>/mo</small></div></div>
</div>
<p class="intro">Training and nutrition coaching in the app, with check-ins and adjustments.</p>
<div class="grow"></div>
<div class="btns"><a class="btn btn-ghost" href="/online-training">Compare &amp; apply</a></div>
</article>
</div>
</div>
</section>

<section id="about" class="wrap section" style="padding-bottom:104px">
<div class="split">
<div class="side"><div class="photo">{ph("Photo: JR coaching on the floor")}</div></div>
<div class="main stack" style="gap:18px">
<h2 class="h-section">About JR</h2>
<div class="rule"></div>
<p>I grew up in Salem, came to Corvallis for Oregon State and earned my degree in Exercise &amp; Sport Science. I played soccer, sprinted and threw before I ever coached.</p>
<p>Today I direct training at Timberhill Athletic Club, lead personal training and performance at G3 Sports &amp; Fitness, and coach my own clients at the Enhanced tier: trained athletes who have plateaued and want finer margins.</p>
<a class="link-arrow" href="/about">Read the full story <span>→</span></a>
</div>
</div>
</section>
"""

# ---------------------------------------------------------------- Train with JR
TRAIN = page_head(
    "Train with JR",
    "Every client starts with a free 30-minute consult with me, in person or online. You don’t need to be a member anywhere.",
) + f"""
<section class="wrap" style="padding-bottom:40px">
<div class="stack" style="gap:36px">
{head("How it works")}
<div class="steps">
<div class="card step"><h3 class="h-card it">Consult</h3><p>Thirty minutes on your goals, training history, limitations, barriers and preferences.</p></div>
<div class="card step"><h3 class="h-card it">Match</h3><p>I choose the facility, the coach and the program. Sometimes the best coach for you isn’t me.</p></div>
<div class="card step"><h3 class="h-card it">Train</h3><p>You start with a plan built for you, under the same coaching standard at both locations.</p></div>
</div>
</div>
</section>

<section class="wrap section">
<div class="stack" style="gap:36px">
{head("Where you’ll train")}
<div class="grid wide">
<article class="card">
<span class="eyebrow">In person · Corvallis</span>
<h3 class="h-card lg">Timberhill Athletic Club</h3>
<div class="rule sm"></div>
<ul class="dots">
<li>Health and general fitness</li>
<li>Longevity and staying capable</li>
<li>Adults at every starting point</li>
</ul>
</article>
<article class="card">
<span class="eyebrow">In person · Corvallis</span>
<h3 class="h-card lg">G3 Sports &amp; Fitness</h3>
<div class="rule sm"></div>
<ul class="dots">
<li>Youth athletic development</li>
<li>Adult human performance</li>
<li>Tactical, teams and organizations</li>
</ul>
</article>
</div>
<p class="intro" style="align-self:center;text-align:center">Families often split: a parent trains at TAC while their kid trains at G3. One consult covers both.</p>
</div>
</section>

<section class="wrap section">
<div class="split">
<div class="main stack" style="gap:18px">
<h2 class="h-section">Not in Corvallis?</h2>
<div class="rule"></div>
<p>Online coaching gives you individualized training and nutrition through the app, with check-ins and adjustments. Packages start at $129 a month.</p>
<div class="btns"><a class="btn btn-ghost" href="/online-training">See online coaching</a></div>
</div>
<div class="side card stack center" style="gap:18px;padding:40px">
<h3 class="h-card it">Free 30-minute consult</h3>
<p class="muted">In person or online. No commitment.</p>
<a class="btn btn-red" href="/apply?path=consult">Book a free consult</a>
</div>
</div>
</section>
"""

# ---------------------------------------------------------------- Online training
def package(name, who, features, prices, pick=False):
    feats = "".join(f"<li>{f}</li>" for f in features)
    month, three, six = prices
    return f"""<article class="card package{' pick' if pick else ''}">
<h3 class="h-card">{name}</h3>
<div class="rule sm"></div>
<p class="intro">{who}</p>
<div class="amt">${month}<small>/month</small></div>
<p class="terms">3 months: ${three[0]} (~${three[1]}/mo) · 6 months: ${six[0]} (~${six[1]}/mo)</p>
<ul class="dots plain">{feats}</ul>
<div class="grow"></div>
<div class="btns"><a class="btn {'btn-red' if pick else 'btn-ghost'}" href="/apply?path=online&amp;level={name.split()[0].lower()}">Apply for {name.split()[0]}</a></div>
</article>"""


ONLINE = page_head(
    "Online coaching",
    "You don’t need more workouts. You need structure, progression and a plan built for your life, with someone checking that it gets done.",
) + f"""
<section class="wrap" style="padding-bottom:40px">
<div class="stack" style="gap:36px">
{head("How it works")}
<div class="steps">
<div class="card step"><h3 class="h-card it">Assess</h3><p>Intake, history, schedule, goals and constraints. No assumptions.</p></div>
<div class="card step"><h3 class="h-card it">Build</h3><p>Training and nutrition structured with progression and intent.</p></div>
<div class="card step"><h3 class="h-card it">Execute</h3><p>Weekly targets, daily actions and consistent check-ins.</p></div>
<div class="card step"><h3 class="h-card it">Refine</h3><p>Data drives decisions. Results dictate change.</p></div>
</div>
</div>
</section>

<section class="wrap section">
<div class="stack" style="gap:36px">
{head("Packages", "Every package includes both training and nutrition coaching.")}
<div class="grid">
{package("Essentials Coaching", "For self-motivated clients who want expert guidance with minimal check-ins.", [
    "Customized training, updated monthly",
    "Personalized nutrition targets and habits",
    "Weekly in-app messaging",
    "Progress tracking and accountability",
    "One 15-minute video call a month",
], (129, (368, 123), (696, 116)))}
{package("Core Coaching", "For committed clients who want structure, feedback and real support.", [
    "Everything in Essentials",
    "Two 30-minute video calls a month",
    "Monthly training and nutrition updates",
    "Form check-ins by video",
    "Private coaching resource library",
], (179, (511, 170), (966, 161)), pick=True)}
{package("Premium Coaching", "For high performers who want full support, accountability and access.", [
    "Everything in Core",
    "Weekly 15-minute calls or two 60-minute deep dives",
    "On-demand video form checks",
    "Biweekly training and nutrition adjustments",
    "Priority messaging and response",
], (249, (711, 237), (1344, 224)))}
</div>
</div>
</section>

<section class="wrap section">
<div class="split">
<div class="main stack" style="gap:18px">
<h2 class="h-section">Every package includes</h2>
<div class="rule"></div>
<ul class="dots">
<li>Fully individualized training and nutrition strategy</li>
<li>Weekly progress reviews and habit coaching</li>
<li>Full app access: workouts, meals, habits, messaging</li>
<li>PDF and in-app resources: macro guides, recipes, cardio planning</li>
<li>Progress tracking with photos, metrics and performance</li>
</ul>
</div>
<div class="side card stack center" style="gap:18px;padding:40px">
<h3 class="h-card it">This is an application</h3>
<p class="muted">If you’re a good fit, you’ll hear back with next steps.</p>
<a class="btn btn-red" href="/apply?path=online">Apply for online coaching</a>
</div>
</div>
</section>
"""

# ---------------------------------------------------------------- Apply
def opt(values):
    return "".join(f'<option value="{v}">{v}</option>' for v in values)


APPLY = page_head(
    "Apply to train with JR",
    "In person or online, this is where it starts. If you’re a good fit, you’ll hear back with next steps.",
) + f"""
<section class="wrap" style="padding-bottom:104px">
<form class="card" id="apply-form" style="max-width:820px;margin:0 auto" novalidate data-form="apply">
<fieldset class="field">
<legend>How do you want to train? <span class="req">*</span></legend>
<div class="choices">
<label class="choice"><input type="radio" name="path" value="in-person" required> In person, Corvallis</label>
<label class="choice"><input type="radio" name="path" value="online"> Online coaching</label>
<label class="choice"><input type="radio" name="path" value="consult"> Not sure, let’s talk</label>
</div>
</fieldset>
<div class="row2">
<div class="field"><label for="f-first">First name <span class="req">*</span></label><input id="f-first" name="first_name" type="text" autocomplete="given-name" required></div>
<div class="field"><label for="f-last">Last name <span class="req">*</span></label><input id="f-last" name="last_name" type="text" autocomplete="family-name" required></div>
</div>
<div class="row2">
<div class="field"><label for="f-email">Email <span class="req">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
<div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
</div>
<div class="row2">
<div class="field"><label for="f-goal">Primary goal <span class="req">*</span></label><select id="f-goal" name="goal" required><option value="">Select one</option>{opt(["Fat loss", "Muscle gain", "Performance", "Body recomposition", "Health and longevity", "Other"])}</select></div>
<div class="field"><label for="f-exp">Training experience <span class="req">*</span></label><select id="f-exp" name="experience" required><option value="">Select one</option>{opt(["Beginner", "Intermediate", "Advanced"])}</select></div>
</div>
<div class="row2">
<div class="field"><label for="f-freq">Current training frequency</label><select id="f-freq" name="frequency"><option value="">Select one</option>{opt(["0–2 days/week", "3–4 days/week", "5+ days/week"])}</select></div>
<div class="field"><label for="f-level">Online coaching level <span class="hint">(if online)</span></label><select id="f-level" name="level"><option value="">Select one</option>{opt(["Essentials", "Core", "Premium", "Not sure yet"])}</select></div>
</div>
<fieldset class="field">
<legend>Access to equipment</legend>
<div class="choices">
<label class="choice"><input type="checkbox" name="equipment" value="Full gym"> Full gym</label>
<label class="choice"><input type="checkbox" name="equipment" value="Home gym"> Home gym</label>
<label class="choice"><input type="checkbox" name="equipment" value="Minimal equipment"> Minimal equipment</label>
<label class="choice"><input type="checkbox" name="equipment" value="Bodyweight only"> Bodyweight only</label>
</div>
</fieldset>
<div class="field"><label for="f-limit">Biggest limiting factor right now</label><textarea id="f-limit" name="limiting_factor"></textarea></div>
<div class="field"><label for="f-why">Why are you seeking coaching now?</label><textarea id="f-why" name="why_now"></textarea></div>
<fieldset class="field">
<legend>Willing to commit to at least 3 months?</legend>
<div class="choices">
<label class="choice"><input type="radio" name="commit_3mo" value="Yes"> Yes</label>
<label class="choice"><input type="radio" name="commit_3mo" value="No"> No</label>
</div>
</fieldset>
<div class="field"><label for="f-msg">Anything else I should know?</label><textarea id="f-msg" name="message"></textarea></div>
<label class="choice"><input type="checkbox" name="newsletter" value="yes"> Send me occasional news and updates by email</label>
<p class="form-note">By applying you agree to the <a href="/privacy-policy" style="text-decoration:underline">Privacy Policy</a>. Health details are optional; we’ll cover them in your consult.</p>
<div class="form-status" role="status" hidden></div>
<div class="btns"><button class="btn btn-red" type="submit">Submit application</button></div>
</form>
</section>
"""

APPLY_SCRIPT = """<script>
(function(){
  var f=document.getElementById('apply-form'); if(!f) return;
  var q=new URLSearchParams(location.search), p=q.get('path'), lv=q.get('level');
  if(p){var r=f.querySelector('input[name=path][value="'+p+'"]'); if(r) r.checked=true;}
  if(lv){var s=f.querySelector('#f-level'); for(var i=0;i<s.options.length;i++){if(s.options[i].value.toLowerCase()===lv){s.selectedIndex=i;}}}
})();
</script>"""

# Shared form handler: preview mode until a backend is chosen.
FORM_SCRIPT = """<script>
document.querySelectorAll('form[data-form]').forEach(function(f){
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var st=f.querySelector('.form-status');
    if(!f.checkValidity()){ st.textContent='Please fill in the required fields marked with *.'; st.hidden=false; f.reportValidity(); return; }
    st.textContent='Preview only: this form isn’t connected yet, so nothing was sent.'; st.hidden=false;
  });
});
</script>"""

# ---------------------------------------------------------------- About
ABOUT = page_head("About JR") + f"""
<section class="wrap" style="padding-bottom:104px">
<div class="split" style="align-items:flex-start">
<div class="side"><div class="photo">{ph("Photo: JR coaching on the floor")}</div></div>
<div class="main prose">
<p class="lead" style="color:#fff">I’m JR Prieto-Romero, CSCS. I direct training at Timberhill Athletic Club and lead personal training and performance at G3 Sports &amp; Fitness in Corvallis, Oregon.</p>
<p>I grew up in Salem and came to Corvallis for Oregon State, where I earned my degree in Exercise &amp; Sport Science. Before I coached, I competed: soccer, sprinting and throwing.</p>
<p>I’ve spent more than ten years and roughly 20,000 hours on the training floor. Today I run personal training across two facilities. Every client who comes to TAC or G3 starts with a consult with me, and I place them with the coach and program that fit, even when that isn’t me.</p>
<p>My own clients sit at the Enhanced tier of IAOE: trained people, often current or former athletes, who have plateaued and want finer margins.</p>
<p>{ph("Your own words: why you started building tools for other coaches")}</p>
<h2>What I’m building</h2>
<ul>
<li><a href="{VAULT}">The Trainer’s Coach Vault</a>: the operating library for professional trainers and coaches.</li>
<li>Built For Her, TRAINCND and The Credential Standard: {ph("one line each")}</li>
</ul>
<h2>Credentials</h2>
<ul>
<li>Certified Strength and Conditioning Specialist (CSCS)</li>
<li>B.S. Exercise &amp; Sport Science, Oregon State University</li>
<li>Director of Training, Timberhill Athletic Club</li>
<li>Director of Personal Training, G3 Sports &amp; Fitness</li>
<li>Director of Performance, G3 Sports &amp; Fitness</li>
</ul>
<div class="btns" style="padding-top:8px"><a class="btn btn-red" href="/train">Train with JR</a><a class="btn btn-ghost" href="{LINKEDIN}">Connect on LinkedIn</a></div>
</div>
</div>
</section>
"""

# ---------------------------------------------------------------- Writing
WRITING = page_head(
    "Writing",
    "I write about coaching systems, consultations and building in public. New posts go up on LinkedIn every weekday.",
) + f"""
<section class="wrap" style="padding-bottom:104px">
<div class="card stack center" style="max-width:720px;margin:0 auto;gap:18px;padding:44px">
<h2 class="h-card it">Follow along on LinkedIn</h2>
<div class="rule sm"></div>
<p class="muted">The newest thinking shows up there first.</p>
<a class="btn btn-red" href="{LINKEDIN}">Follow JR on LinkedIn</a>
</div>
</section>
"""

# ---------------------------------------------------------------- Legal
DRAFT = '<p class="draft">Draft for JR’s review before launch. This is not legal advice; have an attorney review it.</p>'
UPDATED = "<p class=\"muted\">Last updated: [launch date]</p>"

PRIVACY = page_head("Privacy Policy") + f"""
<section class="wrap" style="padding-bottom:104px"><div class="prose" style="margin:0 auto">
{DRAFT}{UPDATED}
<p>This policy explains what JR Strength and Fitness LLC (“we”) collects through jrstrengthandfitness.com and how we use it.</p>
<h2>What we collect</h2>
<ul>
<li><strong>Coaching applications:</strong> your name, email, phone (optional), training goals, experience, equipment access, and anything else you choose to tell us.</li>
<li><strong>Waiver signatures:</strong> your name, email and the date you signed.</li>
<li><strong>Waitlist and newsletter sign-ups:</strong> your email address.</li>
<li><strong>Basic technical data:</strong> our hosting provider records standard server logs (such as IP address and browser type) to run and secure the site.</li>
</ul>
<h2>How we use it</h2>
<ul>
<li>To review your application and contact you about coaching.</li>
<li>To keep a record of your signed waiver.</li>
<li>To send news and updates, only if you opted in. You can unsubscribe at any time.</li>
</ul>
<p>We don’t sell your personal information.</p>
<h2>Who we share it with</h2>
<ul>
<li>Vercel, which hosts this website.</li>
<li>Google Fonts, which serves the site’s typeface.</li>
<li>{ph("Where form submissions are stored and how you're notified")}</li>
<li>Trainerize, if you become an online coaching client.</li>
</ul>
<p>We may also share information when required by law.</p>
<h2>How long we keep it</h2>
<p>We keep applications and waivers for as long as needed to provide coaching and meet legal obligations, then delete them. {ph("Confirm retention period")}</p>
<h2>Your choices</h2>
<p>You can ask us to see, correct or delete your information by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Minors</h2>
<p>Youth athletes train through G3 with a parent or guardian. Applications on this site should be submitted by adults, or by a parent or guardian for a minor.</p>
<h2>Contact</h2>
<p>JR Strength and Fitness LLC, 862 SW Adams Ave, Corvallis, OR 97333 · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>
"""

TERMS = page_head("Terms of Service") + f"""
<section class="wrap" style="padding-bottom:104px"><div class="prose" style="margin:0 auto">
{DRAFT}{UPDATED}
<p>These terms apply to your use of jrstrengthandfitness.com and to coaching services from JR Strength and Fitness LLC (“we”). By using the site or our services, you agree to them.</p>
<h2>Not medical advice</h2>
<p>Content on this site and in our coaching is for general fitness education. It isn’t medical advice. Talk to your physician before starting a new exercise or nutrition program. Every client signs our <a href="/waiver">waiver</a> before training.</p>
<h2>Coaching services</h2>
<p>Online coaching packages, prices and inclusions are described on the <a href="/online-training">Online Coaching</a> page. Coaching is delivered through the Trainerize app, and payments are processed there. Cancellations and refunds follow our <a href="/refund-policy">Refund Policy</a>.</p>
<p>We may decline an application if coaching isn’t a good fit.</p>
<h2>Your responsibilities</h2>
<p>Give accurate information about your health, training history and limitations, and tell your coach about changes. Train within your abilities and follow your program as written.</p>
<h2>Our content</h2>
<p>Programs, guides, videos and other materials we provide are for your personal use. Don’t copy, resell or redistribute them without written permission.</p>
<h2>Other websites</h2>
<p>Links to other sites, including our own products on separate domains, are governed by those sites’ terms.</p>
<h2>Limitation of liability</h2>
<p>To the extent allowed by law, we aren’t liable for indirect or consequential damages arising from your use of the site or our services.</p>
<h2>Changes</h2>
<p>We may update these terms. The date at the top shows the latest version.</p>
<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of Oregon.</p>
<h2>Contact</h2>
<p>JR Strength and Fitness LLC, 862 SW Adams Ave, Corvallis, OR 97333 · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>
"""

REFUND = page_head("Refund Policy") + f"""
<section class="wrap" style="padding-bottom:104px"><div class="prose" style="margin:0 auto">
{DRAFT}{UPDATED}
<p>This policy covers online coaching packages. In-person training at Timberhill Athletic Club and G3 follows each facility’s own policies.</p>
<h2>Monthly packages</h2>
<p>{ph("Your policy: e.g. cancel any time before your next billing date; the current month isn’t refunded")}</p>
<h2>3-month and 6-month packages</h2>
<p>{ph("Your policy: e.g. prepaid packages are non-refundable after the first 7 days, or refunded pro rata")}</p>
<h2>How to cancel</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or message your coach in the app. {ph("Notice period, if any")}</p>
<h2>Exceptions</h2>
<p>If an injury or medical issue stops you from training, contact us. {ph("Your policy: e.g. pause or partial credit")}</p>
</div></section>
"""

WAIVER = page_head("Waiver") + f"""
<section class="wrap" style="padding-bottom:104px"><div class="prose" style="margin:0 auto">
<p>Because physical exercise can be strenuous and subject to risk of serious injury, you are urged to obtain a physical examination from a doctor before using any exercise equipment or participating in any exercise activity. You agree that by participating in physical exercise or training activities, you do so entirely at your own risk. Any recommendation for changes in diet including the use of food supplements, weight reduction and body building enhancement products are entirely your responsibility and you should consult a physician prior to undergoing any dietary or food supplement changes. You agree that you are voluntarily participating in these activities and assume all risks of injury, illness, or death.</p>
<p>You acknowledge that you have carefully read this “waiver and release” and fully understand that it is a release of liability. You expressly agree to release and discharge JR Strength and Fitness LLC from any and all claims or causes of action and you agree to voluntarily give up or waive any right that you may otherwise have to bring a legal action against JR Strength and Fitness LLC for personal injury or damage.</p>
<p>To the extent that statute or case law does not prohibit releases for negligence, this release is also for negligence.</p>
<p>If any portion of this release form liability shall be deemed by a Court of competent jurisdiction to be invalid, then the remainder of this release from liability shall remain in full force and effect and the offending provision or provisions severed here from.</p>
<p>By signing this release, I acknowledge that I understand its content and that this release cannot be modified orally.</p>
<p><strong>JR Prieto-Romero</strong><br>Owner &amp; CEO<br>JR Strength and Fitness LLC</p>
<form class="card" data-form="waiver" novalidate style="margin-top:12px">
<h2 class="h-card it" style="padding-top:0">Sign the waiver</h2>
<div class="row2">
<div class="field"><label for="w-first">First name <span class="req">*</span></label><input id="w-first" name="first_name" type="text" autocomplete="given-name" required></div>
<div class="field"><label for="w-last">Last name <span class="req">*</span></label><input id="w-last" name="last_name" type="text" autocomplete="family-name" required></div>
</div>
<div class="field"><label for="w-email">Email <span class="req">*</span></label><input id="w-email" name="email" type="email" autocomplete="email" required></div>
<label class="choice"><input type="checkbox" name="agree" value="yes" required> I have read this waiver and agree to its terms. <span class="req">*</span></label>
<div class="form-status" role="status" hidden></div>
<div class="btns"><button class="btn btn-red" type="submit">Sign waiver</button></div>
</form>
</div></section>
"""

NOT_FOUND = page_head("Page not found", "That page moved or never existed.") + """
<section class="wrap" style="padding-bottom:104px"><div class="btns" style="justify-content:center"><a class="btn btn-red" href="/">Go home</a><a class="btn btn-ghost" href="/train">Train with JR</a></div></section>
"""
