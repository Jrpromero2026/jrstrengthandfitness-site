"""Newsletter sign-up: one list, tagged by interest.

Runs on Kit. JR makes three Kit forms, one per interest, and pastes each form's ID below.
Each form's success setting should redirect to https://www.jrstrengthandfitness.com/subscribed.
Until an ID is filled in, sign-ups for that interest are emailed to JR through FormSubmit
(subject "Newsletter signup") so nobody is lost; import them into Kit later.
"""
import json

from layout import FORM_ENDPOINT
from ui import hero, sec

KIT_FORMS = {
    "coach": "10028376",     # Kit form: "Newsletter: Coaches"
    "training": "10028379",  # Kit form: "Newsletter: Training"
    "women": "10028394",     # Kit form: "Newsletter: Women's training"
}
INTERESTS = [
    ("coach", "I coach or train others"),
    ("training", "My own training"),
    ("women", "Strength training for women"),
]
PITCH = ("What I’m testing with clients and coaches, new writing, and first word when TRAINCND "
         "and The Credential Standard open. No spam. Unsubscribe anytime.")


def form(uid, default="coach", compact=False):
    choices = "".join(
        f'<label class="choice"><input type="radio" name="interest" value="{k}"{" checked" if k == default else ""}> {t}</label>'
        for k, t in INTERESTS)
    name_field = "" if compact else (
        f'<div class="field"><label for="nl-first-{uid}">First name</label>'
        f'<input id="nl-first-{uid}" name="fields[first_name]" type="text" autocomplete="given-name"></div>')
    return f"""<form class="form-card nl-form" method="post" action="/newsletter" novalidate data-newsletter>
<div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
{name_field}
<div class="field"><label for="nl-email-{uid}">Email <span class="req">*</span></label>
<input id="nl-email-{uid}" name="email_address" type="email" autocomplete="email" required></div>
<fieldset class="field"><legend>I’m most interested in</legend><div class="choices">{choices}</div></fieldset>
<div class="form-status" role="status" hidden></div>
<div class="btns"><button class="btn btn-red" type="submit">Join the list</button></div>
<p class="form-note">See the <a href="/privacy-policy">Privacy Policy</a>.</p>
</form>"""


def block(theme="dark", uid="s", default="coach", eyebrow="The newsletter", title="Notes from<br>the floor.", mark=True):
    inner = f"""<div class="split nl">
<div class="main stack" style="gap:20px"><span class="eyebrow">{eyebrow}</span>
<h2 class="h-display">{title}</h2>
<p class="lead">{PITCH}</p></div>
<div class="side">{form(uid, default)}</div>
</div>"""
    return sec(theme, inner, mark=mark, id="newsletter", label="Newsletter")


PAGE = (
    hero("The newsletter", "Notes from<br>the floor.", PITCH,
         side=form("p"), short=True, size="h-display")
)

THANKS = (
    hero("You’re in", "Check your<br>inbox.",
         "One last step: open the email I just sent and confirm your subscription. "
         "If it isn’t there in a few minutes, check your spam or promotions folder.",
         '<a class="btn btn-red" href="/writing">Read the writing</a>'
         '<a class="link-u" href="/projects">See what I’m building →</a>',
         short=True, size="h-display")
)

SCRIPT = """<script>
(function(){
  var KIT=""" + json.dumps(KIT_FORMS) + """;
  window.addEventListener('pageshow',function(){ document.querySelectorAll('form[data-newsletter]').forEach(function(f){ f.querySelectorAll('[disabled]').forEach(function(i){ i.disabled=false; }); var b=f.querySelector('button[type=submit]'); if(b){ b.textContent='Join the list'; } }); });
  document.querySelectorAll('form[data-newsletter]').forEach(function(f){
    f.addEventListener('submit',function(e){
      var st=f.querySelector('.form-status'), btn=f.querySelector('button[type=submit]');
      if(!f.checkValidity()){ e.preventDefault(); st.textContent='Please enter your email.'; st.hidden=false; f.reportValidity(); return; }
      var fd=new FormData(f); if(fd.get('_honey')){ e.preventDefault(); return; }
      var interest=fd.get('interest')||'coach';
      if(window.va){ window.va('event',{name:'Newsletter signup',data:{interest:interest,page:location.pathname}}); }
      if(KIT[interest]){ f.action='https://app.kit.com/forms/'+KIT[interest]+'/subscriptions'; f.querySelectorAll('[name=_honey],[name=interest]').forEach(function(i){ i.disabled=true; }); btn.disabled=true; btn.textContent='Joining…'; return; }
      e.preventDefault();
      var data={_subject:'Newsletter signup ('+interest+')', email:fd.get('email_address'), first_name:fd.get('fields[first_name]')||'', interest:interest,
        _template:'table', _captcha:'false', page:location.href,
        _autoresponse:'You’re on the list. I’ll be in touch with notes from the floor, new writing and project launches. JR Prieto-Romero, JR Strength & Fitness'};
      btn.disabled=true; var label=btn.textContent; btn.textContent='Sending…'; st.hidden=true;
      fetch('""" + FORM_ENDPOINT + """',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
        .then(function(r){ return r.json().catch(function(){return {};}).then(function(j){ if(!r.ok||String(j.success)==='false'){ throw new Error('send failed'); } }); })
        .then(function(){ f.reset(); st.textContent='You’re on the list. Watch your inbox.'; st.hidden=false; btn.textContent=label; btn.disabled=false; })
        .catch(function(){ st.textContent='Something went wrong. Please email jr@jrstrengthandfitness.com and I’ll add you.'; st.hidden=false; btn.textContent=label; btn.disabled=false; });
    });
  });
})();
</script>"""
