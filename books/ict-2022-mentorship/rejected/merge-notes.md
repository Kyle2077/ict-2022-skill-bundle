# rejected/merge-notes.md — 去重合并与降级说明（不另建逐条 rejected 文件）

## 合并（保留 canonical ID）

| 被合并项 | canonical | 理由 |
|---|---|---|
| pr-01/21/31/40/41 + cx-02/03/21/24 | cap-01 | 同一时段/禁忌过滤机制的数值面与反例面 |
| pr-11/12/16 + fw-02(部分) | cap-02 | 同一静态锚计算 |
| pr-08/23/24/32 + cx-01/15 | cap-03 | 流动性机制一体 |
| pr-42 + cx-20 | cap-04 | 偏向判定的规则面与失效面 |
| pr-04 + cx-06 | cap-05 | MSS 规则与无效情形一体 |
| pr-05 + cx-07 | cap-06 | FVG 规则与非 FVG 情形一体 |
| pr-17/25/26/27/38/39 + cx-17/18 | cap-07 | Block 词典的数值面与失效面 |
| fw-11 + pr-09/10/13/18/36/37 + cx-04/08/13/14 | cap-08 | Ch32 清单一体 |
| fw-12 + pr-33 | cap-09 | 同一九步流程 |
| fw-10 + fw-19 + pr-15/21/22 | cap-10 | 六步与新闻日 9 步为同一执行链的两视图 |
| fw-09 + pr-03 | cap-11 | 同一 OTE 计算 |
| fw-15 + fw-16 + pr-34 + cx-01 | cap-12 | 主/备入场路径一体 |
| fw-08 + pr-19 + cx-10/11/12/23 | cap-13 | PO3 一体 |
| fw-05 + pr-07 + cx-05 | cap-14 | SMT 一体 |
| fw-13 + fw-14 + pr-20 + cx-22 | cap-15 | 工作流一体 |
| fw-01 + fw-06 | cap-03 | ERL/IRL 与 DOL 为同一状态机两视角 |
| fw-20 | cap-04 | Dealing Range 划分是偏向判定第 1 步 |

## 降级为 reference（非淘汰）

- fw-18 MMXM → ref-01（概念曲线模型，实时判定缺客观信号，V2 不充分）
- Ch1/Ch8 心态内容 → ref-02
- pr-02 合约规格 → ref-09（查表数据，非决策能力）
- Ch17/Ch26/Ch23/27/31/33 试点外内容 → ref-03…ref-06（范围外，摘要级）
- glossary 95 条 → ref-07；case 22 条 → ref-08

## 真正 rejected（无原文依据或被完整覆盖）

- 无。五个 extractor 均按原文提取；提取器自补的 2 条推断风险（counter-example 补充节）不进入任何能力，仅存留于 candidates/counter-example.md 备查。
