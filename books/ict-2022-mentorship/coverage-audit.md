# coverage-audit.md — 原书关键任务 → 候选 → 判定 → 交付去向

> 基准来自 BOOK_OVERVIEW.md 第 4 节关键任务清单（task-01…task-12）。decision 列对应阶段 1.5 分流。

| task_id | 读者任务 | 原文位置 | 候选 | decision | 最终去向 |
|---|---|---|---|---|---|
| task-01 | 判断可交易时间窗口与禁忌日 | Ch11 p.155–180; Ch18 p.399–405; Ch28 p.537–546 | fw-07, pr-01/21/31/40/41, cx-02/03/21/24 | verified | cap-01（FOMC/NFP 禁忌日细则来自试点外 Ch18 → 已并入 cap-01 来源，Ch18 正文未深读，仅用候选摘要登记；标 needs-review nr-09） |
| task-02 | 确定 Daily Bias | Ch12 p.183–210; Ch16(试点外) | fw-02, fw-20, pr-42, cx-20 | verified | cap-04 |
| task-03 | 标静态价位锚 | Ch23/27/31（试点外）+ Ch10/11/12（试点内锚定义） | 部分（pr-11/12/16, fw-02 部分） | verified(试点内子集) | cap-02；NWOG/NDOG、PDH/PDL 3日扩展、CBDR±STD 投影在试点外 → references.md ref-05 登记，未深读不编 |
| task-04 | 识别流动性池与 DOL | Ch3 p.39–79 | fw-01, fw-06, pr-08/23/24/32, cx-01/15 | verified | cap-03 |
| task-05 | 判定 MSS 有效性 | Ch4 p.80–83; Ch10 p.143–144; Ch15(试点外) | fw-03, pr-04, cx-06 | verified | cap-05（结构层级 STL/ITL/LTL 在试点外 Ch15 → deferred，nr-10） |
| task-06 | 识别 FVG 与 Displacement | Ch10 p.139–154 | fw-04, pr-05, cx-07 | verified | cap-06 |
| task-07 | 选择入场位置（PD Array+OTE） | Ch16(试点外), Ch29 p.547–616, Ch19(试点外) | fw-17, fw-09, pr-03/17/25/26/27 | verified | cap-07 + cap-11；Ch16 POI 选择细节与 Ch19 六步图在试点外 → cap-10 以 Ch9/Ch32 文本重建六步，图 p.407 已核 |
| task-08 | 止损与分批止盈 | Ch32 p.634–636 | fw-11, pr-09/10/36, cx-08 | verified | cap-08 |
| task-09 | 判断日内阶段(PO3)与 Judas 窗口 | Ch13 p.215–265 | fw-08, pr-19, cx-10/11/12/23 | verified | cap-13 |
| task-10 | 盘前过滤（亚洲阈值/新闻/SMT） | Ch11 p.170; Ch12 p.186–192; Ch32 p.628–631 | fw-05, fw-07, pr-11/12, cx-03/05 | verified | cap-01 + cap-14 + cap-08 硬门 |
| task-11 | 日内执行工作流 | Ch6 p.88–94; Ch8 p.101–111 | fw-13, fw-14, pr-20, cx-22 | verified | cap-15 |
| task-12 | IPDA/季度上下文 | Ch33（试点外） | 无候选（未提取） | deferred | references.md ref-06 登记"试点外未读"，不编内容 |

## critical/high 复核

- task-01/02/06/07/08 均为 high：均有 verified 能力对应，无未解释遗漏（试点外部分显式登记 deferred）。
- 试点内无"重要任务零候选"情况。
- Ch18 禁忌日与 Ch23/27/31/33 价位锚扩展：属用户确认的"核心章节试点"范围外，按范围登记为 deferred，不计为遗漏。

---

# 补章覆盖审计（2026-10-21）

用户要求补齐试点外全部章节：Ch5/7/8/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/30/31/33（21 章，全书 33 章至此全部覆盖）。

| 章 | 候选组 | 去向 |
|---|---|---|
| Ch5 | GA-01 | 并入 cap-01/cap-02（伦敦高低三用途+锚登记） |
| Ch7 | GA-02 | 新增 cap.ict2022.three-drives-pattern |
| Ch8 | GA-03/GA-04 | 并入 cap-13/cap-04；新增 cap.ict2022.afternoon-hours-playbook |
| Ch14 | B-01..B-06 | 新增 cap.ict2022.opening-range-cpe；并入 cap-04/08/13/15 |
| Ch15 | GA-05..GA-08 | 新增 cap.ict2022.market-structure-hierarchy（解决 nr-10）；并入 cap-05/07/11/15 |
| Ch16 | B-07..B-20 | 新增 cap.ict2022.order-flow-formation-gate；并入 cap-04/07/08/11 |
| Ch17 | GD-01/02 | 新增 cap.ict2022.dxy-seasonal-filter（ref-03 落实） |
| Ch18 | GA-09 | 并入 cap-01（解决 nr-09：禁忌日完整清单逐页核） |
| Ch19 | C-01..C-09 | 新增 cap.ict2022.mmxm-state-machine（ref-01 升级）、cap.ict2022.ict-atm-method；并入 cap-05/10/13 |
| Ch20 | C-09/C-10 | 并入 cap-13（算法时间线增量）；Immediate Rebalance 记 references ref-10（原则级、无失效条件，不独立成卡） |
| Ch21 | C-11/C-12 | 新增 cap.ict2022.institutional-perception-model；并入 cap-07 |
| Ch22 | GD-03..GD-06 | 新增 cap.ict2022.monday-range-procedure；并入 cap-01/02 |
| Ch23 | GD-07..GD-09 | 新增 cap.ict2022.nwog-ndog-anchors（ref-05 子项落实，图 p.494 reviewed） |
| Ch24 | GD-10..GD-13 | 并入 cap-06/07/10/13 |
| Ch25 | GD-14 | 并入 cap-01（时段增量细节） |
| Ch26 | GD-15..GD-18 | 新增 cap.ict2022.daily-templates-playbook（ref-04 落实） |
| Ch27 | GE-01 | 并入 cap-02/cap-04 |
| Ch28 | GE-02 | 并入 cap-01（AM/PM/Lunch 时段模板→afternoon-hours-playbook） |
| Ch30 | GE-03 | 并入 cap-06（BPR/Breakaway Gap） |
| Ch31 | GE-04 | 并入 cap-02（CBDR ±STD 投影） |
| Ch33 | GE-05 | 新增 cap.ict2022.ipda-data-range-builder（ref-05/06 落实） |

新增 13 能力 + 11 张既有卡追加"补章并入"节；active 能力总数 28；promoted 7 + router 入口 1 = 预算 8 不变。
