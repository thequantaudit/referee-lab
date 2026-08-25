# Teardown #001 — Claims Ledger (TradingAgents, arXiv:2412.20138)

> Transcribe every quantitative claim from the paper PDF itself — not press,
> not the repo README. Each row is scored at verdict time.
> Fill in during Phase 0. One claim per row; add rows as needed.

## Backtest configuration claimed by the paper

| Field              | Paper states | Page/Table |
| ------------------ | ------------ | ---------- |
| Test window        |              |            |
| Tickers            |              |            |
| Starting capital   |              |            |
| Agent LLM(s) used  |              |            |
| Baselines compared |              |            |

## Quantitative claims

| #   | Claim (verbatim or near-verbatim)            | Metric       | Claimed value | Page/Table | Phase A result | Phase B result | Verdict input? (Y/N) |
| --- | -------------------------------------------- | ------------ | ------------- | ---------- | -------------- | -------------- | -------------------- |
| 1   | e.g. "Cumulative return on AAPL over window" | CR           |               |            |                |                |                      |
| 2   |                                              | Sharpe       |               |            |                |                |                      |
| 3   |                                              | Max drawdown |               |            |                |                |                      |

## Baseline claims

| Baseline   | Ticker | Paper's reported result | Our Phase A result |
| ---------- | ------ | ----------------------- | ------------------ |
| Buy & hold |        |                         |                    |
|            |        |                         |                    |

## Notes on transcription

- Record the paper's exact numbers to the precision printed.
- Note any claim that is ambiguous, rounded, or missing units — ambiguity goes
  in the ledger too; it is part of what we audit.
