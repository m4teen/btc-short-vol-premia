# Methodology and Build Log

This document outlines the development process, design decisions, and
thought process behind the BTC-Denominated Short Volatility Strategy
Simulator project.

---

## 1. Motivation

This project was driven by a desire to gain **hands-on experience
across the full lifecycle of a quant strategy**, including:

- Sourcing and cleaning real financial data
- Constructing synthetic instruments (options)
- Designing and implementing systematic strategies
- Tracking performance and risk metrics
- Visualizing and interpreting results

I chose this problem space because:

- BTC options markets are growing rapidly but still relatively
  underexplored
- Denominating all returns in BTC (rather than USD) introduces unique
  risk perspectives
- Short-volatility strategies (e.g. selling ATM strangles) are simple
  yet powerful tools to study payoff structures and risk dynamics

This project was intended not just as a simulation, but as an
end-to-end sandbox for thinking like a quant reseacher: hypothesis,
implementation, testing, and iteration.

---

## 2. Development Steps

### Step 1: Download BTC Spot Data
- Used `yfinance` to download daily BTC-USD data from 2017 onward
- Run `script/fetch_btc_data.py`
- Cleaned and saved as `data/btc_price.csv`

### Step 2: Enrich the BTC Dataset
- Calculated log returns and 10-day realised volatility (see `notebook/btc_price_analysis.ipynb`)
- Created volatility regime labels: "high" vs "low"
- Saved enriched data to `btc_price_enriched.csv`

### Step 3: Generate Synthetic Options Chain
- For each week:
  - Chose ATM strikes (rounded to nearest 100)
  - Estimated IV from realised volatility, with call/put skew
  - Priced options using Black-Scholes
- Output saved to `options_chain.csv`

### Step 4: Implement Strategy Logic
- Strategy: Sell 1 ATM call + 1 ATM put weekly (short strangle)
- No hedging, no early exit
- PnL = Premium received - max(call payoff, put payoff)
- Held to expiry

### Step 5: Run Simulation
- Simulated weekly PnL and cumulative BTC balance
- Added logic for drawdowns, equity curve, and rolling returns
- Saved results to `results` DataFrame for visualization

### Step 6: Analyze Performance
- Visualized:
  - Weekly PnL (bar chart)
  - Cumulative balance (line chart)
  - Drawdowns
  - PnL distribution
- Calculated:
  - Sharpe Ratio
  - Win Rate
  - Max Drawdown %
  - Final BTC balance

---

## 3. Assumptions and Simplifications

To keep the baseline version clean, I made the following assumptions:
- No transaction costs or slippage
- No margin requirements or leverage
- Implied volatility ~ 10-day realized volatility +/- skew
- No early exits or stop-losses
- Options expire weekly without gaps

These will be addressed in future extensions.

---

## 4. Sample Results (Illustrative)

| Metric             | Value (Example) |
|--------------------|------------------|
| Sharpe Ratio       | ~0.85            |
| Win Rate           | ~62%             |
| Max Drawdown       | ~-19%            |
| Final BTC Balance  | ~3.4 BTC         |

---

## 5. Future Extensions

This system is modular and ready for enhancement. Planned next steps
include:

- Adding BTC-collateralised margin accounting
- Incorporating execution costs and bid-ask spreads
- Creating filters (e.g. low-volatility regime only)
- Comparing strategies (long straddle, OTM puts, delta hedging)
- Simulating dynamic sizing based on BTC equity

---

## 6. Reflections and Learnings

This project helped me deeply understand:
- The shape of option payoffs and volatility risk premia
- How realised and implied volatility diverge in practice
- How to structure reusable backtests in Python
- The tradeoffs between realism and simplicity in simulation

---

- [Project Repo](https://github.com/m4teen/btc-short-vol-premia)
- [1-Page Report](../report/btc_summary.pdf)
