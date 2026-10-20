TD4 : terminal

@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ cat src/main.py
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


def display_market_summary(asset, prices, show_currency=True):
    # On récupère les deux prix pour chaque actif
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)

    # On ajoute la devise si on veut l'afficher
    currency = f" {asset['currency']}" if show_currency else ""

    # Affichage des informations
    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Observations : {len(prices)}")
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
@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ python src/main.py
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First date  : 2026-09-01
Last date   : 2026-09-30
First close : 250.00 USD
Last close  : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First date  : 2026-09-01
Last date   : 2026-09-30
First close : 6600.00
Last close  : 6742.00
@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git branch --show-current
feature/display-observation-dates
@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git status
On branch feature/display-observation-dates
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   src/main.py

no changes added to commit (use "git add" and/or "git commit -a")
@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git diff
diff --git a/src/main.py b/src/main.py
index c0dca5e..9b42a9d 100644
--- a/src/main.py
+++ b/src/main.py
@@ -35,6 +35,12 @@ def get_last_close(prices):
     # Pareil mais avec le dernier prix
     return float(prices[-1]["close"])
 
:...skipping...
diff --git a/src/main.py b/src/main.py
index c0dca5e..9b42a9d 100644
--- a/src/main.py
+++ b/src/main.py
@@ -35,6 +35,12 @@ def get_last_close(prices):
     # Pareil mais avec le dernier prix
     return float(prices[-1]["close"])
 
+def get_first_date(prices):
+    return prices[0]["date"]
+
+def get_last_date(prices):
+    return prices[-1]["date"]
:...skipping...
diff --git a/src/main.py b/src/main.py
index c0dca5e..9b42a9d 100644
--- a/src/main.py
+++ b/src/main.py
@@ -35,6 +35,12 @@ def get_last_close(prices):
     # Pareil mais avec le dernier prix
     return float(prices[-1]["close"])
 
+def get_first_date(prices):
+    return prices[0]["date"]
+
+def get_last_date(prices):
+    return prices[-1]["date"]
+
 
 def display_market_summary(asset, prices, show_currency=True):
     # On récupère les deux prix pour chaque actif
:...skipping...
diff --git a/src/main.py b/src/main.py
index c0dca5e..9b42a9d 100644
--- a/src/main.py
+++ b/src/main.py
@@ -35,6 +35,12 @@ def get_last_close(prices):
     # Pareil mais avec le dernier prix
     return float(prices[-1]["close"])
 
+def get_first_date(prices):
+    return prices[0]["date"]
+
+def get_last_date(prices):
+    return prices[-1]["date"]
+
 
 def display_market_summary(asset, prices, show_currency=True):
     # On récupère les deux prix pour chaque actif
@@ -47,8 +53,11 @@ def display_market_summary(asset, prices, show_currency=True):
     # Affichage des informations
@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git add src/main.py
@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git --no-pager diff --staged
diff --git a/src/main.py b/src/main.py
index c0dca5e..9b42a9d 100644
--- a/src/main.py
+++ b/src/main.py
@@ -35,6 +35,12 @@ def get_last_close(prices):
     # Pareil mais avec le dernier prix
     return float(prices[-1]["close"])
 
+def get_first_date(prices):
+    return prices[0]["date"]
+
+def get_last_date(prices):
+    return prices[-1]["date"]
+
 
 def display_market_summary(asset, prices, show_currency=True):
     # On récupère les deux prix pour chaque actif
@@ -47,8 +53,11 @@ def display_market_summary(asset, prices, show_currency=True):
     # Affichage des informations
     print(f"{asset['ticker']} - {asset['name']}")
     print(f"Observations : {len(prices)}")
+    print(f"First date  : {get_first_date(prices)}")
+    print(f"Last date   : {get_last_date(prices)}")
     print(f"First close : {first_close:.2f}{currency}")
     print(f"Last close  : {last_close:.2f}{currency}")
+    
 
 
 def main():
@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git commit -m "feat: display first and last observation dates"
[feature/display-observation-dates b955bee] feat: display first and last observation dates
 1 file changed, 9 insertions(+)

@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git status
On branch feature/display-observation-dates
nothing to commit, working tree clean

@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git log --oneline -3
b955bee (HEAD -> feature/display-observation-dates) feat: display first and last observation dates
9596943 (origin/main, origin/HEAD, main) Add files via upload
f24b71c docs: add simple comments to MarketPulse code

@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git --no-pager log --oneline --graph --decorate --all
* b955bee (HEAD -> feature/display-observation-dates) feat: display first and last observation dates
| *   0c580e1 (origin/Mathis, Mathis) Merge branch 'main' of https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07 into Mathis
| |\  
| |/  
|/|   
* | 9596943 (origin/main, origin/HEAD, main) Add files via upload
* | f24b71c docs: add simple comments to MarketPulse code
* | 1f7af0b Evidences du td2 et td3
* | 5e49bbd création des fichiers dans evidence
* | d2ebfc3  TD02 + TD03
| * a8d46ed chore: recover files from main
|/  
* e1e81f4 (origin/rudy) rendu td 1
* 5848035 Delete TEAM_TEMPLATE.md
* 982aaa1 student changes
* 97fb916 team.md changements
| * d0cde12 (origin/patch-1) Rename TEAM_TEMPLATE.md to TEAM.md
|/  
* 5207db8 first td session
* ba5c9f4 Update Readme
* 9fd6c8a Update Readme
* bfb94a6 init projecttemplate
@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git --no-pager diff main..feature/display-observation-dates
diff --git a/src/main.py b/src/main.py
index c0dca5e..9b42a9d 100644
--- a/src/main.py
+++ b/src/main.py
@@ -35,6 +35,12 @@ def get_last_close(prices):
     # Pareil mais avec le dernier prix
     return float(prices[-1]["close"])
 
+def get_first_date(prices):
+    return prices[0]["date"]
+
+def get_last_date(prices):
+    return prices[-1]["date"]
+
 
 def display_market_summary(asset, prices, show_currency=True):
     # On récupère les deux prix pour chaque actif
@@ -47,8 +53,11 @@ def display_market_summary(asset, prices, show_currency=True):
     # Affichage des informations
     print(f"{asset['ticker']} - {asset['name']}")
     print(f"Observations : {len(prices)}")
+    print(f"First date  : {get_first_date(prices)}")
+    print(f"Last date   : {get_last_date(prices)}")
     print(f"First close : {first_close:.2f}{currency}")
     print(f"Last close  : {last_close:.2f}{currency}")
+    
 
 
 def main():

@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (feature/display-observation-dates) $ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (main) $ git merge feature/display-observation-dates
Updating 9596943..b955bee
Fast-forward
 src/main.py | 9 +++++++++
 1 file changed, 9 insertions(+)

@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (main) $ python src/main.py
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First date  : 2026-09-01
Last date   : 2026-09-30
First close : 250.00 USD
Last close  : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First date  : 2026-09-01
Last date   : 2026-09-30
First close : 6600.00
Last close  : 6742.00

@Mathis2103 ➜ /workspaces/esilv-marketpulse-g03-t07 (main) $ 