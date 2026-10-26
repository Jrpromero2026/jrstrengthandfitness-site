"""Free resources (lead magnets): the /resources hub, one landing page per resource, and a "check your inbox" page.

The PDF is only ever delivered by email (the first email in the resource's Kit sequence). Nothing on the site links
to it: the thanks page sends people to their inbox, which is the point of collecting the email.

How a request flows:
  landing page form -> Kit form (adds the resource tag; Kit automation starts that resource's sequence)
                    -> Kit redirects to /resources/<slug>/thanks, which tells them to check their inbox (no download link)
                       and offers the newsletter as a separate choice.
  If the visitor ticks the unticked "Also send me Notes from the Floor" box, the same submit also subscribes them to the
  matching double opt-in newsletter form (training -> Newsletter: Training 10028379, coach -> Newsletter: Coaches
  10028376) with signup_source set, so they land in segment 599537. Unticked, the request never joins the newsletter.
  Why a box and not automatic (tested 2026-10-26): the LM forms have double opt-in off, so a requester is already an
  active Kit subscriber, and Kit then puts an active subscriber straight onto a newsletter form without waiting for the
  confirm click. The confirm email could not be the consent, so the tick is.
Until a resource's Kit form ID is filled in below, requests are emailed to JR through FormSubmit (with an
auto-reply that carries the download link) and the visitor goes straight to the thanks page. Nobody is lost.

Kit setup per resource (done once, in Kit):
  1. Create an inline form named "LM: <title>". Paste its numeric ID into `kit_form` below.
  2. In the form's settings: success action -> redirect to https://www.jrstrengthandfitness.com/resources/<slug>/thanks
     and turn OFF "send incentive email" (the sequence's first email delivers the file).
  3. Visual automation: "Joins form LM: <title>" -> "Add tag <tag>" -> "Subscribe to sequence <sequence>".

To launch the next resource: add its PDF to public/resources/, its two page images to public/assets/resources/,
an entry below with live=True, rebuild.
"""
import html

from layout import FORM_ENDPOINT
from ui import hero, sec, head_row
import newsletter as NL

SITE = "https://www.jrstrengthandfitness.com"

RESOURCES = [
    dict(
        slug="training-progress-audit", live=True, lane="training",
        title="The Training Progress Audit", short="the audit", brand="JR Strength &amp; Fitness",
        kit_form="10061495",               # Kit form "LM: Training Progress Audit"
        email_subject="Your Training Progress Audit",  # subject of sequence 2933412's first email (shown on the thanks page)
        tag="lm-training-audit", source="src-lm-audit", sequence="LM01 Training Progress Audit: delivery + follow-ups",
        interest="training", article="why-your-training-program-stops-working",
        pages=7,
        h1="Before you change<br>the plan.",
        card="Six short worksheets for when progress stalls: what you expected, what you did, and what to do next.",
        lead="Progress slowed and the first instinct is a new program. This audit helps you work out what actually happened "
             "first: what you expected, what you did, and what changed.",
        inside=[
            ("The goal", "What was supposed to change, in one sentence you can measure."),
            ("The record", "Sessions planned, completed and cut short, from your log or calendar."),
            ("The direction", "Six checks on whether you know what comes next."),
            ("The response", "What you saw, kept separate from what you think caused it."),
            ("One next step", "The first line that fits, and who can help."),
            ("Next review", "Five lines to run it again."),
        ],
        who="Adults who train on their own or with a coach and feel stuck.",
        scope="It doesn't diagnose a plateau or clear you to train. If pain or a health concern is part of the picture, "
              "talk to a qualified professional first.",
        button="Email me the audit",
        first_action="Write one sentence about what you want your training to help you do. Then open your training log "
                     "or calendar and fill in the record on page three.",
    ),
    dict(
        slug="program-troubleshooting-field-guide", live=True, lane="coaching",
        title="The Program Troubleshooting Field Guide", short="the Field Guide", brand="The Trainer&rsquo;s Coach Vault",
        kit_form="10061497",               # Kit form "LM: Program Troubleshooting Field Guide"
        email_subject="Your Program Troubleshooting Field Guide",  # subject of sequence 2933413's first email
        tag="lm-field-guide", source="src-lm-fieldguide", sequence="LM02 Program Troubleshooting Field Guide: delivery + follow-ups",
        interest="coach", article="your-client-didnt-plateau-their-week-did",
        pages=8,
        h1="Find the problem<br>before the fix.",
        card="The review I run before changing a stalled client's program. Ends with one written adjustment.",
        lead="When a client stops progressing, the easy move is a new program. This is the review I run first: the goal, "
             "the record, then the plan. It ends with one written adjustment and a date to check it.",
        inside=[
            ("The question", "Goal, phase, and what you saw that started the review."),
            ("The order", "Safety and scope first, then the six steps."),
            ("Execution", "Planned versus completed, with four questions to ask without blame."),
            ("Program and context", "Seven checks when the client did the work."),
            ("The adjustment", "One record per change, including what stays the same."),
            ("The conversation", "How to explain the decision to the client in one breath."),
        ],
        who="Working trainers and strength coaches.",
        scope="A coaching review process. It isn't a validated diagnostic tool and doesn't replace scope of practice, "
              "clinical referral or your own judgment.",
        button="Email me the Field Guide",
        first_action="Pick one client whose progress has stalled. Before you change anything, fill in page two: the goal, "
                     "the current phase, and what you saw that started the review.",
    ),
]
LIVE = [r for r in RESOURCES if r["live"]]
BY_SLUG = {r["slug"]: r for r in RESOURCES}
BY_ARTICLE = {r["article"]: r for r in LIVE if r.get("article")}
LANES = [("training", "Your training"), ("coaching", "Your coaching career"), ("business", "Your coaching business")]


def path(r):
    return f"/resources/{r['slug']}"


def pdf(r):
    return f"/resources/{r['slug']}.pdf"


def img(r, n):
    return f"/assets/resources/{r['slug']}-p{n}.webp"


# ---------------------------------------------------------------- Hub
def _card(r):
    return f"""<a class="rs-card" href="{path(r)}">
<span class="rs-img"><img src="{img(r, 1)}" alt="Cover of {html.escape(r['title'])}" width="600" height="776" loading="lazy" decoding="async"></span>
<span class="rs-body">
<span class="rs-k">{r['brand']} · {r['pages']} pages</span>
<span class="h-cell">{r['title']}</span>
<span class="rs-d">{r['card']}</span>
<span class="link-u">Get it free →</span>
</span>
</a>"""


def hub_body():
    lanes = ""
    for key, label in LANES:
        items = [r for r in LIVE if r["lane"] == key]
        if not items:
            continue
        lanes += f'<div class="rs-lane"><span class="eyebrow">{label}</span><div class="rs-grid">{"".join(_card(r) for r in items)}</div></div>'
    return (
        hero("Free resources", "Tools from<br>the floor.",
             "Worksheets I use with clients and coaches. Each one solves one problem and needs a pen and your own records. "
             "No purchase needed, and requesting one doesn't sign you up for anything else unless you tick the newsletter box.",
             short=True, size="h-display")
        + sec("light", lanes)
    )


# ---------------------------------------------------------------- Landing page
def _form(r):
    return f"""<form class="form-card rs-form" method="post" action="#" novalidate data-resource="{r['slug']}"
 data-kit="{r['kit_form']}" data-nl="{NL.KIT_FORMS[r['interest']]}" data-source="{r['source']}" data-thanks="{path(r)}/thanks" data-title="{html.escape(r['title'])}"{"" if r['kit_form'] else f' data-pdf="{SITE}{pdf(r)}"'}>
<div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
<div class="field"><label for="rs-first-{r['slug']}">First name <span class="hint">optional</span></label>
<input id="rs-first-{r['slug']}" name="fields[first_name]" type="text" autocomplete="given-name"></div>
<div class="field"><label for="rs-email-{r['slug']}">Email <span class="req">*</span></label>
<input id="rs-email-{r['slug']}" name="email_address" type="email" autocomplete="email" required></div>
<input type="hidden" name="fields[signup_source]" value="{r['source']}">
<div class="field attest"><label class="choice"><input type="checkbox" name="nl_optin" value="yes"> Also send me Notes from the Floor, my weekly email. You’ll get an email to confirm. Unsubscribe anytime.</label></div>
<div class="form-status" role="status" hidden></div>
<div class="btns"><button class="btn btn-red" type="submit">{r['button']}</button></div>
<p class="form-note">I'll email it to you right away, plus four short emails over two weeks on using it.
Unsubscribe anytime. See the <a href="/privacy-policy">Privacy Policy</a>.</p>
</form>"""


def landing_body(r):
    inside = '<div class="rows rs-rows">' + "".join(
        f'<div class="row"><span class="n">{i:02d}</span><span class="t">{t}</span><span class="d">{d}</span></div>'
        for i, (t, d) in enumerate(r["inside"], 1)) + "</div>"
    return (
        hero(f"Free resource · {r['brand']}", r["h1"], r["lead"], side=_form(r), short=True)
        + sec("light", f"""<div class="split top">
<div class="main stack" style="gap:28px">{head_row("What's inside", f"{r['pages']} pages.<br>One pen.", None, size="h-md")}{inside}</div>
<div class="side"><div class="rs-sample"><img src="{img(r, 2)}" alt="A worksheet page from {html.escape(r['title'])}" width="600" height="776" loading="lazy" decoding="async"></div></div>
</div>""")
        + sec("gray", f"""<div class="split top rs-fit">
<div class="main stack" style="gap:14px"><span class="eyebrow">Who it's for</span><p class="lead">{r['who']}</p></div>
<div class="side stack" style="gap:14px"><span class="eyebrow">What it isn't</span><p class="body">{r['scope']}</p></div>
</div>""", tight=True)
    )


# ---------------------------------------------------------------- Thanks page: check your inbox (no download here)
SENDER = "jr@jrstrengthandfitness.com"
INBOX_LINKS = (
    ("Open Gmail", "https://mail.google.com/mail/u/0/#search/from%3Ajr%40jrstrengthandfitness.com"),
    ("Open Outlook", "https://outlook.live.com/mail/0/"),
)


def thanks_body(r):
    btns = "".join(f'<a class="btn {"btn-red" if i == 0 else "btn-line"}" href="{u}" rel="noopener" data-track="{t} (resource thanks)">{t}</a>'
                   for i, (t, u) in enumerate(INBOX_LINKS))
    return (
        hero("Almost there", "Check your<br>inbox.",
             f"I just emailed you {r['short']}. Look for <strong>“{r['email_subject']}”</strong> from JR Romero, CSCS "
             f"and tap the download button inside. Not there in a few minutes? Check spam or promotions.",
             btns, short=True, size="h-display")
        + NL.block("light", uid=f"rs-{r['slug']}", default=r["interest"], eyebrow="Want more like this?")
    )


def article_box(slug):
    """Matching resource box for the end of a Notes from the Floor article ('' when none)."""
    r = BY_ARTICLE.get(slug)
    if not r:
        return ""
    return f"""<aside class="rs-box" aria-label="Free resource">
<div class="rs-box-img"><img src="{img(r, 2)}" alt="" width="600" height="776" loading="lazy" decoding="async"></div>
<div class="stack" style="gap:12px">
<span class="eyebrow">Free resource</span>
<h2 class="h-cell">{r['title']}</h2>
<p>{r['card']}</p>
<div class="btns"><a class="btn btn-red" href="{path(r)}" data-track="Resource box: {html.escape(r['title'])}">Get it free</a></div>
</div>
</aside>"""


PAGES = (
    [dict(path="/resources", file="resources.html", active="",
          title="Free Resources | JR Strength & Fitness",
          description="Free worksheets from JR Romero, CSCS for your training and your coaching: the Training Progress Audit and more.",
          body=hub_body())]
    + [dict(path=path(r), file=path(r).lstrip("/") + ".html", active="",
            title=f"{r['title']} | Free Resource | JR Strength & Fitness",
            description=r["card"], body=landing_body(r), og_image=SITE + img(r, 1),
            og_image_alt=f"Cover of {r['title']}", og_image_size=(600, 776))
       for r in LIVE]
    + [dict(path=path(r) + "/thanks", file=path(r).lstrip("/") + "/thanks.html", active="", sitemap=False, noindex=True,
            title=f"Check your inbox | {r['title']} | JR Strength & Fitness", description="Your free resource is on its way to your inbox.", body=thanks_body(r))
       for r in LIVE]
)

SCRIPT = """<script>
(function(){
  """ + NL.OPTIN_JS + """
  document.querySelectorAll('form.rs-form').forEach(function(f){
    f.addEventListener('submit',function(e){
      var st=f.querySelector('.form-status'), btn=f.querySelector('button[type=submit]');
      if(!f.checkValidity()){ e.preventDefault(); st.textContent='Enter a valid email address so I can send it.'; st.hidden=false; f.reportValidity(); return; }
      var fd=new FormData(f); if(fd.get('_honey')){ e.preventDefault(); return; }
      var optin=fd.get('nl_optin')==='yes';
      if(window.va){ window.va('event',{name:'Resource request',data:{resource:f.dataset.resource,newsletter:optin?'yes':'no'}}); }
      if(optin){ kitOptin(f.dataset.nl, fd.get('email_address'), fd.get('fields[first_name]')||'', f.dataset.source); }
      var ob=f.querySelector('[name=nl_optin]'); if(ob){ ob.disabled=true; }
      if(f.dataset.kit){ f.action='https://app.kit.com/forms/'+f.dataset.kit+'/subscriptions'; f.querySelector('[name=_honey]').disabled=true; btn.disabled=true; btn.textContent='Sending…'; return; }
      e.preventDefault();
      var data={_subject:'Resource request: '+f.dataset.title, email:fd.get('email_address'), first_name:fd.get('fields[first_name]')||'',
        resource:f.dataset.resource, newsletter:optin?'yes (Kit confirm sent)':'no', _template:'table', _captcha:'false', page:location.href,
        _autoresponse:'Here is '+f.dataset.title+': '+f.dataset.pdf+'  JR Romero, CSCS, JR Strength & Fitness'};
      btn.disabled=true; btn.textContent='Sending…'; st.hidden=true;
      fetch('""" + FORM_ENDPOINT + """',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
        .catch(function(){}).then(function(){ location.href=f.dataset.thanks; });
    });
  });
})();
</script>"""
