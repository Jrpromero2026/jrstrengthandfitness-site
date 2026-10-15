"""/review: the page JR sends clients to leave a review or share their story as a case file.
Not in the nav or sitemap; linked from /proof. /review?type=case opens straight on the case-file option.

Submissions are emailed to JR (FormSubmit, same handler as the application form). Nothing is
published automatically:
- Reviews go into proof.REVIEWS only if the client ticked publish_ok.
- Case files are written by JR from the client's answers and posted only after the client approves
  the final version (case_ok). Posting only some reviews is fine, but /proof must never claim to show all.

Only the chosen section shows; the other is disabled, so it is neither validated nor sent.
(The form sends through JavaScript like every form on the site.)
"""
import json

from ui import hero, sec

STARS = "".join(
    f'<input type="radio" id="rv-{n}" name="rating" value="{n}" required>'
    f'<label for="rv-{n}" title="{n} star{"s" if n > 1 else ""}"><span class="sr">{n} star{"s" if n > 1 else ""}</span>'
    f'<span aria-hidden="true">★</span></label>'
    for n in (1, 2, 3, 4, 5))

AGE = ('<div class="field attest"><label class="choice"><input type="checkbox" name="age_confirmed" value="Yes" required> '
       '<span>I’m 18 or older, or I’m a parent or guardian writing for my child. <span class="req">*</span></span></label></div>')

MODES = {
    "review": dict(subject="Client review", event="Review submitted",
                   done="Thank you. Your review went straight to me. If you said it’s OK to post, it’ll be on the Proof page soon.",
                   reply="Thanks for the review. I read every one myself, and I appreciate you taking the time. JR Prieto-Romero, JR Strength &amp; Fitness"),
    "case": dict(subject="Case file submission", event="Case file submitted",
                 done="Thank you for sharing your story. I’ll write a draft and send it to you. Nothing is posted until you approve it.",
                 reply="Thanks for sharing your story. I’ll write a draft of your case file and send it to you to approve. Nothing goes on the site until you say it’s right. JR Prieto-Romero, JR Strength &amp; Fitness"),
}
R, C = MODES["review"], MODES["case"]

BODY = (
    hero("Reviews", "How’s training going?",
         "Leave a quick review, or share your story as a case file. I read every one myself, and nothing goes on my site without your OK.",
         '<a class="link-u" href="/proof">Read what other clients said →</a>', short=True, size="h-display")
    + sec("light", f"""<form class="form-card" id="review-form" novalidate data-form="review" data-event="{R['event']}" data-done="{R['done']}">
<input type="hidden" name="_subject" value="{R['subject']}">
<input type="hidden" name="_autoresponse" value="{R['reply']}">
<div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>

<fieldset class="field rv-pick">
<legend>What would you like to share? <span class="req">*</span></legend>
<div class="rv-modes">
<label class="rv-mode"><input type="radio" name="kind" value="review" checked><span><b>A review</b><em>A few lines and a star rating. Takes about 2 minutes.</em></span></label>
<label class="rv-mode"><input type="radio" name="kind" value="case"><span><b>My story, as a case file</b><em>Where you started and where you are now. I’ll write it up and you approve it before it’s posted.</em></span></label>
</div>
</fieldset>

<div class="row2">
<div class="field"><label for="rv-first">First name <span class="req">*</span></label><input id="rv-first" name="first_name" type="text" autocomplete="given-name" required></div>
<div class="field"><label for="rv-last">Last name <span class="req">*</span></label><input id="rv-last" name="last_name" type="text" autocomplete="family-name" required></div>
</div>
<div class="row2">
<div class="field"><label for="rv-email">Email <span class="req">*</span></label><input id="rv-email" name="email" type="email" autocomplete="email" required aria-describedby="rv-email-note"><span class="hint" id="rv-email-note">Never posted. Only so I can reply.</span></div>
<div class="field"><label for="rv-where">Where did we train? <span class="req">*</span></label><select id="rv-where" name="where" required><option value="">Select one</option><option>Timberhill</option><option>G3</option><option>Online</option></select></div>
</div>

<fieldset class="rv-sec" data-mode="review">
<legend class="rv-sec-h">Your review</legend>
<fieldset class="field">
<legend>What are you reviewing? <span class="req">*</span></legend>
<div class="choices">
<label class="choice"><input type="radio" name="type" value="Training" required> Training with me</label>
<label class="choice"><input type="radio" name="type" value="Consult"> A consult</label>
</div>
</fieldset>
<fieldset class="field">
<legend>Rating <span class="req">*</span></legend>
<div class="stars">{STARS}</div>
</fieldset>
<div class="field"><label for="rv-text">Your review <span class="req">*</span></label><textarea id="rv-text" name="review" required minlength="10" rows="6" aria-describedby="rv-text-note"></textarea><span class="hint" id="rv-text-note">What was it like? What’s changed for you?</span></div>
<label class="choice"><input type="checkbox" name="publish_ok" value="Yes"> JR can post this review on jrstrengthandfitness.com with my first name and last initial.</label>
<p class="form-note">Leave that box unticked and your review stays private between us. Reviews are posted as written, and I may not post every one.</p>
</fieldset>

<fieldset class="rv-sec" data-mode="case" hidden disabled>
<legend class="rv-sec-h">Your story</legend>
<div class="row2">
<div class="field"><label for="cf-type">How do we train? <span class="req">*</span></label><select id="cf-type" name="case_mode" required><option value="">Select one</option><option>In person</option><option>Online</option><option>Athlete</option></select></div>
<div class="field"><label for="cf-len">How long have we trained together? <span class="req">*</span></label><input id="cf-len" name="case_length" type="text" required placeholder="e.g. 8 months"></div>
</div>
<div class="field"><label for="cf-start">Where were you when you started? <span class="req">*</span></label><textarea id="cf-start" name="case_start" required minlength="10" rows="5" aria-describedby="cf-start-note"></textarea><span class="hint" id="cf-start-note">In your own words. Pain, an injury, stalled progress, never lifted before, whatever was true.</span></div>
<div class="field"><label for="cf-now">Where are you now? <span class="req">*</span></label><textarea id="cf-now" name="case_now" required minlength="10" rows="5" aria-describedby="cf-now-note"></textarea><span class="hint" id="cf-now-note">What’s different, and what can you do now that you couldn’t before?</span></div>
<div class="field"><label for="cf-nums">Any numbers that show the change?</label><textarea id="cf-nums" name="case_results" rows="3" aria-describedby="cf-nums-note"></textarea><span class="hint" id="cf-nums-note">Optional. Lifts, pain levels, sessions a week, a race time. Up to three is plenty.</span></div>
<label class="choice"><input type="checkbox" name="photo_ok" value="Yes"> I’m open to sharing a photo for my case file. JR will ask first.</label>
<label class="choice"><input type="checkbox" name="case_ok" value="Yes" required> <span>JR can write a case file from my answers. It’s posted with my first name only after I approve the final version. <span class="req">*</span></span></label>
</fieldset>

{AGE}
<p class="form-note">See the <a href="/privacy-policy">Privacy Policy</a> for how this is handled.</p>
<div class="form-status" role="status" hidden></div>
<div class="btns"><button class="btn btn-red" type="submit">Send</button></div>
</form>""", mark=False)
)

SCRIPT = """<script>
(function(){
  var f=document.getElementById('review-form'); if(!f) return;
  var M=""" + json.dumps({k: {"subject": v["subject"], "event": v["event"], "done": v["done"], "reply": v["reply"].replace("&amp;", "&")} for k, v in MODES.items()}, ensure_ascii=False) + """;
  var secs=f.querySelectorAll('.rv-sec');
  function set(kind){
    secs.forEach(function(s){ var on=s.getAttribute('data-mode')===kind; s.hidden=!on; s.disabled=!on; });
    var m=M[kind]; f.querySelector('[name=_subject]').value=m.subject; f.querySelector('[name=_autoresponse]').value=m.reply;
    f.setAttribute('data-done',m.done); f.setAttribute('data-event',m.event);
  }
  f.querySelectorAll('[name=kind]').forEach(function(r){ r.addEventListener('change',function(){ set(r.value); }); });
  var want=new URLSearchParams(location.search).get('type')==='case'?'case':'review';
  f.querySelector('[name=kind][value='+want+']').checked=true; set(want);
  f.addEventListener('reset',function(){ setTimeout(function(){ set(f.querySelector('[name=kind]:checked').value); },0); });
})();
</script>"""
