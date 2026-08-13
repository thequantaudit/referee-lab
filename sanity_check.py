import vectorbt as vbt
import yfinance as yf

price = yf.download("SPY", start="2020-01-01", end="2024-12-31")["Close"].squeeze()
fast = vbt.MA.run(price, 10)
slow = vbt.MA.run(price, 50)
entries = fast.ma_crossed_above(slow)
exits = fast.ma_crossed_below(slow)
pf = vbt.Portfolio.from_signals(price, entries, exits, fees=0.001, freq="1D")
print("Total Return [%]:", round(float(pf.total_return()) * 100, 2))
print("Sharpe Ratio:", round(float(pf.sharpe_ratio()), 2))
print("Max Drawdown [%]:", round(float(pf.max_drawdown()) * 100, 2))
print("Total Trades:", int(pf.trades.count()))
