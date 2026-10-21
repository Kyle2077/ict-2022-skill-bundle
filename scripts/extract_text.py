import re, os
from pypdf import PdfReader
src = r"C:\baidunetdiskdownload\开启ICT 2022导师计划的成功之门.pdf"
out_dir = r"C:\Users\Kyle.Gu\Documents\qwen-agent\539xyztXmW\default\books\ict-2022-mentorship\source"
os.makedirs(out_dir, exist_ok=True)
r = PdfReader(src)
n = len(r.pages)
parts = []
img_pages = []
for i, pg in enumerate(r.pages):
    t = pg.extract_text() or ""
    try:
        k = len(pg.images)
    except Exception:
        k = 0
    if k:
        img_pages.append((i+1, k))
    parts.append("\n<<<PDFPAGE %d | images=%d>>>\n%s" % (i+1, k, t))
full = "".join(parts)
with open(os.path.join(out_dir, "fulltext.txt"), "w", encoding="utf-8") as f:
    f.write(full)
print("PDF_PAGES", n)
print("CHARS", len(full))
print("PAGES_WITH_IMAGES", len(img_pages))
print("TOTAL_IMAGES", sum(k for _, k in img_pages))
# dense image pages (likely chart-heavy chapters)
dense = sorted(img_pages, key=lambda x: -x[1])[:15]
print("TOP_IMAGE_PAGES", dense)
