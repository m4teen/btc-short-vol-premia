import pandas as pd
import numpy as np
from datetime import timedelta
from scipy.stats import norm
import os

# ---- Black-Scholes Pricing ----
def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        delta = norm.cdf(d1)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        delta = -norm.cdf(-d1)
    return price, delta

# ---- Generate Chain ----
def generate_option_chain(df, strike_pcts=[-0.1, -0.05, 0.0, 0.05, 0.1], expiry_days=7):
    rows = []
    for current_date, row in df.iterrows():
        spot = row['Close']
        rv = row['realized_vol_10d']
        if pd.isna(rv) or spot <= 0:
            continue

        expiry_date = current_date + timedelta(days=expiry_days)
        T = expiry_days / 365
        r = 0.0

        for pct in strike_pcts:
            strike = round(spot * (1 + pct) / 100) * 100  # rounded to nearest 100

            for opt_type in ['call', 'put']:
                skew = 0.05 if opt_type == 'put' else -0.03
                iv = max(rv + skew, 0.01)
                premium, delta = black_scholes_price(spot, strike, T, r, iv, opt_type)

                rows.append({
                    'date': current_date.strftime('%Y-%m-%d'),
                    'expiry': expiry_date.strftime('%Y-%m-%d'),
                    'type': opt_type,
                    'strike': int(strike),
                    'spot': round(spot, 2),
                    'iv': round(iv, 4),
                    'premium': round(premium, 2),
                    'delta': round(delta, 4),
                })
    return pd.DataFrame(rows)

# ---- Run It ----
if __name__ == "__main__":
    df = pd.read_csv("data/btc_price_enriched.csv", parse_dates=['Date'])
    df.set_index('Date', inplace=True)
    chain = generate_option_chain(df)
    chain.to_csv("data/options_chain.csv", index=False)
    print("✅ options_chain.csv saved to data/")
