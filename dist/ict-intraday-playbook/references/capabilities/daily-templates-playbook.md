# 日内模板剧本（Daily Templates Playbook）

## R — Reading (原文)

> Classic Buy/Sell Day：最佳盈利模板；主要周一二、最迟周三伦敦时段；日线范围持续 7–8 小时；趋势通常至 11:00 EST；Classic Buy=关键支撑低于开盘价时买入、开盘先涨不追等回落开盘价下方；开盘价到支撑平均 7–12pt(ES)，超 12pt 等纽约；12:00 前锁 5–7pt 小利润（p.519–521）。
> Reversal 模板（London Swing to NY Open / London Close Reversal）：先跌穿开盘价买入→反弹至 HTF POI→NY 时段发生=经典反转；监控伦敦最后 1h(4–5am)与纽约第一小时(7–8am)（p.516–518，时区未标，上下文推测 EST）。
> Range to NY Open / London Close Rally：多见 NFP/FOMC/利率；消息前盘整→跌破 London Lows→消息后反弹（p.521）。
> Consolidation Raid on News：开盘后盘整→消息发布下跌破盘整诱空扫止损→清后走真方向；**消息后 5 分钟内未在支撑/阻力被拒绝→离场**（p.522）。

出处：Ch26 PDF p.515–522。

## I — Interpretation (自述)

四种"今日剧本"识别器：经典趋势日（周一二、7–12pt 支撑距离、11:00 前趋势、12:00 前锁利）、反转日（伦敦造极值+纽约反转）、新闻区间反弹日、新闻盘整扫掠日（带 5 分钟拒绝判停门）。用星期+是否有新闻+早盘形态三输入做剧本匹配，输出该剧本的执行路径与放弃条件。它的价值是把"今天像哪种日"从感觉变成带数值门槛的匹配。

## A1 — Application Example

原书案例：Ch26 p.516–522 四模板示意图与实例（【图 prepared-unreviewed】）。原书未给各模板出现频率统计。

## A2 — Future Trigger

情境：早盘问"今天像哪种剧本"；问"开盘先涨了还追吗"；问"消息砸下去又拉回来按哪个模板做"。
语言信号：daily template / 今天剧本 / classic buy day / 反转日 / 新闻日模板 / consolidation raid / 5分钟规则。
区分：管剧本匹配与路径；时段可否→ session-taboo-filter；硬门与风控→ high-probability-entry-risk。

## E — Execution

输入契约：星期、新闻日历、开盘价、早盘形态（是否先涨/是否盘整/是否破 London lows）、支撑距离点数(ES)。
1. 剧本匹配（按优先级）：新闻日+盘整被扫→Consolidation Raid；新闻日+破 London lows 后反弹→Range Rally；周一二+开盘价下方支撑 7–12pt→Classic；伦敦极值+NY 反转→Reversal；均不符→输出"无匹配模板，按通用流程"。
2. 输出匹配剧本的执行路径与数值门槛（Classic：不追先涨、超 12pt 等纽约、12:00 前锁 5–7pt；Raid：消息后 5 分钟拒绝门）。
3. 放弃条件：门槛不满足→切换/放弃并说明。
4. 输出：{剧本, 路径, 门槛检查[], 放弃原因或 null}。
判停：5 分钟门未拒绝→输出离场。

## B — Boundary

- 模板为经验归纳，无频率统计；"主要在周一二"非保证。
- 点数仅 ES；4–5am/7–8am 时区原文未标（推测 EST，标注缺口）。
- 重叠期波动跳空风险作者明示。
- 不用于无早盘数据的盘前预测（剧本需早盘形态确认）。
