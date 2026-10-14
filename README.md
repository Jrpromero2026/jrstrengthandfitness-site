# jrstrengthandfitness.com

Static site for JR Strength & Fitness, hosted on Vercel.

## Layout
- `src/pages.py` — all page copy. Bracketed `[text]` placeholders still need JR's input.
- `src/layout.py` — shared header, footer, meta tags.
- `src/build.py` — builds HTML, sitemap, share image and favicons into `public/`, and writes `vercel.json` (redirects from the old Squarespace URLs).
- `public/assets/styles.css` — brand styles (Jost, #E10612, charcoal texture).

## Writing (/writing)
Each post is one Markdown file in `content/writing/<slug>.md`; the slug is the URL. Front matter and the supported Markdown (pull quotes, the copyable "your move" box, images) are documented at the top of `src/writing.py`.

To publish a post:
1. Copy an existing post, change the front matter and write the body. Keep `draft: true` while it's in progress.
2. Optional featured image: put it in `public/assets/writing/` (1600x900 WebP or JPG), then set `image:` and `image_alt:`. It becomes the share image too.
3. Run `python3 src/build.py`, open the draft at `/writing/<slug>` on the Vercel preview and read it on your phone.
4. Delete the `draft: true` line, rebuild, commit. The post then appears on /writing, in the sitemap, the RSS feed (`/writing/feed.xml`) and `llms.txt`.

## Build locally
    pip install pillow
    python3 src/build.py

## Deploy
Vercel serves the prebuilt `public/` folder; it does not run the Python build. After editing `src/`, run `python3 src/build.py` locally and commit the updated `public/` and `vercel.json`.

## Before cancelling Squarespace
Keep `public/assets/jr-logo.png` committed. If it's missing, the build downloads the logo from the Squarespace media library, which goes away with the account.

## Forms
Apply, review and waitlist forms email JR through FormSubmit (`FORM_ENDPOINT` in `src/layout.py`). Newsletter sign-ups go to Kit, one form per interest (`src/newsletter.py`).
