# MIT 6.S191 Study Guide — The Quant Audit Track

_Which lectures sharpen the referee's eye, in watch order — August 2026_

Framing rule: watch each lecture asking not "is this interesting?" but
**"what does this teach me to spot in the models I'm auditing?"**

---

## Priority 1 — Watch first

### Lecture 2 — RNNs, Transformers, and Attention

**Why it matters:** most hyped time-series models (e.g., Kronos, on the docket)
are transformers or RNN descendants applied to price data.

**What to listen for:**

- Why attention models can _memorize_ rather than generalize — the root cause
  of most "great backtest, dies live" stories
- Why sequence models behave differently on non-stationary data (markets)
  than on text
- The questions to ask when a paper claims a transformer "learned market dynamics"

### Lecture 6 — Language Models and New Frontiers

**Why it matters:** teardown #1 (TradingAgents) is an LLM-agent system.

**What to listen for:**

- Pretraining corpora and training cutoffs — this _is_ our "look-ahead via
  pretraining" hazard: an LLM's training data may already contain the honesty
  window's news
- RLHF and capability limits — how to tell a genuine reasoning agent from
  pattern-matching theater

**Pairing note:** watch this the same week you transcribe the TradingAgents
claims ledger. The paper's architecture section will read differently.

### Lecture 5 — Reinforcement Learning

**Why it matters:** a whole species of hyped trading models (FinRL and friends)
are RL agents.

**What to listen for:**

- Reward hacking — agents optimizing the metric, not the goal
- Sensitivity to environment design — backtest environments that don't
  resemble live markets
- Where RL papers hide their fragility (sample efficiency, seed variance,
  environment overfitting)

---

## Priority 2 — Foundation

### Lecture 1 — Introduction to Deep Learning

Watch if Lecture 2 assumes knowledge you don't have. Otherwise skimmable
at 1.5x speed.

---

## Priority 3 — Optional / skip for now

| Lecture                                    | Relevance | Note                                                                                                                              |
| ------------------------------------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 4 — Deep Generative Modeling               | Medium    | Matters when auditing models that generate _synthetic price data_ — a known backtest-laundering technique. Teardown #3+ territory |
| 7 — The Three Laws of AI                   | Low       | Big-picture framing; interesting, won't sharpen audits                                                                            |
| 8 — AI for Science                         | Low       | Different domain                                                                                                                  |
| 9 — Secrets of Massively Parallel Training | Low       | Infrastructure, not methodology                                                                                                   |

---

## The loop

Lectures make you sharper; teardowns make it real. The coaching plan:
every concept you learn should show up as a question in a claims ledger
within two weeks of learning it.

_The Quant Audit · referee-lab · methodology v1.0_
