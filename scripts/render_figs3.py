import os, json, hashlib
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
def render(pages, out_name, max_edge=2400):
    out = os.path.join(base, "figures", out_name)
    if os.path.exists(out):
        print("SKIP_EXISTS", out_name); return
    os.makedirs(out, exist_ok=True)
    sha = digest(src)
    doc = pymupdf.open(src)
    manifest = {"schema_version": 1, "source_id": source_id, "source_filename": os.path.basename(src),
        "source_sha256": sha, "pdf_page_count": doc.page_count, "selected_pdf_pages": sorted(pages),
        "max_edge": max_edge, "renderer": "PyMuPDF", "pages": [],
        "note": "仅页面准备；printed_page 需人工核对。"}
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
        open(os.path.join(out, stem + ".txt"), "w", encoding="utf-8").write(txt)
        manifest["pages"].append({"page_id": "%s-%s-p%04d" % (source_id, sha[:12], n),
            "pdf_page": n, "printed_page": None, "image": img,
            "image_sha256": hashlib.sha256(data).hexdigest(),
            "text": stem + ".txt", "text_sha256": hashlib.sha256(txt.encode()).hexdigest(),
            "text_method": "pymupdf",
            "text_status": "present" if txt.strip() else "empty-needs-visual-reading-or-ocr",
            "width": pix.width, "height": pix.height, "review_status": "unreviewed"})
    json.dump(manifest, open(os.path.join(out, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    doc.close()
    print("RENDERED", out_name, len(pages))
render([427, 441, 449], "fig-mmxm")
