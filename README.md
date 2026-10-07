# jrstrengthandfitness.com

Static site for JR Strength & Fitness, hosted on Vercel.

## Layout
- `src/pages.py` — all page copy. Bracketed `[text]` placeholders still need JR's input.
- `src/layout.py` — shared header, footer, meta tags.
- `src/build.py` — builds HTML, sitemap, share image and favicons into `public/`, and writes `vercel.json` (redirects from the old Squarespace URLs).
- `public/assets/styles.css` — brand styles (Jost, #E10612, charcoal texture).

## Build locally
    pip install pillow
    python3 src/build.py

## Deploy
Import this repo in Vercel (team: JR Strength and Fitness LLC). Vercel reads `vercel.json` for the build command and output folder.

## Before cancelling Squarespace
Keep `public/assets/jr-logo.png` committed. If it's missing, the build downloads the logo from the Squarespace media library, which goes away with the account.

## Not wired yet
Forms (apply, waiver) show a "preview only" message. Choose where submissions go, then replace `FORM_SCRIPT` in `src/pages.py`.
