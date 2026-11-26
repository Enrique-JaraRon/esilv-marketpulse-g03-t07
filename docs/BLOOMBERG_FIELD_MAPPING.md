# Bloomberg Field Mapping

## Access mode

- Mode: `APPROVED_SAMPLE`
- Input: `data/sample/bloomberg_reference_sample.json`
- The fixture contains illustrative teaching values reused from `data/sample/prices.csv`.
- Live Bloomberg connectivity: not demonstrated.
- The instructor reference listed in TD09 was unavailable on team `main` at the time of review.

## Market instruments

| Role | MarketPulse ticker | Bloomberg identifier |
|---|---|---|
| Instrument | `AAPL` | `AAPL US Equity` |
| Benchmark | `SP500` | `SPX Index` |

## Sample inspection

The input contains a `series` array with two entries. Each entry has a
`role`, a `canonical_ticker`, a `provider_identifier`, and an `observations`
array.

Both series contain 21 daily observations on the same dates, from
2026-09-01 to 2026-09-30. All six observation fields are present and
non-null in every row.

| Ticker | First close | Last close | Volume |
|---|---:|---:|---|
| `AAPL` | 250.00 | 266.20 | Numeric values in all 21 rows |
| `SP500` | 6600 | 6742 | Explicitly `0` in all 21 rows |

## Field mapping

| MarketPulse field | Source in the approved sample | Notes |
|---|---|---|
| `date` | `observation_date` | Preserve the `YYYY-MM-DD` format. |
| `ticker` | Parent series' `canonical_ticker` | Use `AAPL` or `SP500` on every row. |
| `open` | `open_value` | Opening price or index level. |
| `high` | `high_value` | Session high. |
| `low` | `low_value` | Session low. |
| `close` | `close_value` | Closing price or index level. |
| `volume` | `volume_value` | Preserve the numeric value, including `0`. |

The observation keys are specific to the teaching sample.

## TD10 handoff

- Convert each observation into one MarketPulse row and copy the parent
  series' `canonical_ticker` into its `ticker` field.
- Keep dates as `YYYY-MM-DD` strings and prices and volumes as numbers.
  Preserve the explicit zero volume for `SP500`.
- Validate against `data/sample/bloomberg_reference_expected.json`.
  Applying this mapping reproduced all 42 expected rows in the same order.