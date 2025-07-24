# Strategy Analysis: BTC-Denominated Short ATM Strangle

---

This section presents a performance breakdown of the short
at-the-money (ATM) strangle strategy when evaluated in BTC
terms. Unlike traditional USD-denominated metrics, BTC-based
evaluation highlights risk and reward from the perspective of a
crypto-native balance sheet.

## Strategy Overview

The strategy involves selling weekly ATM strangles on BTC options — a
directionally neutral position that benefits from time decay (theta)
and stable implied volatility. It's a classic short volatility trade
structure.

## Performance Summary

### Key statistics:

| Metric            |	Value              |
|-------------------|----------------------|
| Sharpe Ratio	    | Very low (negative)  |
| Win Rate	        | ~58%                 |
| Max Drawdown	    | ~59% (BTC terms)     |
| Final BTC Balance	| Deep negative        |

Despite a decent win rate, the negative skew and extreme downside tail
events dominate long-term performance.

### Equity Curve

The equity curve reveals large cumulative losses with occasional sharp
recoveries. It reflects the asymmetric risk profile of short
strangles: frequent small gains punctuated by rare but extreme
losses. The pattern is characteristic of volatility-selling strategies
that aren't sufficiently hedged.

### Weekly PnL

The weekly PnL plot shows the distribution of returns over time. While
most weeks yield modest profits, tail risk events cause significant
losses. Volatility spikes in 2020–2021 and again in 2024 visibly
damage the performance.

### PnL Distribution

Returns are not normally distributed — they are fat-tailed and heavily
skewed to the left. A small cluster of extremely negative weeks is
responsible for the bulk of the drawdown. This confirms that the risk
is not diversifiable by time alone.

### Drawdown & Cumulative PnL

![Sell Strangle Four Chart Panel](./figures/sell_strangle_4_chart_panel.png)

The panel above combines:

- Weekly PnL
- Cumulative PnL
- Drawdown
- Histogram

It reinforces the view that BTC-denominated short strangles without
proper hedging are vulnerable to volatility shocks. The strategy
performs reasonably in low-vol regimes but collapses when volatility
surges.

## Insights & Considerations

- BTC as Numeraire: Evaluating in BTC emphasizes that the strategy
  loses BTC over time — important for crypto-native portfolios.
- Tail Risk Dominance: Typical short vol behavior — many small gains,
  few catastrophic losses.
- Risk Mitigation Required: Vanilla short strangles should be
  complemented with dynamic hedging, stop-losses, or long-tail
  protection.

## Takeaway
The BTC-denominated short ATM strangle strategy, while conceptually
attractive due to its simplicity, is structurally exposed to
volatility spikes. In its raw, unhedged form, it leads to large
cumulative losses and drawdowns. This reinforces the need for
tail-risk management and stress testing when applying short-volatility
strategies in crypto markets.
