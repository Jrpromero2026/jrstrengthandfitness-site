"""/review: the page JR sends clients to leave a review. Not in the nav or sitemap; linked from /proof.

Submissions are emailed to JR (FormSubmit, same handler as the application form). Nothing is
published automatically: JR reads each one and adds it to proof.REVIEWS only if the client ticked
the permission box. Posting only some reviews is fine, but /proof must never claim to show all of them.
"""
from ui import hero, sec

STARS = "".join(
    f'<input type="radio" id="rv-{n}" name="rating" value="{n}" required>'
    f'<label for="rv-{n}" title="{n} star{"s" if n > 1 else ""}"><span class="sr">{n} star{"s" if n > 1 else ""}</span>'
    f'<span aria-hidden="true">★</span></label>'
    for n in (1, 2, 3, 4, 5))

AGE = ('<div class="field attest"><label class="choice"><input type="checkbox" name="age_confirmed" value="Yes" required> '
       'I’m 18 or older, or I’m a parent or guardian writing for my child. <span class="req">*</span></label></div>')

BODY = (
    hero("Reviews", "How’s training going?",
         "Tell me honestly. I read every review myself. If you say it’s OK, I’ll post it on my site with your first name and last initial.",
         '<a class="link-u" href="/proof">Read what other clients said →</a>', short=True, size="h-display")
    + sec("light", f"""<form class="form-card" id="review-form" novalidate data-form="review" data-event="Review submitted"
 data-done="Thank you. Your review went straight to me. If you said it’s OK to post, it’ll be on the Proof page soon.">
<input type="hidden" name="_subject" value="Client review">
<input type="hidden" name="_autoresponse" value="Thanks for the review. I read every one myself, and I appreciate you taking the time. JR Romero, JR Strength &amp; Fitness">
<div class="hp" aria-hidden="true"><label>Leave this empty <input type="text" name="_honey" tabindex="-1" autocomplete="off"></label></div>
<div class="row2">
<div class="field"><label for="rv-first">First name <span class="req">*</span></label><input id="rv-first" name="first_name" type="text" autocomplete="given-name" required></div>
<div class="field"><label for="rv-last">Last name <span class="req">*</span></label><input id="rv-last" name="last_name" type="text" autocomplete="family-name" required></div>
</div>
<div class="row2">
<div class="field"><label for="rv-email">Email <span class="req">*</span></label><input id="rv-email" name="email" type="email" autocomplete="email" required aria-describedby="rv-email-note"><span class="hint" id="rv-email-note">Never posted. Only so I can reply.</span></div>
<div class="field"><label for="rv-where">Where did we train? <span class="req">*</span></label><select id="rv-where" name="where" required><option value="">Select one</option><option>Timberhill</option><option>G3</option><option>Online</option></select></div>
</div>
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
<fieldset class="field">
<legend>Posting</legend>
<label class="choice"><input type="checkbox" name="publish_ok" value="Yes"> JR can post this review on jrstrengthandfitness.com with my first name and last initial.</label>
<label class="choice"><input type="checkbox" name="case_file_ok" value="Yes"> I’d be open to sharing my story as a case file. JR will ask before anything is written.</label>
</fieldset>
{AGE}
<p class="form-note">Leave the first box unticked and your review stays private between us. Reviews are posted as written, and I may not post every one. See the <a href="/privacy-policy">Privacy Policy</a>.</p>
<div class="form-status" role="status" hidden></div>
<div class="btns"><button class="btn btn-red" type="submit">Send review</button></div>
</form>""", mark=False)
)
