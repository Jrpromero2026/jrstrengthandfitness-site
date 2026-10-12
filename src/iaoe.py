"""The Standard: JR's IAOE model (Inadequate, Adequate, Optimal, Enhanced) applied across five areas.

Coaching tiers are JR's stated model. The other four areas are drafted from his principles
(adequate is a legitimate target; enhanced is for finer margins) and approved by JR before publishing.
"""
from ui import rows

TIERS = ("Inadequate", "Adequate", "Optimal", "Enhanced")

# area key, tab label, intro line, [(label, description) x 4 in tier order]
AREAS = [
    ("coaching", "Coaching", "Who coaches the person, and at what level.", [
        ("Below the line", "Unsafe, unstructured or not progressing."),
        ("Fitness trainer", "Safe, effective and progressing. The right target for many clients."),
        ("Fitness coach", "Individualized programming built around the person’s goals."),
        ("Performance coach", "Where I coach: trained athletes who have plateaued and want finer margins."),
    ]),
    ("programs", "Training programs", "What the plan on paper actually does.", [
        ("Random", "Workouts with no plan: no progression, no reason behind exercise choice, injury risk left to chance."),
        ("Structured", "Progressive overload, balanced movement patterns and safe technique. Enough for most people to keep progressing."),
        ("Individualized", "Built around the person’s goals, history, schedule and limitations, with planned phases and adjustments."),
        ("Periodized for margins", "Advanced periodization and specific methods for trained athletes chasing the last few percent."),
    ]),
    ("nutrition", "Nutrition", "How the eating supports the training.", [
        ("No plan", "Under-fueled or unstructured eating that works against the training."),
        ("Consistent basics", "Enough protein, enough total energy and regular meals to support training and recovery."),
        ("Targets", "Calorie and macro targets matched to the goal and training load, adjusted as progress comes in."),
        ("Precision fueling", "Timing, periodized intake and competition fueling where small margins matter."),
    ]),
    ("trainers", "Trainer development", "How coaches are qualified, educated and held to a standard.", [
        ("Unverified", "Credentials nobody checked, no continuing education and no standard to coach to."),
        ("Accredited", "An accredited certification and safe, effective sessions. A legitimate place to start."),
        ("Developing", "Ongoing education, mentorship and real systems: consultations, programming frameworks and client tools."),
        ("Specialized", "Advanced credentials and specialization, such as performance coaching for athletes."),
    ]),
    ("experience", "Client experience", "What it feels like to be the client, from first contact on.", [
        ("Ad hoc", "No consult, no onboarding and no follow-up. Clients drift and leave."),
        ("Consistent", "A real consult, a clear start and regular check-ins."),
        ("Coordinated", "Intake, programming, scheduling and check-ins in one system, so nothing falls through."),
        ("Proactive", "Readiness data, reviews and adjustments made before problems show up."),
    ]),
]


def _ladder(items):
    data = []
    for i, (tier, (label, desc)) in enumerate(zip(TIERS, items)):
        d = dict(n=f"0{i + 1}", k=label, t=tier, d=desc)
        if i == 0:
            d["cls"] = "dim"
        if i == 3:
            d["cls"] = "hot"
        data.append(d)
    return rows(data).replace('<div class="rows">', '<div class="rows ladder" data-ladder>', 1)


def block():
    tabs = "".join(
        f'<button type="button" role="tab" id="iaoe-tab-{k}" aria-controls="iaoe-{k}" aria-selected="{"true" if i == 0 else "false"}"'
        f'{"" if i == 0 else " tabindex=\"-1\""}>{label}</button>'
        for i, (k, label, _, _) in enumerate(AREAS))
    panels = "".join(
        f'<div class="iaoe-panel" role="tabpanel" id="iaoe-{k}" aria-labelledby="iaoe-tab-{k}"{"" if i == 0 else " hidden"}>'
        f'<p class="iaoe-intro">{intro}</p>{_ladder(items)}</div>'
        for i, (k, _, intro, items) in enumerate(AREAS))
    return f"""<div class="iaoe" data-iaoe>
<div class="iaoe-tabs" role="tablist" aria-label="Where IAOE applies">{tabs}</div>
{panels}
</div>
<script>
(function(){{
  var root=document.querySelector('[data-iaoe]'); if(!root) return;
  var tabs=[].slice.call(root.querySelectorAll('[role=tab]'));
  function show(t, focus){{
    tabs.forEach(function(x){{ var on=x===t; x.setAttribute('aria-selected', on); x.tabIndex=on?0:-1;
      var p=document.getElementById(x.getAttribute('aria-controls')); p.hidden=!on;
      if(on){{ var l=p.querySelector('[data-ladder]'); if(l && l.classList.contains('armed')){{ l.classList.remove('go'); void l.offsetWidth; l.classList.add('go'); }} }}
    }});
    if(focus) t.focus();
  }}
  tabs.forEach(function(t,i){{
    t.addEventListener('click',function(){{ show(t); }});
    t.addEventListener('keydown',function(e){{
      var j = e.key==='ArrowRight' ? (i+1)%tabs.length : e.key==='ArrowLeft' ? (i-1+tabs.length)%tabs.length : e.key==='Home' ? 0 : e.key==='End' ? tabs.length-1 : -1;
      if(j>=0){{ e.preventDefault(); show(tabs[j], true); }}
    }});
  }});
}})();
</script>"""
