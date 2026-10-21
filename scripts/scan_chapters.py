import re, os, json, hashlib
src = r"C:\baidunetdiskdownload\开启ICT 2022导师计划的成功之门.pdf"
base = r"C:\Users\Kyle.Gu\Documents\qwen-agent\539xyztXmW\default\books\ict-2022-mentorship"
os.makedirs(base, exist_ok=True)
txt_path = os.path.join(base, "source", "fulltext.txt")
text = open(txt_path, encoding="utf-8").read()

# split by page markers
pages = re.split(r"\n<<<PDFPAGE (\d+) \| images=(\d+)>>>\n", text)
# pages[0] is preface junk; then triples (num, imgs, body)
recs = []
for i in range(1, len(pages), 3):
    num = int(pages[i]); imgs = int(pages[i+1]); body = pages[i+2]
    recs.append((num, imgs, body))
print("PAGE_RECORDS", len(recs))

# Find chapter heading occurrences: a line starting with "Chapter N" that is NOT in TOC pages (4,5)
chap_re = re.compile(r"^\s*Chapter\s*(\d{1,2})\s*$", re.MULTILINE)
hits = {}
for num, imgs, body in recs:
    if num in (4, 5):
        continue
    for m in chap_re.finditer(body):
        c = int(m.group(1))
        hits.setdefault(c, []).append(num)

print("=== CHAPTER -> PDF PAGES (first occurrences) ===")
for c in sorted(hits):
    print(c, hits[c][:4])
