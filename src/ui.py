"""Small HTML helpers for the v2 layout: heroes, themed sections, heading rows, numbered rows."""
from layout import GRAIN


def ph(text):
    """Visible placeholder for copy or media JR still needs to supply."""
    return f'<span class="placeholder">[{text}]</span>'


def hero(eyebrow, title, lead="", btns="", side="", short=False, size="h-hero"):
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    btn_html = f'<div class="btns" style="padding-top:6px">{btns}</div>' if btns else ""
    main = f"""<div class="main stack" style="gap:24px">
<span class="eyebrow">{eyebrow}</span>
<h1 class="{size}">{title}</h1>
{lead_html}
{btn_html}
</div>"""
    side_html = f'<div class="side">{side}</div>' if side else ""
    return f"""<section class="hero dark{' short' if short else ''}">
{GRAIN}
<img class="watermark" src="/assets/jr-watermark.png" alt="" aria-hidden="true">
<div class="wrap split">
{main}
{side_html}
</div>
</section>"""


def sec(theme, inner, mark=True, id=None, tight=False, label=None):
    cls = f"sec {theme}" + (" mark" if mark else "") + (" tight" if tight else "")
    attrs = (f' id="{id}"' if id else "") + (f' aria-label="{label}"' if label else "")
    return f'<section class="{cls}"{attrs}><div class="wrap">{inner}</div></section>'


def head_row(eyebrow, title, para=None, level="h2", size="h-display"):
    p = f"<p>{para}</p>" if para else ""
    return f"""<div class="head-row">
<div class="h"><span class="eyebrow">{eyebrow}</span><{level} class="{size}">{title}</{level}></div>
{p}
</div>"""


def rows(items):
    """items: (n, k, t, d) tuples, or dicts with an optional 'cls' ('dim' / 'hot')."""
    out = []
    for it in items:
        if isinstance(it, dict):
            n, k, t, d, cls = it["n"], it.get("k", ""), it["t"], it.get("d", ""), it.get("cls", "")
        else:
            (n, k, t, d), cls = it, ""
        out.append(
            f'<div class="row {cls}"><span class="n">{n}</span><span class="k">{k}</span>'
            f'<span class="t">{t}</span><span class="d">{d}</span></div>'
        )
    return f'<div class="rows">{"".join(out)}</div>'


# Real photos go here as they come in: label -> (path under /assets, alt text).
PHOTOS = {}


def frame(label, wide=False, card=""):
    """Photo slot. Until JR supplies the photo for `label`, shows a branded panel instead of a placeholder."""
    cls = "frame with-card" if card else "frame"
    w = " wide" if wide else ""
    if label in PHOTOS:
        src, alt = PHOTOS[label]
        media = f'<div class="media photo{w}"><img src="{src}" alt="{alt}" loading="lazy"></div>'
    else:
        media = (f'<div class="media brand-fill{w}" aria-hidden="true"><!-- photo slot: {label} -->'
                 f'<img src="/assets/jr-mark.png" alt=""></div>')
    return f'<div class="{cls}">{media}{card}</div>'


def ext(href):
    return "" if href.startswith(("/", "mailto:", "#")) else ' rel="noopener"'
