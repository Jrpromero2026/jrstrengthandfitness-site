# jrstrengthandfitness.com

Static site for JR Strength & Fitness, hosted on Vercel.

## Layout
- `src/pages.py` — all page copy. Bracketed `[text]` placeholders still need JR's input.
- `src/layout.py` — shared header, footer, meta tags.
- `src/build.py` — builds HTML, sitemap, share image and favicons into `public/`, and writes `vercel.json` (redirects from the old Squarespace URLs).
- `public/assets/styles.css` — brand styles (Jost, #E10612, charcoal texture).

## Notes from the Floor (/notes)
The articles section and the newsletter share one name: Notes from the Floor. It lives at /notes; old /notes and /blog links redirect there.
Each post is one Markdown file in `content/notes/<slug>.md`; the slug is the URL. Front matter and the supported Markdown (pull quotes, the copyable Proven box, images) are documented at the top of `src/notes.py`.

To publish a post:
1. Copy an existing post, change the front matter and write the body. Keep `draft: true` while it's in progress.
2. Optional featured image: put it in `public/assets/notes/` (1600x900 WebP or JPG), then set `image:` and `image_alt:`. It becomes the share image too.
3. Run `python3 src/build.py`, open the draft at `/notes/<slug>` on the Vercel preview and read it on your phone.
4. Delete the `draft: true` line, rebuild, commit. The build also makes the post's share card (`public/assets/share/<slug>.jpg`, from `src/sharecard.py`), using the post's `image` when it has one, otherwise JR's portrait. The post then appears on /notes, in the sitemap, the RSS feed (`/notes/feed.xml`) and `llms.txt`.

## NASM-CPT Exam Prep (/projects/vault/exam-prep)

Marketing page only: checkout, accounts and the app live in the Vault. Every buy button goes to
`vault.jrstrengthandfitness.com/pricing#exam-prep`. Copy, prices and the required NASM disclaimer are in
`src/examprep.py`; the Vault pricing page is the source of truth for prices. The build fails if the page
uses a banned claim (official, guarantee, real/leaked questions, pass rates). Short links: /exam-prep,
/nasm-cpt-exam-prep.

## Free resources (/resources)

Lead magnets live in `src/resources.py`: the /resources hub, one landing page per resource and a thanks page with the
download. PDFs are in `public/resources/`, page images in `public/assets/resources/`. Each resource needs a Kit form ID
(`kit_form`); until it's filled in, requests are emailed to JR through FormSubmit and the visitor still gets the download.
The Kit setup steps are at the top of `src/resources.py`. A matching resource box appears at the end of its article.

## Build locally
    pip install pillow
    python3 src/build.py

## Deploy
Vercel serves the prebuilt `public/` folder; it does not run the Python build. After editing `src/`, run `python3 src/build.py` locally and commit the updated `public/` and `vercel.json`.

## Before cancelling Squarespace
Keep `public/assets/jr-logo.png` committed. If it's missing, the build downloads the logo from the Squarespace media library, which goes away with the account.

## Forms
Apply, review and waitlist forms email JR through FormSubmit (`FORM_ENDPOINT` in `src/layout.py`). Newsletter sign-ups go to Kit, one form per interest (`src/newsletter.py`).
