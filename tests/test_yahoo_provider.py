import unittest
from unittest.mock import patch

import pandas as pd
from src.providers.yahoo_provider import fetch_yahoo_prices


class TestYahooProvider(unittest.TestCase):
    @patch("src.providers.yahoo_provider.yf.download")
    def test_sp500_canonical_rows(self, mock_download):
        raw = pd.DataFrame(
            {
                "Open": [101.0, 99.0],
                "High": [102.0, 100.0],
                "Low": [100.0, 98.0],
                "Close": [101.5, 99.5],
                "Volume": [None, 123],
            },
            index=pd.to_datetime(["2026-11-12", "2026-11-11"]),
        )
        raw.columns = pd.MultiIndex.from_product([raw.columns, ["^GSPC"]])
        mock_download.return_value = raw

        rows = fetch_yahoo_prices("SP500")

        mock_download.assert_called_once_with(
            "^GSPC", period="1mo", interval="1d",
            auto_adjust=False, progress=False
        )
        self.assertEqual([row["date"] for row in rows], ["2026-11-11", "2026-11-12"])
        self.assertEqual(
            set(rows[0]),
            {"date", "ticker", "open", "high", "low", "close", "volume"}
        )
        self.assertTrue(all(row["ticker"] == "SP500" for row in rows))
        self.assertIs(type(rows[0]["close"]), float)
        self.assertIs(type(rows[0]["volume"]), int)
        self.assertEqual(rows[1]["volume"], 0)

    def test_unknown_ticker(self):
        with self.assertRaises(ValueError):
            fetch_yahoo_prices("UNKNOWN")

    @patch("src.providers.yahoo_provider.yf.download")
    def test_empty_response(self, mock_download):
        mock_download.return_value = pd.DataFrame()
        with self.assertRaisesRegex(RuntimeError, "no data"):
            fetch_yahoo_prices("AAPL")

    @patch("src.providers.yahoo_provider.yf.download")
    def test_missing_close_is_skipped(self, mock_download):
        mock_download.return_value = pd.DataFrame({
            "Open": [10, 11],
            "High": [11, 12],
            "Low": [9, 10],
            "Close": [float("nan"), 11.5],
            "Volume": [100, 200],
        }, index=pd.to_datetime(["2026-11-11", "2026-11-12"]))
        rows = fetch_yahoo_prices("AAPL")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["date"], "2026-11-12")


if __name__ == "__main__":
    unittest.main()
