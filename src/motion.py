"""Site motion: scroll reveals, the IAOE ladder, and the hero credential count-up.

Everything starts visible. Motion only runs when <html> has the "m" class, which the <head> sets
when the browser supports IntersectionObserver and the visitor hasn't asked for reduced motion.
The hero entrance itself is pure CSS (see "Motion" in styles.css).
"""

MOTION_JS = """<script>
(function(){
  var root=document.documentElement; if(!root.classList.contains('m')) return;

  /* 1. Scroll reveal: blocks rise in as they enter view, siblings staggered. Skips anything already on screen. */
  var SEL=['.sec .head-row','.panel.brands .cell','.sec .split > .main','.sec .split > .side','.sec .facts',
           '.sec .rows:not(.ladder) .row','.for-row','.post-row','.sec .info-card','.sec .form-card','.post-cta','.closing .wrap > *','.pf-case','.pf-rc','.pf-soon'];
  var items=[].slice.call(document.querySelectorAll(SEL.join(','))).filter(function(el){
    return !el.closest('.hero') && !el.closest('.vs') && !el.closest('.ladder') && el.getBoundingClientRect().top > innerHeight*0.92;
  });
  items=items.filter(function(el){ return !items.some(function(o){ return o!==el && o.contains(el); }); });  /* outermost only */
  var io=new IntersectionObserver(function(es){ es.forEach(function(e){
    if(!e.isIntersecting) return; var el=e.target; io.unobserve(el);
    var sib=[].slice.call(el.parentNode.children).filter(function(c){ return c.classList.contains('rv'); });
    el.style.transitionDelay=Math.min(sib.indexOf(el),5)*90+'ms';
    el.classList.add('rv-in');
    setTimeout(function(){ el.style.transitionDelay=''; }, 1600);
  }); },{rootMargin:'0px 0px -8% 0px'});
  items.forEach(function(el){ el.classList.add('rv'); io.observe(el); });

  /* 2. IAOE ladder: rungs light up in order, Enhanced last. */
  document.querySelectorAll('[data-ladder]').forEach(function(l){
    l.classList.add('armed');
    var lo=new IntersectionObserver(function(es){ if(es[0].isIntersecting){ l.classList.add('go'); lo.disconnect(); } },{threshold:0.35});
    lo.observe(l);
  });

  /* 3. Hero credential count-up (20,000 hrs). */
  document.querySelectorAll('.hero [data-countup]').forEach(function(n){
    var end=+n.getAttribute('data-countup'), t0=null; n.textContent='0';
    setTimeout(function(){ requestAnimationFrame(function step(t){
      if(!t0) t0=t; var p=Math.min(1,(t-t0)/1600);
      n.textContent=Math.round(end*(1-Math.pow(1-p,3))).toLocaleString('en-US');
      if(p<1) requestAnimationFrame(step);
    }); },1100);
  });
})();
</script>"""
