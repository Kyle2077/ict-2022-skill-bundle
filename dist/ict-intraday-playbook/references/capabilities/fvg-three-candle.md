# FVG 三蜡烛判定（FVG Three-Candle Detector）

## R — Reading (原文)

> Bearish FVG：Candle 1 的低点=起点；Candle 2=缺口本体；Candle 3 的高点=终点。Bullish FVG：Candle 1 的高点=起点；Candle 3 的低点=终点。（PDF p.147，书 p.119；图已核查 reviewed）
> 最佳形态：bearish FVG 出现在 BSL 被扫之后/相对等高上方；bullish 出现在 SSL 被扫之后/相对等低下方（p.149–151）。
> 非 FVG：前一根K线高点已抵消第三根K线低点→平衡价格行为（p.141）。

出处：Ch10 PDF p.139–154；图文证据 resources/figures/fvg-p0147/（reviewed）。

## I — Interpretation (自述)

FVG 是"三根连续K线之间的价格空档"：中间那根大蜡烛把价格推走，快到前后两根蜡烛的影线都够不着它的一部分。Bearish 方向取蜡烛 1 低点到蜡烛 3 高点之间的空档；bullish 镜像。它既是入场区、也是目标区、还是"机构赞助"的脚印（位移的副产品）。判定是纯 OHLC 算术：给定任意三根连续蜡烛即可判有无与区间；质量过滤（是否在流动性被扫后形成）是加分项而非存在性条件。

## A1 — Application Example

原书案例：PDF p.147（书 p.119）三蜡烛标注图，已实际看图核查（figure reviewed）：三根红烛标 1/2/3，蓝色 FVG- 区间上界对齐蜡烛 1 低点、下界对齐蜡烛 3 高点；右折线图标 Displacement High/Low 与 "FVG forms inside this range"。原书未给该例盈亏结果。

## A2 — Future Trigger

情境：问"这里有没有 FVG / 缺口在哪"；为入场能力找入场区；问"这个 FVG 算不算好 FVG"；核对位移证据。
语言信号：FVG / fair value gap / 公允价值缺口 / 三蜡烛 / imbalance / 不平衡 / 缺口区间 / 回补。
区分：只识别与定区间；"FVG 被扫后去哪"→ liquidity-dol-state-machine；"在 FVG 里挂哪一档"→ ote-entry-zone。

## E — Execution

输入契约：连续K线 OHLC 序列（或单组三蜡烛）。
1. 对每组连续三蜡烛：bearish 判定 = c1.low > c3.high（空档=[c3.high, c1.low]）；bullish 判定 = c3.low > c1.high（空档=[c1.high, c3.low]）。
2. 空档存在性检查：bearish 需 c3.high < c1.low；bullish 需 c3.low > c1.high；不满足即非 FVG。p.141"抵消=平衡价格行为"的原文措辞（哪两根影线相抵）存在歧义，本能力的可执行实现=空档不存在即平衡（阶段 4 训练集修正并记录：旧版镜像排除条件在对应方向序列中物理不可达，执行器按其推理亦得出同结论）。
3. 质量标注：空档形成前是否刚扫过 BSL/SSL、是否位于相对等高/等低外侧→标 best/normal。
4. 输出：{方向, 区间[low,high], 三蜡烛索引, 质量标注, 是否未回补}。
5. 多 FVG 时按时间序全列，不替用户选。
判停：序列不足三根→说明缺数据。

## B — Boundary

- FVG 最小宽度原文未定义（nr-04）：不过滤宽度，原样输出。
- "高概率回补"是作者未验证声明；不输出回补概率。
- 不用于无 K 线数据的场景；不猜影线缺失数据。
- 与 Liquidity Void 区分：LV 是单边大运动的空白区（Ch24），FVG 是三蜡烛结构，二者不混用。

## 补章并入（2026-10-21，Ch24/30 逐页细读）

- Liquidity Void 子类（Ch24 p.499–501）：单方向大幅运动的大实体小影线蜡烛区=Void（FVG 的极端形态）；回填行为=上下插针（做市商区间内平多/回空）；回填非即时；Void 填满后找更远端 FVG/OB。输出增加 subtype=void 标记。
- BPR/RDRB 与 Breakaway Gap（Ch30 p.617–621）：Bullish BPR=UP→DOWN→UP AGAIN；Bearish=DOWN→UP→DOWN AGAIN（RDRB=BPR 别名）；FVG 上/下方存在 BPR→该 FVG 保持开放=Breakaway Gap（输出增加 breakaway_gap=true 标记与不回填预期）。
- 警告：BPR 无最小幅度阈值；Breakaway 为定性判断。

## 图文证据

涉及图形、编号或图文对应时，先实际打开完整图与核查记录，再按需放大局部。当前宿主不能看图时说明限制；记录中的推断不能冒充图中事实。

- 图例 fig-fvg-p0147 — 来源 src-ict2022，PDF 页序 147，书本页码 119；源文件 SHA256 `c072988322c073be09a95858fc5ec571c12af388fce9f093e6655ffc58b3bd7d`
  - [完整图](../../resources/figures/fvg-p0147/page-0147.png) · [图文核查记录](../../resources/figures/fvg-p0147/figure-notes.md)

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/figures/fvg-p0147/page-0147.png](../../resources/figures/fvg-p0147/page-0147.png)
- [resources/figures/fvg-p0147/figure-notes.md](../../resources/figures/fvg-p0147/figure-notes.md)
