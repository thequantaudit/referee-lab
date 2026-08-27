import yfinance as yf
import vectorbt as vbt
from harness.evaluator import StrategyEvaluator

data = yf.download("SPY", start="2022-01-01", end="2024-12-31")["Close"].squeeze()

fast = vbt.MA.run(data, 10)
slow = vbt.MA.run(data, 50)
entries = fast.ma_crossed_above(slow)
exits = fast.ma_crossed_below(slow)

evaluator = StrategyEvaluator(data, fees=0.001, slippage=0.0005)
results = evaluator.evaluate_signals(entries, exits)

print("Compliant Harness Metrics:")
for metric, val in results.items():
    print(f"  {metric}: {val}")
