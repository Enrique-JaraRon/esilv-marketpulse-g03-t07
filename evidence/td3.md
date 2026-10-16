Dans ce TD, nous avons appris à utiliser Git pour suivre les modifications de notre code.
Nous avons commencé par git status pour voir les fichiers modifiés, puis git diff pour regarder les changements.
Ensuite, nous avons utilisé git add src/main.py pour préparer notre fichier et git diff --staged pour vérifier les modifications.
Après avoir testé le programme nous avons créé un commit avec git commit.
Enfinnous avons utilisé git log --oneline et git show HEAD pour consulter l'historique.
Nous avons compris la différence entre modifier un fichier, le préparer avec git add et enregistrer les changements avec git commit.Le commit a été fait en local, et push.

voici le code brut :

+    print("Instrument")
+    display_market_summary(instrument, instrument_prices)
     print()
-    print("Observations")
-    print(f"{instrument['ticker']}: {len(instrument_prices)}")
-    print(f"{benchmark['ticker']}: {len(benchmark_prices)}")
 
+    print("Benchmark")
+    display_market_summary(benchmark, benchmark_prices, show_currency=False)
 
 if __name__ == "__main__":
     main()
+    
\ No newline at end of file
@Enrique-JaraRon ➜ /workspaces/esilv-marketpulse-g03-t07 (main) $ 
@Enrique-JaraRon ➜ /workspaces/esilv-marketpulse-g03-t07 (main) $ python src/main.py
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First close : 250.00 USD
Last close  : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First close : 6600.00
Last close  : 6742.00
@Enrique-JaraRon ➜ /workspaces/esilv-marketpulse-g03-t07 (main) $ git commit -m " TD03 check et commit " git add src/main.py
git diff --staged --check
python src/main.py
error: pathspec 'git' did not match any file(s) known to git
error: pathspec 'add' did not match any file(s) known to git
src/main.py:75: trailing whitespace.
+    
src/main.py:75: new blank line at EOF.
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First close : 250.00 USD
Last close  : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First close : 6600.00
Last close  : 6742.00
@Enrique-JaraRon ➜ /workspaces/esilv-marketpulse-g03-t07 (main) $ git commit -m " TD02 + TD03 "
[main d2ebfc3]  TD02 + TD03
 1 file changed, 29 insertions(+), 15 deletions(-)
@Enrique-JaraRon ➜ /workspaces/esilv-marketpulse-g03-t07 (main) $ git log --oneline
git show HEAD
git status
d2ebfc3 (HEAD -> main)  TD02 + TD03
e1e81f4 (origin/main, origin/HEAD) rendu td 1
5848035 Delete TEAM_TEMPLATE.md
982aaa1 student changes
97fb916 team.md changements
5207db8 first td session
ba5c9f4 Update Readme
9fd6c8a Update Readme
bfb94a6 init projecttemplate
commit d2ebfc329dfce691094996e5690cf1b3e0d7dba6 (HEAD -> main)
Author: Enrique Jara Ron <enrique.jararon@gmail.com>
Date:   Fri Oct 16 14:31:24 2026 +0000

     TD02 + TD03

diff --git a/src/main.py b/src/main.py
index 884b045..ba99770 100644
--- a/src/main.py
+++ b/src/main.py
@@ -25,6 +25,26 @@ def load_prices():
 def filter_prices(prices, ticker):
     return [row for row in prices if row["ticker"] == ticker]
 
+def get_first_close(prices):
+    return float(prices[0]["close"])
+
+def get_last_close(prices):
+    return float(prices[-1]["close"])
+
+
+def display_market_summary(asset, prices, show_currency=True):
+    first_close = get_first_close(prices)
+    last_close = get_last_close(prices)
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   src/main.py

no changes added to commit (use "git add" and/or "git commit -a")
@Enrique-JaraRon ➜ /workspaces/esilv-marketpulse-g03-t07 (main) $ 