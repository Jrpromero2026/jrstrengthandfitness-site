"""Page content for jrstrengthandfitness.com (v2 layout). Bracketed [text] marks copy or media JR still needs to supply."""

from layout import VAULT, LINKEDIN, EMAIL, CONSULT, TAC_PT, G3_PT, FORM_ENDPOINT
from ui import ph, hero, sec, head_row, rows, frame
import projects as P

CONSULT_BTN = f'<a class="btn btn-red" href="{CONSULT}">Book a free consult</a>'

# ---------------------------------------------------------------- Home
CRED_CARD = """<div class="cred-card"><div class="k">Credentials</div><div class="v"><span>CSCS</span><span>B.S. Oregon State</span><span>20,000 hrs</span></div></div>"""

STRIP = """<section class="strip" aria-label="Roles"><div class="wrap">
<div class="c"><b>01</b><span>Director of Training, TAC</span></div>
<div class="c"><b>02</b><span>Director of PT &amp; Performance, G3</span></div>
<div class="c"><b>03</b><span>Founder of four coaching products</span></div>
<div class="c"><b>04</b><span>10+ years on the floor</span></div>
</div></section>"""

IAOE_ROWS = rows([
    dict(n="01", k="Below the line", t="Inadequate", d="Unsafe, unstructured or not progressing.", cls="dim"),
    dict(n="02", k="Fitness trainer", t="Adequate", d="Safe, effective and progressing. The right target for many clients."),
    dict(n="03", k="Fitness coach", t="Optimal", d="Individualized programming built around the person’s goals."),
    dict(n="04", k="Performance coach", t="Enhanced", d="Where I coach: trained athletes who have plateaued and want finer margins.", cls="hot"),
])

HOME = (
    hero(
        "Coach · Builder · Corvallis, Oregon",
        "Built on<br>the floor.<br>Now built<br>for coaches.",
        "I’m JR Prieto-Romero, CSCS. I direct training at Timberhill Athletic Club and lead personal training and performance at G3 Sports &amp; Fitness. Now I’m turning what works on the floor into tools for coaches and athletes.",
        f'{CONSULT_BTN}<a class="link-u" href="#projects">See what I’m building ↓</a>',
        frame("Photo: JR coaching on the floor", card=CRED_CARD),
    )
    + STRIP
    + sec("light", head_row("What I’m building", "Four projects.<br>One coaching<br>standard.",
                            "Each one started as a problem I kept solving by hand at TAC or G3. Now they’re tools any coach, athlete or gym can use.")
          + P.panel() + P.FOR_ROW, id="projects")
    + sec("dark", head_row("The standard underneath", "Match the<br>intervention<br>to the person.",
                           "Every project runs on IAOE. Adequate is a legitimate target, not a failure: safe, effective and progressing is the right outcome for many clients.")
          + IAOE_ROWS, id="standard")
    + sec("light", f"""<div class="split">
<div class="side">{frame("Photo or short video: a session at TAC or G3", wide=True)}</div>
<div class="main stack">
<span class="eyebrow">Train with JR</span>
<h2 class="h-md">Every client starts with a free 30-minute consult.</h2>
<p class="lead">Goals, training history, limitations, barriers and preferences. Local clients start at Timberhill or G3, where I match you with the right coach and program. Sometimes that coach isn’t me.</p>
<div class="facts"><div>In person · Corvallis</div><div>Online · from $129/mo</div><div>No membership needed</div></div>
<div class="btns">{CONSULT_BTN}<a class="link-u" href="/train">How training works →</a></div>
</div>
</div>""", id="train")
    + sec("gray", f"""<div class="split">
<div class="side"><div class="tile"><div class="box"><img src="/assets/jr-mark.png" alt=""><span>The Trainer’s<br>Coach Vault</span></div><span class="badge">Founding membership soon</span></div></div>
<div class="main stack">
<span class="eyebrow">Featured project</span>
<h2 class="h-md">The operating library for coaches.</h2>
<p class="lead">Consultation systems, programming frameworks and client-management tools I built and run across two facilities, packaged so a working coach can use them this week.</p>
<div class="stats"><div><b>34</b><span>Systems &amp; frameworks</span></div><div><b>26</b><span>Tools</span></div><div><b>11</b><span>Workflows</span></div></div>
<div class="btns"><a class="btn btn-line" href="{VAULT}/signup" rel="noopener">Create a free account</a><a class="link-u" href="/projects/vault">About the Vault →</a></div>
</div>
</div>""", mark=False)
    + sec("dark", """<div class="head-row" style="margin-bottom:0">
<div class="h"><span class="eyebrow">About JR</span><h2 class="h-display">Salem.<br>Oregon State.<br>20,000 hours.</h2></div>
<div class="stack" style="flex:1 1 420px;min-width:0;gap:18px">
<p class="lead">I grew up in Salem, came to Corvallis for Oregon State and earned my degree in Exercise &amp; Sport Science. I played soccer, sprinted and threw before I ever coached.</p>
<p class="lead">Today I direct training at Timberhill Athletic Club, lead personal training and performance at G3, and coach my own clients at the Enhanced tier.</p>
<a class="link-u" href="/about" style="align-self:flex-start">Read the full story →</a>
</div>
</div>""", id="about")
)

# ---------------------------------------------------------------- Train with JR
TRAIN = (
    hero("Train with JR", "Every client starts with a free consult.",
         "Local to Corvallis? Book a free consult at Timberhill Athletic Club or G3 Sports &amp; Fitness. You don’t need to be a member. Anywhere else, apply for online coaching.",
         f'{CONSULT_BTN}<a class="link-u" href="/online-training">Online coaching →</a>',
         frame("Photo: consult at TAC or G3"), short=True, size="h-display")
    + sec("light", head_row("How it works", "Consult. Match.<br>Train.",
                            "One coaching standard at both facilities, whoever your coach is.")
          + rows([
              ("01", "Consult", "Thirty minutes with JR", "Your goals, training history, limitations, barriers and preferences."),
              ("02", "Match", "The right coach and facility", "I choose the facility, the coach and the program. Sometimes the best coach for you isn’t me."),
              ("03", "Train", "A plan built for you", "You start with a program built around you, held to the same standard at both locations."),
          ]))
    + sec("dark", head_row("Where you’ll train", "Two facilities.<br>One standard.",
                           "Families often split: a parent trains at TAC while their kid trains at G3. One consult covers both.")
          + f"""<div class="panel">
<div class="cell"><div class="bar"></div><span class="tag live">In person · Corvallis</span><h3 class="h-cell">Timberhill Athletic Club</h3><ul class="ticks"><li>Health and general fitness</li><li>Longevity and staying capable</li><li>Adults at every starting point</li></ul><div class="grow"></div><div class="btns" style="padding-top:10px"><a class="btn btn-red" href="{TAC_PT}" rel="noopener">Book at Timberhill</a></div></div>
<div class="cell"><div class="bar"></div><span class="tag live">In person · Corvallis</span><h3 class="h-cell">G3 Sports &amp; Fitness</h3><ul class="ticks"><li>Youth athletic development</li><li>Adult human performance</li><li>Tactical, teams and organizations</li></ul><div class="grow"></div><div class="btns" style="padding-top:10px"><a class="btn btn-red" href="{G3_PT}" rel="noopener">Book at G3</a></div></div>
</div>""")
    + sec("light", f"""<div class="split">
<div class="side">{frame("Photo: an online coaching check-in", wide=True)}</div>
<div class="main stack">
<span class="eyebrow">Not in Corvallis?</span>
<h2 class="h-md">Train with me online.</h2>
<p class="lead">Individualized training and nutrition through the app, with check-ins and adjustments.</p>
<div class="facts"><div>Essentials · $129/mo</div><div>Core · $179/mo</div><div>Premium · $249/mo</div></div>
<div class="btns"><a class="btn btn-red" href="/apply">Apply for online coaching</a><a class="link-u" href="/online-training">Compare packages →</a></div>
</div>
</div>""")
)

# ---------------------------------------------------------------- Consult routing
CONSULT_PAGE = (
    hero("Free consult", "Start with a free consult.",
         "Local to Corvallis? Every in-person client starts with a free consult at Timberhill Athletic Club or G3 Sports &amp; Fitness. Pick the one that fits your goals. You don’t need to be a member.",
         '<a class="link-u" href="#choose">Choose a facility ↓</a>', short=True, size="h-display")
    + sec("light", head_row("Choose your facility", "Two facilities.<br>One standard.",
                            "Not sure? Pick either one. Families often split: a parent trains at Timberhill while their kid trains at G3.")
          + f"""<div class="panel">
<div class="cell"><div class="bar"></div><span class="tag live">Health · fitness · longevity</span><h2 class="h-cell">Timberhill Athletic Club</h2><ul class="ticks"><li>Health and general fitness</li><li>Longevity and staying capable</li><li>Adults at every starting point</li><li>Free initial consultation with personal training</li></ul><div class="grow"></div><div class="btns" style="padding-top:10px"><a class="btn btn-red" href="{TAC_PT}" rel="noopener">Book at Timberhill</a></div></div>
<div class="cell"><div class="bar"></div><span class="tag live">Performance · athletes · teams</span><h2 class="h-cell">G3 Sports &amp; Fitness</h2><ul class="ticks"><li>Youth athletic development</li><li>Adult human performance</li><li>Tactical, teams and organizations</li><li>Personal training with the G3 coaching staff</li></ul><div class="grow"></div><div class="btns" style="padding-top:10px"><a class="btn btn-red" href="{G3_PT}" rel="noopener">Book at G3</a></div></div>
</div>""", id="choose")
    + sec("dark", """<div class="split">
<div class="main stack"><span class="eyebrow">Not in Corvallis?</span><h2 class="h-md">Train with me online.</h2><p class="lead">Individualized training and nutrition through the app, with check-ins and adjustments. Packages start at $129 a month.</p></div>
<div class="side"><div class="btns"><a class="btn btn-red" href="/apply">Apply for online coaching</a><a class="link-u" href="/online-training">Compare packages →</a></div></div>
</div>""")
)

# ---------------------------------------------------------------- Online training
def package(name, who, features, prices, pick=False):
    feats = "".join(f"<li>{f}</li>" for f in features)
    month, three, six = prices
    short = name.split()[0]
    flag = '<span class="flag">Most popular</span>' if pick else ""
    return f"""<div class="cell{' pick' if pick else ''}">
<div class="bar"></div>
{flag}
<h3 class="h-cell">{name}</h3>
<p>{who}</p>
<div class="amt">${month}<small>/month</small></div>
<p class="terms">3 months: ${three[0]} (~${three[1]}/mo) · 6 months: ${six[0]} (~${six[1]}/mo)</p>
<ul class="ticks">{feats}</ul>
<div class="grow"></div>
<div class="btns" style="padding-top:8px"><a class="btn {'btn-red' if pick else 'btn-line'}" href="/apply?level={short.lower()}">Apply for {short}</a></div>
</div>"""


ONLINE = (
    hero("Online coaching", "Coaching, not content.",
         "You don’t need more workouts. You need structure, progression and a plan built for your life, with someone checking that it gets done.",
         '<a class="btn btn-red" href="/apply">Apply for online coaching</a><a class="link-u" href="#packages">See packages ↓</a>',
         short=True, size="h-display")
    + sec("light", head_row("How it works", "Assess. Build.<br>Execute. Refine.") + rows([
        ("01", "Assess", "No assumptions", "Intake, history, schedule, goals and constraints."),
        ("02", "Build", "Structured with intent", "Training and nutrition built with progression and purpose."),
        ("03", "Execute", "Weekly targets", "Daily actions and consistent check-ins."),
        ("04", "Refine", "Data drives decisions", "Results dictate change. Nothing stays static."),
    ]))
    + sec("dark", head_row("Packages", "Three levels<br>of coaching.", "Every package includes both training and nutrition coaching.")
          + f"""<div class="panel three">
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
</div>""", id="packages")
    + sec("light", """<div class="split top">
<div class="main stack"><span class="eyebrow">Every package includes</span><h2 class="h-md">Everything you need to execute.</h2>
<ul class="ticks">
<li>Fully individualized training and nutrition strategy</li>
<li>Weekly progress reviews and habit coaching</li>
<li>Full app access: workouts, meals, habits, messaging</li>
<li>PDF and in-app resources: macro guides, recipes, cardio planning</li>
<li>Progress tracking with photos, metrics and performance</li>
</ul></div>
<div class="side"><div class="info-card"><span class="k">This is an application</span><div class="it"><b>Not a sign-up</b><span>If you’re a good fit, you’ll hear back with next steps.</span></div><div class="btns" style="padding-top:14px"><a class="btn btn-red" href="/apply">Apply now</a></div></div></div>
</div>""")
)

# ---------------------------------------------------------------- Apply
def opt(values):
    return "".join(f'<option value="{v}">{v}</option>' for v in values)


APPLY = (
    hero("Online coaching", "Apply for online coaching.",
         "Tell me about your training and goals. Your application comes straight to me, and if you’re a good fit you’ll hear back by email with next steps.",
         f'<a class="link-u" href="{CONSULT}">Local to Corvallis? Book a free consult instead →</a>', short=True, size="h-display")
    + sec("light", f"""<form class="form-card" id="apply-form" novalidate data-form="apply" data-done="Thanks, your application went straight to JR. You’ll hear back by email with next steps.">
<input type="hidden" name="_subject" value="Online coaching application">
<div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
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
<div class="field"><label for="f-level">Coaching level you’re interested in</label><select id="f-level" name="level"><option value="">Select one</option>{opt(["Essentials", "Core", "Premium", "Not sure yet"])}</select></div>
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
<p class="form-note">Your application is emailed to JR. By applying you agree to the <a href="/privacy-policy">Privacy Policy</a>. Health details are optional; we’ll cover them on our first call.</p>
<div class="form-status" role="status" hidden></div>
<div class="btns"><button class="btn btn-red" type="submit">Submit application</button></div>
</form>""", mark=False)
)

APPLY_SCRIPT = """<script>
(function(){
  var f=document.getElementById('apply-form'); if(!f) return;
  var q=new URLSearchParams(location.search), lv=q.get('level');
  if(lv){var s=f.querySelector('#f-level'); for(var i=0;i<s.options.length;i++){if(s.options[i].value.toLowerCase()===lv){s.selectedIndex=i;}}}
})();
</script>"""

# Shared form handler: emails each submission to JR through FormSubmit (formsubmit.co).
FORM_SCRIPT = """<script>
document.querySelectorAll('form[data-form]').forEach(function(f){
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var st=f.querySelector('.form-status'), btn=f.querySelector('button[type=submit]');
    if(!f.checkValidity()){ st.textContent='Please fill in the required fields marked with *.'; st.hidden=false; f.reportValidity(); return; }
    var data={}; new FormData(f).forEach(function(v,k){ if(data[k]!==undefined){ data[k]=data[k]+', '+v; } else { data[k]=v; } });
    if(data._honey){ return; }
    var who=((data.first_name||'')+' '+(data.last_name||'')).trim();
    if(who){ data._subject=(data._subject||'Website submission')+' — '+who; }
    data._template='table'; data._captcha='false'; data.page=location.href;
    btn.disabled=true; var label=btn.textContent; btn.textContent='Sending…'; st.hidden=true;
    fetch('""" + FORM_ENDPOINT + """',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
      .then(function(r){ return r.json().catch(function(){ return {}; }).then(function(j){ if(!r.ok || String(j.success)==='false'){ throw new Error(j.message||'send failed'); } }); })
      .then(function(){ if(window.va){ window.va('event',{name:(f.getAttribute('data-form')==='apply'?'Application submitted':'Waitlist signup'),data:{project:(data.project||data.level||''),page:location.pathname}}); } f.reset(); st.textContent=f.getAttribute('data-done')||'Thanks, it’s in. You’ll hear back by email.'; st.hidden=false; btn.textContent=label; btn.disabled=false; })
      .catch(function(){ st.textContent='Something went wrong sending this. Please email jr@jrstrengthandfitness.com directly.'; st.hidden=false; btn.textContent=label; btn.disabled=false; });
  });
});
</script>"""

# ---------------------------------------------------------------- About
ABOUT = (
    hero("About JR", "Salem. Oregon State.<br>20,000 hours.",
         "I’m JR Prieto-Romero, CSCS. I direct training at Timberhill Athletic Club and lead personal training and performance at G3 Sports &amp; Fitness in Corvallis, Oregon.",
         f'{CONSULT_BTN}<a class="link-u" href="{LINKEDIN}" rel="noopener">Connect on LinkedIn →</a>',
         frame("Photo: JR portrait"), short=True, size="h-display")
    + sec("light", f"""<div class="split top">
<div class="side stack" style="gap:18px"><span class="eyebrow">My story</span><h2 class="h-display">Athlete first.<br>Coach second.<br>Builder now.</h2></div>
<div class="main prose" style="max-width:none">
<p class="lead" style="max-width:none">I grew up in Salem and came to Corvallis for Oregon State, where I earned my degree in Exercise &amp; Sport Science. Before I coached, I competed: soccer, sprinting and throwing.</p>
<p class="lead" style="max-width:none">I’ve spent more than ten years and roughly 20,000 hours on the training floor. Today I run personal training across two facilities. Every client who comes to TAC or G3 starts with a consult with me, and I place them with the coach and program that fit, even when that isn’t me.</p>
<p class="lead" style="max-width:none">My own clients sit at the Enhanced tier of IAOE: trained people, often current or former athletes, who have plateaued and want finer margins.</p>
<p class="lead" style="max-width:none">{ph("Your own words: why you started building tools for other coaches")}</p>
</div>
</div>""")
    + sec("dark", head_row("Credentials", "Built on<br>standards.") + rows([
        ("01", "Certification", "CSCS", "Certified Strength and Conditioning Specialist."),
        ("02", "Education", "B.S. Exercise &amp; Sport Science", "Oregon State University."),
        ("03", "Timberhill Athletic Club", "Director of Training", "Leads personal training and the trainer team."),
        ("04", "G3 Sports &amp; Fitness", "Director of Personal Training", "Every G3 training client starts with JR."),
        ("05", "G3 Sports &amp; Fitness", "Director of Performance", "Youth athletic development, adult performance, tactical and teams."),
    ]))
    + sec("light", head_row("What I’m building", "Four projects.<br>One standard.") + P.panel())
)

# ---------------------------------------------------------------- Legal
DRAFT = '<p class="draft">Draft for JR’s review before launch. This is not legal advice; have an attorney review it.</p>'
UPDATED = "<p class=\"muted\">Last updated: [launch date]</p>"


def legal(eyebrow, title, prose):
    return hero(eyebrow, title, short=True, size="h-display") + sec("light", f'<div class="prose">{prose}</div>', mark=False)


PRIVACY = legal("Legal", "Privacy Policy", f"""{DRAFT}{UPDATED}
<p>This policy explains what JR Strength and Fitness LLC (“we”) collects through jrstrengthandfitness.com and how we use it.</p>
<h2>What we collect</h2>
<ul>
<li><strong>Online coaching applications:</strong> your name, email, phone (optional), training goals, experience, equipment access, and anything else you choose to tell us.</li>
<li><strong>Waitlist sign-ups:</strong> your email address and the project you’re interested in.</li>
<li><strong>Basic technical data:</strong> our hosting provider records standard server logs (such as IP address and browser type) to run and secure the site.</li>
</ul>
<h2>How we use it</h2>
<ul>
<li>To review your application and contact you about coaching.</li>
<li>To tell you when a project you signed up for opens. You can ask to be removed at any time.</li>
</ul>
<p>We don’t sell your personal information.</p>
<h2>Who we share it with</h2>
<ul>
<li>Vercel, which hosts this website.</li>
<li>Google Fonts, which serves the site’s typeface.</li>
<li>FormSubmit, which delivers form submissions from this site to our email inbox.</li>
<li>Google Workspace, which hosts our email.</li>
<li>Trainerize, if you become an online coaching client.</li>
</ul>
<p>We may also share information when required by law.</p>
<h2>How long we keep it</h2>
<p>We keep applications and sign-ups for as long as needed to provide coaching and meet legal obligations, then delete them. {ph("Confirm retention period")}</p>
<h2>Your choices</h2>
<p>You can ask us to see, correct or delete your information by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Minors</h2>
<p>Youth athletes train through G3 with a parent or guardian. Applications on this site should be submitted by adults, or by a parent or guardian for a minor.</p>
<h2>Contact</h2>
<p>JR Strength and Fitness LLC, 862 SW Adams Ave, Corvallis, OR 97333 · <a href="mailto:{EMAIL}">{EMAIL}</a></p>""")
TERMS = legal("Legal", "Terms of Service", f"""{DRAFT}{UPDATED}
<p>These terms apply to your use of jrstrengthandfitness.com and to coaching services from JR Strength and Fitness LLC (“we”). By using the site or our services, you agree to them.</p>
<h2>Not medical advice</h2>
<p>Content on this site and in our coaching is for general fitness education. It isn’t medical advice. Talk to your physician before starting a new exercise or nutrition program. Clients sign a waiver with their training facility (Timberhill Athletic Club or G3 Sports &amp; Fitness) or coaching platform before training.</p>
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
<p>JR Strength and Fitness LLC, 862 SW Adams Ave, Corvallis, OR 97333 · <a href="mailto:{EMAIL}">{EMAIL}</a></p>""")
REFUND = legal("Legal", "Refund Policy", f"""{DRAFT}{UPDATED}
<p>This policy covers online coaching packages. In-person training at Timberhill Athletic Club and G3 follows each facility’s own policies.</p>
<h2>Monthly packages</h2>
<p>{ph("Your policy: e.g. cancel any time before your next billing date; the current month isn’t refunded")}</p>
<h2>3-month and 6-month packages</h2>
<p>{ph("Your policy: e.g. prepaid packages are non-refundable after the first 7 days, or refunded pro rata")}</p>
<h2>How to cancel</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or message your coach in the app. {ph("Notice period, if any")}</p>
<h2>Exceptions</h2>
<p>If an injury or medical issue stops you from training, contact us. {ph("Your policy: e.g. pause or partial credit")}</p>""")

NOT_FOUND = hero("404", "Page not found.", "That page moved or never existed.",
                 '<a class="btn btn-red" href="/">Go home</a><a class="link-u" href="/train">Train with JR →</a>', short=True, size="h-display")
