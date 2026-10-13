"""Self-host the site's web fonts (no Google Fonts request at page load).

Usage: npm i @fontsource/jost@5 @fontsource/montserrat@5 @fontsource/inter@5 @fontsource/geist-sans@5 @fontsource/geist-mono@5
       python3 tools/self_host_fonts.py path/to/node_modules
Writes public/assets/fonts/*.woff2 and public/assets/fonts/fonts.css (latin + latin-ext only).
"""
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public", "assets", "fonts")
# (package, family name the site's CSS uses, [(weight, style)])
WANT = [
    ("jost", "Jost", [(400, "normal"), (500, "normal"), (600, "normal"), (700, "normal"), (800, "normal"), (700, "italic")]),
    ("montserrat", "Montserrat", [(700, "normal"), (800, "normal")]),
    ("inter", "Inter", [(600, "normal"), (800, "normal")]),
    ("geist-sans", "Geist", [(700, "normal")]),
    ("geist-mono", "Geist Mono", [(500, "normal")]),
]
SUBSETS = ("latin", "latin-ext")


def main(nm):
    os.makedirs(OUT, exist_ok=True)
    rules = []
    for pkg, family, faces in WANT:
        base = os.path.join(nm, "@fontsource", pkg)
        for w, style in faces:
            css = open(os.path.join(base, f"{w}{'-italic' if style == 'italic' else ''}.css")).read()
            for block in re.findall(r"/\* ([^*]+) \*/\s*(@font-face\s*{[^}]*})", css):
                name, rule = block
                if not any(name.startswith(f"{pkg}-{s}-{w}-") for s in SUBSETS):
                    continue
                f = re.search(r"url\(\./files/([^)]+\.woff2)\)", rule).group(1)
                shutil.copy(os.path.join(base, "files", f), os.path.join(OUT, f))
                rule = re.sub(r"font-family:[^;]+;", f"font-family: '{family}';", rule)
                rule = re.sub(r"src:[^;]+;", f"src: url(/assets/fonts/{f}) format('woff2');", rule)
                rules.append(f"/* {name} */\n{rule}")
    open(os.path.join(OUT, "fonts.css"), "w").write("/* Self-hosted from @fontsource (SIL OFL). Regenerate with tools/self_host_fonts.py */\n" + "\n".join(rules) + "\n")
    print(len(rules), "faces;", len(os.listdir(OUT)) - 1, "files")


if __name__ == "__main__":
    main(sys.argv[1])
