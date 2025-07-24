"""
PortfolioTracker

A minimal class to simulate BTC portfolio performance
for options strategies. Tracks cumulative PnL, drawdowns, and balance
over time as trades are executed.

Used to separate simulation logic (PnL tracking, equity curve construction)
from strategy implementation and visualization.

Intended for backtesting weekly BTC options strategies like short strangles.

"""

import pandas as pd

class PortfolioTracker:
    def __init__(self, starting_balance_btc=1.0):
        self.starting_balance = starting_balance_btc
        self.records = []
        self.cumulative_pnl = 0.0
        self.rolling_max = 0.0

    def update(self, entry_date, pnl):
        self.cumulative_pnl += pnl
        self.rolling_max = max(self.rolling_max, self.cumulative_pnl)
        drawdown = self.cumulative_pnl - self.rolling_max
        balance = self.starting_balance + self.cumulative_pnl

        self.records.append({
            'entry_date': entry_date,
            'pnl': pnl,
            'cumulative_pnl': self.cumulative_pnl,
            'drawdown': drawdown,
            'btc_balance': balance
        })

    def to_dataframe(self):
        return pd.DataFrame(self.records)
