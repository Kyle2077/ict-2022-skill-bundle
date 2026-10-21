# 三驱模式识别（Three Drives Pattern）

## R — Reading (原文)

> 三驱：第一驱=朝 HTF PD Array 的初始运动（升=HH+HL，降=LL+LH）；第二驱=第二次同向推动；第三驱=最终推动应超过第一驱高/低点。关键规则：见三驱朝流动性池时，第三驱不必实际猎取该池——每次创出新短期高/低点市场已在耗尽短期流动性（p.95–98）。
> 衔接：三驱后找 Displacement（"大象跳进儿童泳池"级），Displacement 打印 FVG，入场在 FVG（p.99–100）。
> 判别：若价格非逐步推进式突破短期高点→预期 Stop Hunt 而非三驱延续（p.97–98）。第三驱未达 POI 即强反转=更强信号（机构已建仓）。

出处：Ch7 PDF p.95–100。

## I — Interpretation (自述)

一个"流动性耗尽计数器"：价格朝 HTF 阵列做三次脉冲式推进，每创一次新短期高/低就在消耗一批短期止损；三驱完成后期待一次位移反转（留 FVG），入场在 FVG。它的判别价值在于和 Stop Hunt 的对照——逐步推进=三驱（延续后反转），非推进式单针突破=Stop Hunt（直接反手）。第三驱没到 POI 就强反转是加分信号。

## A1 — Application Example

原书案例：Ch7 p.97–100 三驱标注图（【图 PDF p.97/99/100 prepared-unreviewed】）：三脉冲+位移+FVG 入场标注。原书未给结果。

## A2 — Future Trigger

情境：问"这是三驱吗/第几驱了"；问"三驱完了等什么入场"；问"这次突破是三驱延续还是 stop hunt"。
语言信号：three drives / 三驱 / 第几驱 / impulse / 流动性耗尽 / 三推。
区分：只识别三驱结构与衔接位移；"位移是否有效"→ mss-displacement-gate；"FVG 区间"→ fvg-three-candle；"扫掠反手"→ turtle-soup-entry。

## E — Execution

输入契约：K线序列 + HTF PD Array 方向参考。
1. 计数驱动：按 HH+HL / LL+LH 结构计 1–3 驱；记录每驱新高/低点。
2. 第三驱核验：是否超过第一驱极值；未超→标"三驱未完成"。
3. 判别分支：推进式（逐级）=三驱；单针/非推进突破短期极值=Stop Hunt 预期（转 turtle-soup-entry 口径）。
4. 反转证据：三驱后 Displacement+FVG→输出入场区（FVG）；第三驱未达 POI 即强反转→标注强信号。
5. 输出：{驱数, 类型(三驱/stop-hunt), 反转证据, 入场区或 null}。
判停：不足两驱→说明并停。

## B — Boundary

- Displacement 力度无量化（沿用 nr-03 代理）。
- 三驱不保证反转；作者只给案例。
- 图依赖未全核（nr-11）。
- 不用于无 HTF 阵列方向的场景。
