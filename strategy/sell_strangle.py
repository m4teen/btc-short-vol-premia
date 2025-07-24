import pandas as pd
from datetime import timedelta

def sell_strangle(option_chain, underlying_df):
    """
    Sell weekly ATM strangle using precomputed option chain.
    One call + one put sold at ATM strike, held to expiry.
    """

    # Parse and index properly
    option_chain['date'] = pd.to_datetime(option_chain['date'])
    option_chain['expiry'] = pd.to_datetime(option_chain['expiry'])
    option_chain.set_index('date', inplace=True)

    underlying_df = underlying_df.copy()
    underlying_df.index = pd.to_datetime(underlying_df.index)

    trade_log = []

    # Loop weekly (every 7 days)
    for i in range(0, len(underlying_df) - 7, 7):
        entry_date = underlying_df.index[i]
        expiry_date = entry_date + timedelta(days=7)

        try:
            spot = underlying_df.loc[entry_date]['Close']
            spot_expiry = underlying_df.loc[expiry_date]['Close']
        except KeyError:
            continue

        atm_strike = round(spot / 100) * 100  # ATM rounded to nearest 100

        # Get call and put options at ATM
        try:
            call = option_chain.loc[entry_date].query(
                "type == 'call' and strike == @atm_strike"
            )
            put = option_chain.loc[entry_date].query(
                "type == 'put' and strike == @atm_strike"
            )
        except (KeyError, AttributeError):
            continue

        if call.empty or put.empty:
            continue

        try:
            call_premium_val = float(call['premium'].values[0])
            put_premium_val = float(put['premium'].values[0])
        except IndexError:
            continue

        total_premium = call_premium_val + put_premium_val

        # Compute loss at expiry
        call_loss = max(0, spot_expiry - atm_strike)
        put_loss = max(0, atm_strike - spot_expiry)
        pnl = total_premium - (call_loss + put_loss)

        trade_log.append({
            'entry_date': entry_date,
            'expiry_date': expiry_date,
            'spot_entry': spot,
            'spot_expiry': spot_expiry,
            'strike': atm_strike,
            'call_premium': call_premium_val,
            'put_premium': put_premium_val,
            'total_premium': total_premium,
            'call_loss': call_loss,
            'put_loss': put_loss,
            'pnl': pnl
        })

    return pd.DataFrame(trade_log)
