# IPDA 数据范围构建器（IPDA Data Range Builder）

## R — Reading (原文)

> 构建六步：①仅日线；②不含周末仅计工作日；③在 20/40/60 日回溯内找最高高点与最低低点；④找范围内 PD Arrays（旧月/周/4H 高低、Gaps、Liquidity Voids、ICT OB 等）；⑤取过去 60 日最高最低并切半；⑥在切半范围内定位明显 premium/discount arrays（p.667–668）。
> 前瞻：结构转变后头 20/40/60 天预期设置；两侧止损清除+均衡后→看 60 日外下一个范围高低=下一重大波动方向；新市场划分后 20 天内可预期重要波动（p.664–666）。20 天=近期、40=短期、60=中期高低（p.666）。
> 警告："IPDA lookback data ranges alone does not tell you where to buy and sell. There needs to be a blend of concepts, mainly time and price."（p.669）旧高低多长影线→找 Rejection Block，扫实体而非影线（p.663）。

出处：Ch33 PDF p.660–671。

## I — Interpretation (自述)

一个纯日历+极值的坐标构建器：在日线（只数工作日）上取 20/40/60 三个回溯窗的高低点与范围内 PD Arrays，再把 60 日范围切半标折溢价阵列；产出是"算法近期会参考哪些价位"的清单，以及"结构转变后 20/40/60 天窗口内预期设置"的时间提示。它是偏向与 Top Down 的上游输入，本身不给买卖点——作者亲自警告单独使用无效，必须与时间/价格融合。

## A1 — Application Example

原书案例：Ch33 p.666 六图展示 20/40/60 范围与切半标注（【图 prepared-unreviewed】）。原书未给统计验证；季度轮换频率为作者断言。

## A2 — Future Trigger

情境：周度复盘问"未来几周算法会参考哪些价位"；问"20/40/60 日范围怎么画"；问"结构转变后多久会有大波动"。
语言信号：IPDA / data range / 20 40 60 天 / 回溯 / 季度轮换 / quarterly shift / 切半 / lookback。
区分：只做范围构建与时间窗提示；买卖决策→ daily-bias-checklist / ict-2022-model。

## E — Execution

输入契约：日线 OHLC 序列（≥60 工作日）、当前日期。
1. 工作日计数（排除周末）建 20/40/60 三窗。
2. 每窗输出高/低点；窗内 PD Arrays 清单（旧月/周/4H 高低、gaps、voids、OB——OB 识别调 pd-array-block-dictionary）。
3. 60 日范围切半→输出折价/溢价半区与区内明显阵列。
4. 时间窗提示：若存在近期结构转变日→输出其后 20/40/60 天窗口。
5. 影线处理：旧高低多长影线→标注 Rejection Block 候选（扫实体口径）。
6. 输出：{三窗高低, 窗内阵列, 切半折溢价, 时间窗, 警告：须与时间/价格融合}。
判停：日线不足 60 工作日→输出可用窗并降级标注。

## B — Boundary

- 20/40/60 回溯期与季度轮换频率均无统计验证（作者断言，进 B）。
- "obvious arrays" 选择主观→输出候选清单不做唯一选择。
- 单独使用不给买卖点（作者明令）。
- 不用于 intraday 级别决策。
