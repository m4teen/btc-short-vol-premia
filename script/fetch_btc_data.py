import yfinance as yf
import os

# Output file path
output_path = os.path.join("data", "btc_price.csv")

# Download historical BTC-USD data (daily since 2017)
btc = yf.download("BTC-USD", start="2017-01-01", interval="1d")

# Select relevant columns and reset index for CSV
columns_to_keep = ['Open', 'High', 'Low', 'Close', 'Volume']
btc_clean = btc[columns_to_keep].copy()
btc_clean.reset_index(inplace=True)  # Move 'Date' from index to column

# Save to CSV
btc_clean.to_csv(output_path, index=False)

print(f"BTC price data saved to {output_path}")
