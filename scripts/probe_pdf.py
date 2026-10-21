from pypdf import PdfReader
p = r"C:\baidunetdiskdownload\开启ICT 2022导师计划的成功之门.pdf"
r = PdfReader(p)
n = len(r.pages)
print("PAGES", n)
print("META", {k: str(v)[:60] for k, v in (r.metadata or {}).items()})
empty = 0
samples = []
imgs = 0
for i, pg in enumerate(r.pages):
    t = (pg.extract_text() or "").strip()
    if len(t) < 20:
        empty += 1
    try:
        imgs += len(pg.images)
    except Exception:
        pass
    if i in (0, 1, 2, 3, 4, 5, n//2, n-1):
        samples.append((i+1, len(t), t[:200].replace("\n", " | ")))
print("LOW_TEXT_PAGES", empty, "of", n)
print("IMAGE_COUNT_APPROX", imgs)
for s in samples:
    print("---PAGE", s[0], "len", s[1])
    print(s[2])
