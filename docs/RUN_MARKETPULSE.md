
# Running MarketPulse

## 1. Objective

MarketPulse is a Python application that displays
basic market information for an instrument and a benchmark.

The current configuration uses:
- AAPL — Apple Inc.
- SP500 — S&P 500

## 2. Requirements

- Python 3
- The MarketPulse repository

The application uses Python's standard library
for reading CSV and JSON files.

## 3. Run the application

Open a terminal at the repository root.

Check Python:

```bash
python --version
```

Run MarketPulse:

```bash
python src/main.py
```

## 4. Input files

The program reads two sample files:

- `data/sample/instruments.json`
  Contains the instrument and benchmark metadata.

- `data/sample/prices.csv`
  Contains historical daily prices.

Run the script from the repository root because
the current data path is relative.

## 5. Expected output

The program displays, for AAPL and SP500:

- Ticker and instrument name
- Number of observations
- First and last observation dates
- First and last closing prices

With the current sample data:

| Field | AAPL | SP500 |
|---|---|---|
| Observations | 21 | 21 |
| First date | 2026-09-01 | 2026-09-01 |
| Last date | 2026-09-30 | 2026-09-30 |
| First close | 250.00 | 6600.00 |
| Last close | 266.20 | 6742.00 |

## 6. Troubleshooting

If a sample file cannot be found, check that
the terminal is open at the repository root.

If the program fails, inspect the error message
and verify that both input files are present.

## 7. Validation

From the repository root:

```bash
python src/main.py
git status
```

The Python command should complete successfully.
