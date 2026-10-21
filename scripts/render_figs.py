import os, json, hashlib, re
import pymupdf

src = r"C:\baidunetdiskdownload\开启ICT 2022导师计划的成功之门.pdf"
base = r"C:\Users\Kyle.Gu\Documents\qwen-agent\539xyztXmW\default\books\ict-2022-mentorship"
source_id = "src-ict2022"

def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def render(pages, out_name, max_edge=2400, printed_page=None):
    out = os.path.join(base, "figures", out_name)
    if os.path.exists(out):
        raise SystemExit("OUT_EXISTS " + out)
    os.makedirs(out, exist_ok=True)
    sha = digest(src)
    doc = pymupdf.open(src)
    total = doc.page_count
    manifest = {
        "schema_version": 1, "source_id": source_id,
        "source_filename": os.path.basename(src), "source_sha256": sha,
        "pdf_page_count": total, "selected_pdf_pages": sorted(pages),
        "max_edge": max_edge, "renderer": "PyMuPDF (Poppler unavailable)", "pages": [],
        "note": "仅页面准备，未执行 OCR 或视觉理解；printed_page 需人工核对。路径相对于本清单。",
    }
    for n in sorted(pages):
        pg = doc[n - 1]
        r = pg.rect
        scale = max_edge / max(r.width, r.height)
        pix = pg.get_pixmap(matrix=pymupdf.Matrix(scale, scale), alpha=False)
        stem = "page-%04d" % n
        img = stem + ".png"
        pix.save(os.path.join(out, img))
        data = open(os.path.join(out, img), "rb").read()
        txt = pg.get_text()
        with open(os.path.join(out, stem + ".txt"), "w", encoding="utf-8") as f:
            f.write(txt)
        manifest["pages"].append({
            "page_id": "%s-%s-p%04d" % (source_id, sha[:12], n),
            "pdf_page": n, "printed_page": printed_page if len(pages) == 1 else None,
            "image": img, "image_sha256": hashlib.sha256(data).hexdigest(),
            "text": stem + ".txt", "text_sha256": hashlib.sha256(txt.encode()).hexdigest(),
            "text_method": "pymupdf",
            "text_status": "present" if txt.strip() else "empty-needs-visual-reading-or-ocr",
            "width": pix.width, "height": pix.height, "review_status": "unreviewed",
        })
    json.dump(manifest, open(os.path.join(out, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    doc.close()
    print("RENDERED", out_name, len(pages), "pages ->", out)
    return out

# 关键图页组：FVG 结构 / ERL-IRL / PO3 序列 / 2022 模型图 / Breaker / CBDR / Ch32 清单
groups = {
    "fig-fvg": [140, 141, 147, 149, 150, 151],
    "fig-liquidity": [43, 45, 47, 52, 57],
    "fig-po3": [216, 224, 225, 226, 227],
    "fig-model-diagram": [407, 408, 409, 410],
    "fig-breaker": [550, 551, 554, 555, 557, 559],
    "fig-cbdr": [622, 623, 624],
    "fig-ch32": [628, 629, 632, 634, 635],
}
for name, pgs in groups.items():
    render(pgs, name)
