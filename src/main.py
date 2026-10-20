from pathlib import Path
import csv
import json


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_close(prices):
    # On prend le premier prix et on le convertit en float
    return float(prices[0]["close"])


def get_last_close(prices):
    # Pareil mais avec le dernier prix
    return float(prices[-1]["close"])

def get_first_date(prices):
    return prices[0]["date"]

def get_last_date(prices):
    return prices[-1]["date"]


def display_market_summary(asset, prices, show_currency=True):
    # On récupère les deux prix pour chaque actif
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)

    # On ajoute la devise si on veut l'afficher
    currency = f" {asset['currency']}" if show_currency else ""

    # Affichage des informations
    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Observations : {len(prices)}")
    print(f"First date  : {get_first_date(prices)}")
    print(f"Last date   : {get_last_date(prices)}")
    print(f"First close : {first_close:.2f}{currency}")
    print(f"Last close  : {last_close:.2f}{currency}")
    


def main():
    # On charge les fichiers JSON et CSV
    instruments = load_instruments()
    prices = load_prices()

    # On récupère Apple et son benchmark
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    # On garde seulement les lignes correspondant à chaque actif
    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print(f"Period   : {LOOKBACK_LABEL}")
    print(f"Interval : {INTERVAL_LABEL}")
    print()

    # Résumé pour Apple
    print("Instrument")
    display_market_summary(instrument, instrument_prices)
    print()

    # Même fonction pour le S&P 500, sans afficher la devise
    print("Benchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)


if __name__ == "__main__":
    main()
