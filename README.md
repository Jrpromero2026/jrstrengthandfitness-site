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
Vercel serves the prebuilt `public/` folder; it does not run the Python build. After editing `src/`, run `python3 src/build.py` locally and commit the updated `public/` and `vercel.json`.

## Before cancelling Squarespace
Keep `public/assets/jr-logo.png` committed. If it's missing, the build downloads the logo from the Squarespace media library, which goes away with the account.

## Not wired yet
Forms (apply, waiver) show a "preview only" message. Choose where submissions go, then replace `FORM_SCRIPT` in `src/pages.py`.
