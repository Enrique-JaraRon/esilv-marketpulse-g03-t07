
from pathlib import Path
import csv
import json
from providers.yahoo_provider import fetch_yahoo_prices
from analytics import (
    align_series,
    calculate_period_return,
    calculate_base_100,
    calculate_relative_performance,
)


DATA_DIR = Path("data/sample")

LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"

PROVIDER = "yahoo"
LOOKBACK = "1mo"
INTERVAL = "1d"

def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    return float(prices[0]["close"])


def get_last_close(prices):
    return float(prices[-1]["close"])


def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def display_market_summary(asset, prices, show_currency=True):
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)
    first_date = get_first_date(prices)
    last_date = get_last_date(prices)

    currency = f" {asset['currency']}" if show_currency else ""

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Market      : {asset['market']}")
    print(f"Data provider : {PROVIDER}")
    print(f"Observations : {len(prices)}")
    print(f"First date  : {first_date}")
    print(f"Last date   : {last_date}")
    print(f"First close : {first_close:.2f}{currency}")
    print(f"Last close  : {last_close:.2f}{currency}")



def main():
    
    instruments = load_instruments()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    if PROVIDER == "csv":
        prices = load_prices()

        instrument_prices = filter_prices(
            prices, instrument["ticker"]
        )
        benchmark_prices = filter_prices(
            prices, benchmark["ticker"]
        )

    elif PROVIDER == "yahoo":
        instrument_prices = fetch_yahoo_prices(
            instrument["ticker"],
            lookback=LOOKBACK,
            interval=INTERVAL
        )
        benchmark_prices = fetch_yahoo_prices(
            benchmark["ticker"],
            lookback=LOOKBACK,
            interval=INTERVAL
        )

    else:
        raise ValueError(f"Unknown provider: {PROVIDER}")


    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print(f"Period        : {LOOKBACK_LABEL}")
    print(f"Interval      : {INTERVAL_LABEL}")
    print()

    print("Instrument")
    display_market_summary(instrument, instrument_prices)
    print()

    print("Benchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices, benchmark_prices
    )

    if not aligned_instrument:
        raise RuntimeError("No common trading sessions for AAPL and SP500.")

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    relative_performance = calculate_relative_performance(
        instrument_return, benchmark_return
    )

    instrument_base_100 = calculate_base_100(aligned_instrument)
    benchmark_base_100 = calculate_base_100(aligned_benchmark)

    print()
    print("Comparison (aligned)")
    print(f"Aligned sessions     : {len(aligned_instrument)}")
    print(f"{instrument['ticker']} period return   : {instrument_return:+.2f}%")
    print(f"{benchmark['ticker']} period return  : {benchmark_return:+.2f}%")
    print(f"Relative performance : {relative_performance:+.2f} percentage points")

    print()
    print("Base 100")
    print(
        f"{instrument['ticker']} : "
        f"{instrument_base_100[0]['value']:.2f} -> "
        f"{instrument_base_100[-1]['value']:.2f}"
    )
    print(
        f"{benchmark['ticker']} : "
        f"{benchmark_base_100[0]['value']:.2f} -> "
        f"{benchmark_base_100[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()

