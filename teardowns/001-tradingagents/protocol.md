# Teardown #001 — TradingAgents: Reproduction Protocol

**Model:** TradingAgents — Multi-Agents LLM Financial Trading Framework
**Paper:** arXiv:2412.20138 (v1 published 2024-12-28)
**Repo:** TauricResearch/TradingAgents
**Coverage start date:** (commit timestamp of this file)
**Protocol version:** 1.0, per Methodology v1.0

---

## 1. The claim under audit

TradingAgents proposes a multi-agent LLM trading framework (fundamental, sentiment, and technical analyst agents; bull/bear researcher debate; trader agents with varied risk profiles; risk management layer) and claims superiority over technical-analysis baselines on cumulative returns, Sharpe ratio, and maximum drawdown.

All specific quantitative claims (tickers, windows, returns, Sharpe, drawdown, baselines) are transcribed from the paper PDF — never from press coverage — into `claims-ledger.md`. The verdict is scored against the ledger alone.

## 2. Test design

### Phase A — Reproduction (on the paper's terms)

- Their repository, their default configuration, their stated backtest window, their stated tickers
- Baselines run alongside: buy-and-hold, plus every baseline the paper cites
- **3 runs per ticker** (LLM agents are stochastic); we report median and range — never a single lucky run
- Costs applied to all strategies, including baselines: **10 bps per trade + 5 bps slippage** (Methodology §3)

### Phase B — The Honesty Window

- Identical configuration, identical tickers
- Window: **2025-01-01 → coverage start date** (all data post-dating the paper's v1 publication of 2024-12-28)
- Same costs, same metrics, same 3-run protocol
- This phase decides the verdict (Methodology §4)

## 3. Metrics

All published metrics computed by the referee-lab harness directly from raw returns and trade logs: total return, Sharpe ratio, maximum drawdown, hit rate, turnover (Methodology §6). The model's own reporting code is never used for verdict metrics.

## 4. Verdict scoring (fixed thresholds, Methodology §5)

| Verdict    | Threshold (honesty-window excess Sharpe vs. claimed)                                         |
| ---------- | -------------------------------------------------------------------------------------------- |
| REPLICATES | ≥ 70% retained, net of costs, and in-sample claims reproduced                                |
| DEGRADES   | 30–70% retained, or edge exists only before realistic costs                                  |
| FAILS      | < 30% retained, central claim unreproducible, or underperforms buy-and-hold SPY net of costs |

## 5. Declared hazards

1. **LLM version drift.** The paper's results were produced with Dec-2024 model builds. We pin and document the exact model IDs used at reproduction time; residual drift is disclosed as a limitation.
2. **Non-determinism.** Mitigated by the 3-run protocol; run-to-run variance is reported, not hidden.
3. **Look-ahead via pretraining.** The LLM's training corpus may contain information from inside the honesty window. There is no clean fix for this in LLM-agent backtesting; it is disclosed in every published result.
4. **Budget cap: $50 for Phase A.** If the framework cannot be reproduced within that budget, the cost of reproduction is itself reported as a finding.

## 6. Artifacts published with the verdict

- Complete run notebooks (`teardowns/001-tradingagents/`)
- Raw decision/trade logs per run (CSV)
- Equity curves: model vs. buy-and-hold vs. baselines, both phases
- Claims ledger with per-claim scoring
- Environment: `requirements.txt` pin at time of run

_Not investment advice._
