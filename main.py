import pandas as pd
from strategy.sell_strangle import sell_strangle

# Load data
df = pd.read_csv("data/btc_price_enriched.csv", parse_dates=['Date'])
df.set_index('Date', inplace=True)

option_chain = pd.read_csv("data/options_chain.csv")

# Run strategy
results = sell_strangle(option_chain, df)

# Save or plot
results['cumulative_pnl'] = results['pnl'].cumsum()
results.set_index('entry_date')['cumulative_pnl'].plot(title="Cumulative PnL (ATM Strangle Strategy)")
