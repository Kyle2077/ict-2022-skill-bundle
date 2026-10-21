# 市场结构层级判定（Market Structure Hierarchy: STL/ITL/LTL）

## R — Reading (原文)

> ITL = 任何 STL 其两侧都有更高的 STL；ITH = 任何 STH 其两侧都有更低的 STH；LTL = 两侧有更高 ITL 的 ITL；LTH = 两侧有更低 ITH 的 ITH。（PDF p.301–302）
> "Once a ITH/ITL is broken, you have a significant break in market structure (BMS/MSB)."（p.322）
> 目标投射：MSS 后从 ITH 到 LTL 锚定 Fib，投射 -2.0 STDV 作为目标（p.322–325）。Rebalanced ITH = 市场 VERY weak 的摊牌信号（p.306）。
> 图已核查：PDF p.319（书 p.215）蓝圈=ITH/ITL、绿圈=STH/STL、橙箭头=LTH/LTL。

出处：Ch15 PDF p.301–331；图文证据 resources/figures/structure-p0319/（reviewed）。

## I — Interpretation (自述)

把"结构"从一次性突破判定升级为递归层级：短期摆动点（STL/STH）按"两侧邻居更高/更低"升级为中期（ITL/ITH），再升级为长期（LTL/LTH）。层级决定突破的分量：只破 STL 是噪音级，破 ITL/ITH 才是 BMS/MSB（重大结构突破）。配套两个工具：持仓验证（看跌时 up-close 蜡烛应持续压制价格）与目标投射（ITH→LTL 锚 Fib，-2.0 STDV）。它补上了 MSS 判定的上游——先知道当前结构在哪一级，才知道"突破"意味着什么。

## A1 — Application Example

原书案例：PDF p.319（书 p.215）双图，已实际看图核查：层级圈注与 LTL/Short-term SSL 水平线、两档空头入场带（Aggressive / Low Risk High Confirmation）一致。原书未给盈亏结果。

## A2 — Future Trigger

情境：问"这次破的是哪一级结构"；问"现在趋势的 ITL/LTL 在哪"；问"破位后目标投射到哪儿"；为 MSS/偏向能力提供层级上下文。
语言信号：market structure / 结构层级 / STL ITL LTL / STH ITH LTH / BMS MSB / 重大突破 / -2.0 STDV / rebalanced ITH。
区分：只做层级标注与突破分量判定；"突破是否带位移"→ mss-displacement-gate；"偏向"→ daily-bias-checklist。

## E — Execution

输入契约：K线序列（足够长度以形成两级邻居）或已标注摆动点列表。
1. 标出全部 STL/STH（局部极值，口径由调用方 TF 决定并记录）。
2. 递归升级：两侧邻居更高/更低 → ITL/ITH；再同级规则 → LTL/LTH。
3. 突破分量：被破对象是 STL 级=minor；ITL/ITH 级=BMS/MSB（重大）；LTL/LTH 级=趋势级。
4. 持仓验证：看跌时检查 up-close 蜡烛是否持续压制；被收盘越过→标注结构存疑。
5. 目标投射（可选）：ITH→LTL 锚 Fib，输出 -2.0 STDV 价位（STD 口径=Fib 标准差工具，作者未给替代定义）。
6. 输出：{层级表, 被破级别, 分量, 投射目标或 null}。
判停：序列不足以形成邻居关系→说明并停。

## B — Boundary

- 作者警告内建：不理解银行间结构观会成为虚假 MSB 的受害者；ITH 被打破必须 step aside。
- -2.0 STDV 无成功率数据；"为何 -2.0"原文未论证。
- 层级判定依赖摆动点口径（TF/影线），不同口径结论不同——必须记录口径。
- 图依赖 p.303–327 未全核（nr-11）。

## visual_evidence 关联

- figure_id: fig-structure-p0319（reviewed）

## 图文证据

涉及图形、编号或图文对应时，先实际打开完整图与核查记录，再按需放大局部。当前宿主不能看图时说明限制；记录中的推断不能冒充图中事实。

- 图例 fig-structure-p0319 — 来源 src-ict2022，PDF 页序 319，书本页码 215；源文件 SHA256 `c072988322c073be09a95858fc5ec571c12af388fce9f093e6655ffc58b3bd7d`
  - [完整图](../../resources/figures/structure-p0319/page-0319.png) · [图文核查记录](../../resources/figures/structure-p0319/figure-notes.md)

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/figures/structure-p0319/page-0319.png](../../resources/figures/structure-p0319/page-0319.png)
- [resources/figures/structure-p0319/figure-notes.md](../../resources/figures/structure-p0319/figure-notes.md)
