"""Turn a stitched phone capture of vault.jrstrengthandfitness.com (585px wide = 1.5x a 390px phone)
into a scrolling screen image (optionally with a pinned header image when the site pins its header), and record the sizes for src/vault_showcase.py.
usage: python3 tools/vault_screens.py NAME capture.png HEADER_PX
"""
import json, os, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public", "assets", "vault")
META = os.path.join(ROOT, "src", "vault_screens.json")

name, src, head_px = sys.argv[1], sys.argv[2], int(sys.argv[3])
im = Image.open(src).convert("RGB")
w, h = im.size
if head_px:
    im.crop((0, 0, w, head_px)).save(os.path.join(OUT, f"{name}-head.webp"), quality=86, method=6)
im.crop((0, head_px, w, h)).save(os.path.join(OUT, f"{name}-body.webp"), quality=82, method=6)
meta = json.load(open(META)) if os.path.exists(META) else {}
meta[name] = {"w": w, "head": head_px, "body": h - head_px}
json.dump(meta, open(META, "w"), indent=2)
print(name, meta[name], os.path.getsize(os.path.join(OUT, f"{name}-body.webp")) // 1024, "KB")
