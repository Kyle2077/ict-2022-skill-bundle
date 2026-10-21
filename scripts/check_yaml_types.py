import yaml, os
p = r"C:\Users\Kyle.Gu\Documents\qwen-agent\539xyztXmW\default\books\ict-2022-mentorship\.cangjie\capabilities\verified.yaml"
d = yaml.safe_load(open(p, encoding="utf-8"))
bad = []
for c in d["capabilities"]:
    for field in ("keywords", "intents", "also_read"):
        for i, v in enumerate(c.get(field, [])):
            if not isinstance(v, str):
                bad.append((c["slug"], field, i, repr(v)))
print("BAD_ITEMS", bad)
print("CAPS", len(d["capabilities"]))
