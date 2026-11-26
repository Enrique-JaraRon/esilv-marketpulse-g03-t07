import json
from pathlib import Path


SAMPLE_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "sample"
    / "bloomberg_reference_sample.json"
)


def load_approved_observations(canonical_ticker):
    with SAMPLE_PATH.open(encoding="utf-8") as sample_file:
        sample = json.load(sample_file)

    for series in sample["series"]:
        if series["canonical_ticker"] == canonical_ticker:
            return series["observations"]

    raise ValueError(f"Ticker introuvable dans APPROVED_SAMPLE : {canonical_ticker}")

def normalize_bloomberg_history(raw_data, canonical_ticker):
    rows = []

    for observation in raw_data:
        rows.append({
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })

    return rows

def load_bloomberg_history(canonical_ticker):
    observations = load_approved_observations(canonical_ticker)
    return normalize_bloomberg_history(observations, canonical_ticker)