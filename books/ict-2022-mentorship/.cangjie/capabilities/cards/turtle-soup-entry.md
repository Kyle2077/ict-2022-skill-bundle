# Turtle Soup/Stop Run 与 Failure Swing 入场（Liquidity-Pool Entry）

## R — Reading (原文)

> "Stop run or turtle soup - highest, most probable trading condition… The market trades to a key level or just short of it - but fails to immediately react - indicating another run deeper before a reversal. After the reversal - the opportunity is best taken when the short-term Market Structure breaking point is retested."（PDF p.28–29 意旨，≤150字）
> 挂单法：看涨=在短期低点处或略下方挂 Buy Limit（买散户 sell stops）；看跌镜像（p.197–198）。假突破三重确认：FVG + 市场结构转变 + 流动性池（p.198）。Failure Swing：穿关键水平后拒绝→回撤→再试失败→破短期高低，作为 stop run 缺失时的备选（p.36–37）。
> V 型要求：扫掠点应成影线、立即 V 型远离，不喜徘徊（p.30–33）。

出处：Ch2 PDF p.22–38；Ch12 p.197–198；Ch29 p.592–596。

## I — Interpretation (自述)

作者口中"最高概率"的入场族：等市场把关键水平外的止损簇扫掉（stop run / turtle soup），扫完不延续而是 V 型收回，就在收回后的短期结构断点回测处入场；挂单视角是"像银行间交易者一样买散户的 sell stops"。若扫掠没发生、改为穿越后二次尝试失败（failure swing），则走备选路径在同一逻辑位入场。能力输出主/备两条路径与各自的确认清单（三重确认、V 型、回测位），并显式记录"扫两次无对侧被取"的 turtle soup 变体。

## A1 — Application Example

原书案例：Ch2 p.30–37 的 stop run / failure swing 示意图组（红三角扫掠点、V 型收回、break point 回测标注；【图 prepared-unreviewed】）；Ch12 p.197–198 流动性池挂单图。原书未给盈亏结果。

## A2 — Future Trigger

情境：价格刚扫了前低/前高问"能反手吗"；问"turtle soup 怎么挂单"；问"没有 stop run 只有假突破怎么办"。
语言信号：turtle soup / stop run / 扫止损 / 假突破 / 反手 / 挂单买止损 / failure swing / 三重确认 / V型。
区分：管"扫掠后的反手入场"；"扫掠是否有效结构"→ mss-displacement-gate；"扫完目标去哪"→ liquidity-dol-state-machine。

## E — Execution

输入契约：关键水平（旧高/旧低/EQH/EQL）、扫掠后的K线序列、短期结构断点。
1. 确认扫掠：价格越关键水平取止损（记录越位深度与是否二次扫掠）。
2. V 型核验：扫掠点是否成影线且迅速收回水平内？徘徊→降级警告（作者不喜徘徊）。
3. 主路径：收回后等短期 MSS 断点回测→入场；或直接在水平处/略外挂反向限价单（买 sell stops 口径）。
4. 三重确认核对：FVG 存在 + MSS + 流动性池，缺一标注降级。
5. 备选路径：若无扫掠而见"穿越→拒绝→回撤→再试失败→破短期高低"→按 failure swing 在同一回测位入场。
6. 输出：{路径(主/备), 扫掠对象, V型判定, 确认清单, 入场位, 止损位（扫掠影线外）}。
判停：扫掠后延续不收回→输出"非 turtle soup，不反手"。

## B — Boundary

- V 型"立即"无时间阈值：作主观项标注。
- 作者警告内建：不在任意旧高低反手，必须是有显著止损簇的高流动性水平；不在破旧高买/破旧低卖（此族是扫后反手，方向相反）。
- 图依赖 p.30–37 未全核（nr-11）。
- 不用于趋势中段的首次突破追单。
