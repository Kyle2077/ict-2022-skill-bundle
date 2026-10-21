# NWOG/NDOG 动态缺口锚（NWOG/NDOG Gap Anchors）

## R — Reading (原文)

> NWOG = 周五收盘与周日开盘之间区间；画法用低 TF（5m）、仅 RTH 可见（ETH 不可见）；CE = Fib 自周五收盘锚至周日开盘的 50%（p.492–493）。图已核查 p.494（书 p.390）：粉色区间=NWOG High/Low、绿线 C.E.=50%；蓝色注释框给出 SUNDAY FIRST CANDLE 18:00 NY、FRIDAY LAST CANDLE 17:00 NY。
> 使用：像 FVG 一样对待；价格尊重 NWOG 的 CE；至少记录最近 5 个（ICT：前 4 周 NWOG=X-ray view）；多个聚集→区间震荡；上缺口=支撑、下缺口=阻力（p.493–494）。
> NDOG = 5PM 收盘与 6PM 开盘差额（p.493，时区原文未标，惯例纽约）。
> Event Horizon = 两相邻 NWOG 的中点之间位置；阻止价格逃离 NWOG 吸引并制造朝未达 NWOG 的脉冲（p.495–496）。

出处：Ch23 PDF p.492–496；图文证据 resources/figures/nwog-p0494/（reviewed）。

## I — Interpretation (自述)

跨日/跨周的动态公允价值锚：周末与日间的收盘-开盘缺口是"未交易真空"，算法倾向回访。能力输出每日可查的缺口清单：最近 ≥5 个 NWOG 的高低与 CE、当日 NDOG、相邻 NWOG 的 Event Horizon，以及支撑/阻力方向标记与"聚集=震荡"的状态提示。它是纯取数+中点计算，方向结论交给偏向能力；时区口径（周五 17:00/周日 18:00 NY 为图示口径）与 RTH-only 限制必须随输出声明。

## A1 — Application Example

原书案例：PDF p.494（书 p.390）NWOG 标注图，已实际看图核查：粉色区间、50% C.E. 线、17:00/18:00 NY 注释框与正文定义一致。原书未给回填率统计。

## A2 — Future Trigger

情境：周日晚/周一问"这周 NWOG 在哪、CE 多少"；问"缺口当支撑还是阻力"；问"好几个缺口叠在一起意味什么"。
语言信号：NWOG / NDOG / 周缺口 / 日缺口 / opening gap / CE / consequent encroachment / event horizon / 缺口回填。
区分：只管缺口锚；静态锚→ daily-static-anchors；FVG→ fvg-three-candle（NWOG 用法"像 FVG"但对象不同）。

## E — Execution

输入契约：RTH 图表数据（5m 或更细）、周五收盘/周日开盘/每日 17:00–18:00（纽约）收盘开盘价；缺则询问。
1. 取最近 ≥5 个 NWOG：high/low/CE(50%)；标注上/下缺口→支撑/阻力。
2. 取当日 NDOG（5PM 收–6PM 开，纽约口径标注）。
3. Event Horizon：相邻两 NWOG 的中点中位→输出。
4. 状态提示：≥3 个 NWOG 聚集→标"区间震荡倾向"。
5. 输出：{nwog_list[{high,low,ce,week}], ndog, event_horizon, cluster_flag, 时区与RTH声明}。
判停：ETH-only 数据源→输出"RTH 不可见，无法绘制"并停。

## B — Boundary

- 时区/夏令时未说明（nr-01）；17:00/18:00 为图示口径，正文未逐字给。
- 回填非即时（作者明示"不必立即"）；聚集期单向概率下降。
- 经纪商 RTH/ETH 定义差异可能改变缺口（作者未覆盖）。
- 不输出回填概率。

## visual_evidence 关联

- figure_id: fig-nwog-p0494（reviewed）

## 图文证据

涉及图形、编号或图文对应时，先实际打开完整图与核查记录，再按需放大局部。当前宿主不能看图时说明限制；记录中的推断不能冒充图中事实。

- 图例 fig-nwog-p0494 — 来源 src-ict2022，PDF 页序 494，书本页码 390；源文件 SHA256 `c072988322c073be09a95858fc5ec571c12af388fce9f093e6655ffc58b3bd7d`
  - [完整图](../../resources/figures/nwog-p0494/page-0494.png) · [图文核查记录](../../resources/figures/nwog-p0494/figure-notes.md)

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/figures/nwog-p0494/page-0494.png](../../resources/figures/nwog-p0494/page-0494.png)
- [resources/figures/nwog-p0494/figure-notes.md](../../resources/figures/nwog-p0494/figure-notes.md)
