import os, yaml, re
base = r"C:\Users\Kyle.Gu\Documents\qwen-agent\539xyztXmW\default\books\ict-2022-mentorship"
vy = os.path.join(base, ".cangjie", "capabilities", "verified.yaml")
ap = os.path.join(base, ".cangjie", "capabilities", "_append_caps.yaml")
t = open(vy, encoding="utf-8").read()
add = open(ap, encoding="utf-8").read()
if "cap.ict2022.market-structure-hierarchy" in t:
    print("ALREADY_MERGED"); raise SystemExit
# router entry count update
t2 = t.replace("按意图把请求路由到 15 张能力卡", "按意图把请求路由到 28 张能力卡")
merged = t2.rstrip("\n") + "\n" + add
open(vy, "w", encoding="utf-8").write(merged)
d = yaml.safe_load(open(vy, encoding="utf-8"))
caps = d["capabilities"]
print("TOTAL_CAPS", len(caps))
print("SLUGS", [c["slug"] for c in caps])
promoted = [c["slug"] for c in caps if c.get("promotion", {}).get("destination") == "promoted"]
print("PROMOTED", len(promoted), promoted)
missing = []
for c in caps:
    card = os.path.join(base, ".cangjie", "capabilities", c["card"].replace("/", os.sep))
    if not os.path.exists(card):
        missing.append(c["card"])
    for r in c.get("resources", []):
        rp = os.path.join(base, ".cangjie", "capabilities", r.replace("/", os.sep))
        if not os.path.exists(rp):
            missing.append(r)
    for v in c.get("visual_evidence", []):
        for k in ("image", "notes"):
            p = os.path.join(base, ".cangjie", "capabilities", v[k].replace("/", os.sep))
            if not os.path.exists(p):
                missing.append(v[k])
        if "detail_image" in v:
            p = os.path.join(base, ".cangjie", "capabilities", v["detail_image"].replace("/", os.sep))
            if not os.path.exists(p):
                missing.append(v["detail_image"])
print("MISSING_FILES", missing)
ids = [c["capability_id"] for c in caps]
print("DUP_IDS", [i for i in set(ids) if ids.count(i) > 1])
slugs = [c["slug"] for c in caps]
print("DUP_SLUGS", [s for s in set(slugs) if slugs.count(s) > 1])
