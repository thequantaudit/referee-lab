# The Standard

### How The Quant Audit Judges an AI Trading Model

**Methodology v1.0 — August 2026**
_The Quant Audit · thequantaudit.com_

---

Every week, another model arrives with a spectacular backtest. A transformer that predicts the S&P 500. A reinforcement-learning agent that "beats the market." An LLM that reads filings and front-runs earnings. The charts are beautiful, the Sharpe ratios are heroic, and the social media traction is immediate.

Almost nobody checks.

Not because the people sharing these models are dishonest — most are genuinely excited — but because checking is slow, unglamorous work. You have to reproduce the pipeline, source the data, model transaction costs, and then do the one thing hype never does: **wait.** Wait to see whether the model survives data it has never seen, in a market that doesn't know it's supposed to cooperate.

The Quant Audit exists to do that work in public. This document is the standard we hold every model to — including, eventually, our own mistakes. It is fixed, versioned, and published before our first verdict, so that no one can accuse the ruler of changing length after the measurement.

---

## 1. What we test

Our docket is driven by hype, not by our preferences. A model becomes a candidate when it achieves visible traction — arXiv citations and social pickup, Hugging Face downloads, or sustained fintwit attention. We disclose the hype metrics that earned each model its teardown at the top of every report.

We do not cherry-pick strawmen. If anything, our incentive runs the other way: a famous model that survives our gauntlet is a better story than an obscure one that dies. Selection disclosure exists so readers can judge whether our docket is representative. It is part of every teardown, permanently.

## 2. The test universe

Unless a paper specifies otherwise, models are evaluated on **liquid US large-cap equities**, with **SPY** (and QQQ where relevant) as the benchmark. This is deliberately ungenerous terrain: the most efficient, most-arbitraged market on earth. A model that only "works" on illiquid small-caps is not rejected — but it is flagged, because trading costs and capacity constraints in that space routinely erase paper returns.

Data comes from free, publicly documented sources (Yahoo Finance / Stooq for prices, SEC EDGAR for filings). Every dataset used in a teardown is cached and referenced so any reader can replay our exact inputs.

## 3. Costs, because reality has costs

The single most common way a published backtest lies is by omission: zero transaction costs, zero slippage, infinite liquidity. We apply **10 basis points per trade plus 5 basis points of slippage** to every strategy, no exceptions.

This is stricter than most academic papers. That is the point. A model with genuine edge should survive realistic friction; a model that only works in a frictionless vacuum works nowhere else either.

## 4. The honesty window

Here is the core of the standard, and the section we'd ask a skeptic to read twice.

Every paper defines its own in-sample and out-of-sample periods. We respect those — we reproduce the authors' claims on _their_ terms first. But then we add our own layer: **the honesty window — a minimum of twelve months of market data beginning after the model's public release date** (paper publication or model-hub upload, whichever is earlier).

The honesty window answers the only question that matters: _if you had believed the hype on the day everyone first believed the hype, what would have happened to your money?_ No parameter in this window can have influenced the model's design. It is the closest thing to a controlled experiment that markets allow.

## 5. The verdicts

Every teardown ends in exactly one of three verdicts. The thresholds are fixed:

**✅ REPLICATES**
The model's in-sample claims reproduce within reasonable tolerance, _and_ it retains **at least 70% of its claimed excess Sharpe** through the honesty window, net of our cost assumptions. This is a high bar on purpose. Most published strategies will never earn it — which is exactly what makes it meaningful when one does.

**⚠️ DEGRADES**
The in-sample claims reproduce, but honesty-window performance falls **30–70% short of claimed excess Sharpe**, or the strategy's edge exists only before realistic costs are applied. The model isn't fraudulent — it's fragile. The most common verdict, and the most useful one for readers: the idea may have merit, but the marketed version of it does not.

**❌ FAILS**
We cannot reproduce the paper's central claimed result at all, _or_ the model underperforms buy-and-hold SPY through the honesty window net of costs. When we issue a FAIL, we publish our complete pipeline so the authors — or anyone — can show us where we went wrong. Being publicly correctable is part of the design.

## 6. Metrics we trust (because we compute them)

Every number we publish is computed by our own harness directly from raw returns: **total return, Sharpe ratio, maximum drawdown, hit rate, and turnover.** We do not use any library's convenience statistics for published verdicts. During the build of this lab, a popular backtesting library shipped a silent bug in one of its convenience metrics — a useful reminder that in this field, "the library said so" is not evidence. The arithmetic behind every verdict ships with the verdict.

## 7. Reproducibility obligations

For every teardown, we publish: the complete test notebook, the cached input data (or exact retrieval instructions), the pinned environment (`requirements.txt`), and the coverage start date — the moment we began looking at the model, time-stamped by commit history. No retroactive claims, ever. If we revisit a model later, the revisit is dated and the original verdict stands on the record.

## 8. Versioning

This is Methodology **v1.0**. If the standard ever changes, the change is logged in a public changelog with reasons, and previously issued verdicts are annotated — never silently rewritten. An audit whose methods drift is just another opinion.

---

## What we are not

We are not investment advisors, and nothing we publish is investment advice. We are not short sellers of ideas — a REPLICATES verdict delights us as much as a FAIL. And we are not claiming that surviving our gauntlet makes a model safe to trade; it makes it _honest_, which is a different and rarer property.

## What we are

The scoreboard is public and permanent. Every model we've tested, every verdict, every honesty-window result, updated as the windows play out. Over time, that archive — not any single verdict — is the product: a time-stamped, reproducible record of which AI trading claims survived contact with reality.

The hype will keep arriving weekly. So will we.

---

_The Quant Audit — hyped models, honest verdicts._
_Methodology v1.0 · Changelog: initial publication._
