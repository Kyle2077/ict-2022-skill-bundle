# MMXM/MMBM 做市商模型状态机（Market Maker Buy/Sell Model）

## R — Reading (原文)

> MMXM（HTF 看跌时）：Initial Consolidation → Buy Program（accumulation/re-accumulation，BDR 25% 象限）→ Manipulation Swing → SMR（Type1: higher high 后破旧 swing low；Type2: lower high 后破 swing low）→ Sell Program（SDR 25% 分级）；MSB 必须含 FVG，"If this FVG is not present, we don't class this as a valid break"（p.443–445）；Calibration：consolidation 下方 NQ 5/10/15/20 点、ES 2/5/7/10 点增量 + Manipulation Swing 2–2.5 STD 投影（p.447–452）；Distribution 四要素：run liquidity→rebalance/run stops→mitigate in area→continue lower（p.462–464）。SMR 后入场三模型：2022 Model / OFED / Breaker+FVG（p.454–467）。
> 图已核查：p.427（BDR 边界）、p.441（SMR Type1/Type2 + 红 X 失败峰 + SMT 确认）。

出处：Ch19 PDF p.419–467；Ch3 p.64–66；图文证据 resources/figures/mmxm-p0427/、mmxm-p0441/（reviewed）。

## I — Interpretation (自述)

把"做市商如何把价格从 A 送到 B"写成可跟踪的状态机：起点盘整→买方程序沿 BDR 象限逐级积累（每象限间一次 accumulation/re-accumulation）→50% 处 Measuring Gap（不回填，作 terminus 校验）→最后的 Manipulation Swing 诱多→SMR 翻转（Type1/2，需位移+时间+FVG 确认）→卖方程序沿 SDR 分配到 calibrated terminus。状态转换全部有可判定证据：SMR=MSS/MSB+FVG+displacement；terminus=point-range 增量与 2–2.5 STD 投影与 HTF level 的三重汇合。它回答"当前在曲线哪一侧、下一状态等什么证据、terminus 大概多深"。

## A1 — Application Example

原书案例：PDF p.427（BDR=consolidation→HTF Level）与 p.441（Type1 理想反转 + Type2 红 X 失败峰 + SMT 确认条件），均已实际看图核查。原书未给盈亏统计。

## A2 — Future Trigger

情境：问"现在是 buy program 还是 sell program"；问"SMR 确认了吗、Type1 还是 Type2"；问"这轮分配的 terminus 大概在哪"；问"manipulation swing 之后等什么"。
语言信号：MMXM / MMBM / market maker model / buy program / sell program / SMR / BDR SDR / measuring gap / calibration / terminus / distribution cycle。
区分：管"曲线状态与 terminus 校准"；单步结构判定→ mss-displacement-gate / market-structure-hierarchy；具体入场→ ict-2022-model / turtle-soup-entry。

## E — Execution

输入契约：HTF 方向、K线序列、HTF PD Array 水平、（ES/NQ）point-range 表。
1. 定位 Initial Consolidation 与 HTF level → 建 BDR（或镜像 SDR）并 25% 分象限。
2. 标注积累阶段（象限间）与 Measuring Gap（50% 未回填 FVG）；Measuring Gap 缺失→terminus 校验降级标注。
3. SMR 判定：Type1/Type2 + 三证据（位移、时间、扩张腿内 FVG）；缺 FVG→非有效 break，判停于 buy program。
4. Calibration：consolidation 下方 point-range 增量（NQ 5/10/15/20；ES 2/5/7/10）+ Manipulation Swing 2–2.5 STD 投影 + HTF level 汇合 → 输出 terminus 候选带。
5. 状态输出：{当前程序(buy/sell/distribution), 阶段, SMR 状态与类型, terminus 带, 下一证据}。
6. 入场指引：SMR 后三模型择一（2022 Model/OFED/Breaker+FVG），Low Risk Sell=change in state 确认后回撤至 bearish OB（不收盘破 mean threshold）。
判停：HTF 方向缺失→不启动模型（仅 HTF bearish 用 sell model）。

## B — Boundary

- 积累/分配阶段"可以超过两个"，无计数停止规则——状态机输出"当前阶段"而非阶段总数。
- Calibration 数值为经验值，未给波动率调整；非 ES/NQ 不输出 point-range。
- IPDA/做市商意图为未证明假设（进 B）；图依赖 p.420–466 大部分未全核（nr-11），已核 2 页。
- 不用于 HTF 方向不明的震荡。

## visual_evidence 关联

- figure_id: fig-mmxm-p0427（reviewed）、fig-mmxm-p0441（reviewed）

## 图文证据

涉及图形、编号或图文对应时，先实际打开完整图与核查记录，再按需放大局部。当前宿主不能看图时说明限制；记录中的推断不能冒充图中事实。

- 图例 fig-mmxm-p0427 — 来源 src-ict2022，PDF 页序 427，书本页码 323；源文件 SHA256 `c072988322c073be09a95858fc5ec571c12af388fce9f093e6655ffc58b3bd7d`
  - [完整图](../../resources/figures/mmxm-p0427/page-0427.png) · [图文核查记录](../../resources/figures/mmxm-p0427/figure-notes.md)
- 图例 fig-mmxm-p0441 — 来源 src-ict2022，PDF 页序 441，书本页码 337；源文件 SHA256 `c072988322c073be09a95858fc5ec571c12af388fce9f093e6655ffc58b3bd7d`
  - [完整图](../../resources/figures/mmxm-p0441/page-0441.png) · [图文核查记录](../../resources/figures/mmxm-p0441/figure-notes.md)

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/figures/mmxm-p0427/page-0427.png](../../resources/figures/mmxm-p0427/page-0427.png)
- [resources/figures/mmxm-p0427/figure-notes.md](../../resources/figures/mmxm-p0427/figure-notes.md)
- [resources/figures/mmxm-p0441/page-0441.png](../../resources/figures/mmxm-p0441/page-0441.png)
- [resources/figures/mmxm-p0441/figure-notes.md](../../resources/figures/mmxm-p0441/figure-notes.md)
