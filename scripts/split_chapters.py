import re, os, json
base = r"C:\Users\Kyle.Gu\Documents\qwen-agent\539xyztXmW\default\books\ict-2022-mentorship"
text = open(os.path.join(base, "source", "fulltext.txt"), encoding="utf-8").read()
parts = re.split(r"\n<<<PDFPAGE (\d+) \| images=(\d+)>>>\n", text)
recs = []
for i in range(1, len(parts), 3):
    recs.append((int(parts[i]), int(parts[i+1]), parts[i+2]))

# chapter start pdf pages from scan
starts = {1:14,2:22,3:39,4:80,5:84,6:88,7:95,8:101,9:112,10:139,11:155,12:181,13:215,14:266,15:301,16:332,17:383,18:399,19:406,20:468,21:477,22:482,23:492,24:497,25:508,26:515,27:523,28:537,29:547,30:617,31:622,32:627,33:660}
titles = {1:"Introduction to Intraday Trading and Price Action",2:"Elements To A Trade Setup",3:"Introduction to Liquidity in Trading",4:"Market Structure Shifts",5:"How London Session Highs and Lows Can Provide Valuable Insights",6:"Intraday Order Flow & Understanding The Daily Range",7:"Three Drives Pattern",8:"Morning Trade and Positioning",9:"Market Efficiency Paradigm & Institutional Order Flow",10:"Fair Value Gap",11:"ICT Killzones and Sessions",12:"Daily Bias & Consolidation Hurdles",13:"Power Of 3 & New York PM Session Opportunities",14:"Implementing Economic Calendar Events With The Open",15:"Market Structure For Precision Technicians",16:"Multiple Setups Inside Trading Session",17:"Intermarket Relationships & Intermarket Analysis",18:"FOMC, NFP Study",19:"Model Diagrams",20:"Daily Rebalance Theory",21:"View Price with Institutional Perception",22:"General Range Trading Rules",23:"New Week/Day Opening Gap (NWOG/NDOG)",24:"Liquidity Void and Fair Valuation",25:"How to Use Day of the Week and Time of Day",26:"Daily Templates",27:"Previous Day High and Low as a Liquidity Pool",28:"Hours of Operation",29:"Core Content - ICT Block Types",30:"Breakaway Gaps and the Redelivered Rebalanced PD Array",31:"Central Bank Dealers Range",32:"High Probability Daytrade Setups",33:"Quarterly Shifts & IPDA Data Ranges"}

out = os.path.join(base, "source", "chapters")
os.makedirs(out, exist_ok=True)
# front matter
front = "".join(b for n, k, b in recs if n < 14)
open(os.path.join(out, "ch00-frontmatter.txt"), "w", encoding="utf-8").write(front)

idx = []
ks = sorted(starts)
for j, c in enumerate(ks):
    s = starts[c]
    e = starts[ks[j+1]] - 1 if j + 1 < len(ks) else 671
    body = "".join("\n<<<PDFPAGE %d | images=%d>>>\n%s" % (n, k, b) for n, k, b in recs if s <= n <= e)
    fn = "ch%02d.txt" % c
    open(os.path.join(out, fn), "w", encoding="utf-8").write(body)
    idx.append({"chapter": c, "title": titles[c], "file": fn, "pdf_start": s, "pdf_end": e, "pages": e - s + 1, "chars": len(body), "images": sum(k for n, k, b in recs if s <= n <= e)})
json.dump(idx, open(os.path.join(base, "source", "chapter-index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("CHAPTER_FILES", len(idx))
print("FRONT_CHARS", len(front))
for r in idx:
    print("Ch%-3d p%-4d %-4d pages=%-4d chars=%-7d imgs=%d" % (r["chapter"], r["pdf_start"], r["pdf_end"], r["pages"], r["chars"], r["images"]))
