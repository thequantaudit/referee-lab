import numpy as np
import pandas as pd
import vectorbt as vbt

class StrategyEvaluator:
    """
    Standardized referee evaluation engine (Methodology v1.0).
    Core metrics computed from raw returns — never library convenience stats.
    """
    def __init__(self, price_series: pd.Series, fees: float = 0.001, slippage: float = 0.0005):
        self.price = price_series.squeeze()
        self.fees = fees
        self.slippage = slippage

    def evaluate_signals(self, entries: pd.Series, exits: pd.Series) -> dict:
        pf = vbt.Portfolio.from_signals(
            self.price, entries=entries, exits=exits,
            fees=self.fees, slippage=self.slippage, freq="1D"
        )

        equity = pf.value().values.astype(float)
        rets = pd.Series(equity).pct_change().dropna().values

        total_return = equity[-1] / equity[0] - 1
        sharpe = (rets.mean() / rets.std()) * np.sqrt(252) if rets.std() > 0 else 0.0
        peak = np.maximum.accumulate(equity)
        max_dd = float(((equity - peak) / peak).min())
        bench_return = float(self.price.iloc[-1] / self.price.iloc[0] - 1)

        n_trades = int(pf.trades.count())
        win_rate = None  # filled from trade records in a later iteration

        return {
            "Total Return [%]": round(total_return * 100, 2),
            "Benchmark Return [%]": round(bench_return * 100, 2),
            "Sharpe Ratio": round(float(sharpe), 2),
            "Max Drawdown [%]": round(max_dd * 100, 2),
            "Total Trades": n_trades,
        }