# ICT 2022 Model 六步执行流程（ICT 2022 Model Six-Step）

## R — Reading (原文)

> 模型图（PDF p.407，书 p.303，图已核查 reviewed）：价格带小修正奔向 Old High / Relative Equal Highs→突破后位移下跌留 Fair Value Gap area→跌破 short-term low = MSS；注释要求"see it go below that level with displacement and an energetic move, taking out a short-term low"。
> 新闻日框架（p.116–118）：新闻解禁后等大看跌位移→前 10 分钟不交易→看跌 PD arrays 失效→看涨位移→订单流转变→折价阵列买入，ES 止损≤5 点、目标 10 点。

出处：Ch19 PDF p.406–410（图）、Ch9 p.116–118、Ch32 p.628–631；图文证据 resources/figures/model-p0407/（reviewed）。

## I — Interpretation (自述)

全书的集成执行链，六步：①价格扫过主要流动性（旧高/旧低、亚洲/伦敦/前日高低）；②反转并产生带位移的 FVG（位移=机构赞助的脚印）；③摆动高/低点与 FVG 三蜡烛之一水平对齐即 MSS；④画 50% Fib（两种锚定）；⑤FVG 须位于均衡线或流动性一侧；⑥在 FVG 内均衡或更优侧挂限价单。新闻日叠加九步观察框架（前 10 分钟禁交易、PD arrays 失效序列、5/10 点风控）。它把"扫流动性-位移-结构-折价入场"串成单一可核对序列，任何一步缺失即不成立。

## A1 — Application Example

原书案例：PDF p.407（书 p.303）模型双图（Old High 版与 Old FVG 版），已实际看图核查：绿线目标、黄色 FVG 带、品红 MSS 线与 short-term low 对齐关系均与六步文本一致。原书未给盈亏结果。

## A2 — Future Trigger

情境：问"按 2022 模型现在走到第几步了"；问"扫完高点后该等什么信号再进"；新闻日问"解禁后怎么找设置"。
语言信号：2022 model / 六步 / ICT model / 扫流动性之后 / displacement FVG MSS / 新闻日设置 / news embargo / buy side oriented / sell side oriented。
区分：管"执行序列走到哪、缺哪步"；单步判定分别调 mss-displacement-gate / fvg-three-candle；风控数值→ high-probability-entry-risk。

## E — Execution

输入契约：K线序列、主要流动性水平清单、新闻日历（新闻日分支必需）。
1. 确认流动性扫掠：价格越过 Old High/Low 或会话高低（记录被扫对象）。
2. 位移+FVG：扫掠后反向位移并留下 FVG（调 fvg-three-candle）。缺失→判停"步骤2未满足"。
3. MSS：摆动点与 FVG 三蜡烛之一水平对齐且带位移（调 mss-displacement-gate）。缺失→判停。
4. 50% Fib：自位移腿高/低锚定，标均衡线。
5. FVG 位置核验：FVG 在均衡线或流动性一侧？否→降级警告。
6. 入场：FVG 内均衡或更优侧限价单；新闻日叠加：解禁后 10 分钟内禁交易、PD arrays 失效序列核对、ES 止损≤5 点目标 10 点。
7. 输出：{step1..step6: met/unmet, next, status}。status 词汇固定：ok / stop_step1 / stop_step2 / stop_step3 / news_window_wait。判停：步骤 2/3 缺失即停（status=stop_step2/stop_step3），不跳步入场；未扫流动性 status=stop_step1。

## B — Boundary

- "clear unobstructed path" 无判定法：本能力不实现该判断，标注为使用者主观项。
- 5/10 点仅 ES；新闻日框架仅适用 NFP/CPI/FOMC/PPI/Fed 讲话类事件。
- 模型图步骤 4–6 在 p.408–410（prepared-unreviewed），六步文本来源完整，图未全核不宣称图证齐备。
- 不用于无流动性扫掠的顺势追单场景。

## visual_evidence 关联

- figure_id: fig-model-2022-p0407（reviewed，见 resources/figures/model-p0407/figure-notes.md）

## 补章并入（2026-10-21，Ch19/24 逐页细读）

- Step 4 精确化（Ch19 p.409–411）：50% Fib 两种锚定：(a) 取流动性的 swing→FVG 另一侧 swing；(b) 取流动性后的 prominent swing→FVG 另一侧 swing。原文未给优先级——输出两种锚定值并列。
- Step 5 精确表述：FVG 缺口必须在 Equilibrium(50%) 线上或流动性一侧（better side）。Displacement Range=displacement low（被破短期低）到 displacement high（旧高）。
- Equilibrium 蜡烛体信号（Ch24 p.499）并入 Step 5 确认：烛体停留一侧而影线穿 Equilibrium=潜在反转 hint（非确定信号）。

## 图文证据

涉及图形、编号或图文对应时，先实际打开完整图与核查记录，再按需放大局部。当前宿主不能看图时说明限制；记录中的推断不能冒充图中事实。

- 图例 fig-model-p0407 — 来源 src-ict2022，PDF 页序 407，书本页码 303；源文件 SHA256 `c072988322c073be09a95858fc5ec571c12af388fce9f093e6655ffc58b3bd7d`
  - [完整图](../../resources/figures/model-p0407/page-0407.png) · [图文核查记录](../../resources/figures/model-p0407/figure-notes.md)

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/figures/model-p0407/page-0407.png](../../resources/figures/model-p0407/page-0407.png)
- [resources/figures/model-p0407/figure-notes.md](../../resources/figures/model-p0407/figure-notes.md)
