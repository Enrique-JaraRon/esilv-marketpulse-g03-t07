
import math

import pandas as pd
import yfinance as yf


CANONICAL_TO_YAHOO = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(
    canonical_ticker,
    lookback="1mo",
    interval="1d"
):
    if canonical_ticker not in CANONICAL_TO_YAHOO:
        raise ValueError(f"Unknown ticker: {canonical_ticker}")

    yahoo_symbol = CANONICAL_TO_YAHOO[canonical_ticker]

    raw = yf.download(
        yahoo_symbol,
        period=lookback,
        interval=interval,
        auto_adjust=False,
        progress=False,
    )

    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = raw.columns.get_level_values(0)

    rows = []

    for date, values in raw.iterrows():
        prices = [
            values["Open"],
            values["High"],
            values["Low"],
            values["Close"],
        ]

        if any(pd.isna(value) for value in prices):
            continue

        volume = values["Volume"]
        if pd.isna(volume):
            volume = 0

        row = {
            "date": date.strftime("%Y-%m-%d"),
            "ticker": canonical_ticker,
            "open": float(values["Open"]),
            "high": float(values["High"]),
            "low": float(values["Low"]),
            "close": float(values["Close"]),
            "volume": int(volume),
        }

        rows.append(row)

    rows.sort(key=lambda row: row["date"])

    return rows
