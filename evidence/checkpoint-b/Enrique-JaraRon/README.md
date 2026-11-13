# Checkpoint B — Enrique Jara-Ron

**GitHub:** `Enrique-JaraRon`  
**Équipe:** G03-T07  
**Branche TD08:** `feature/yahoo-provider`  
**PR créée (TD08):** [#5 — Yahoo Finance](https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07/pull/5) — ouverte, non mergée  
**PR créée auparavant:** [#1 — documentation](https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07/pull/1) et [#3 — data provider](https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07/pull/3)  
**PR revue:** [#4 — analytics (TD07)](https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07/pull/4) — review COMMENTED enregistrée par Enrique-JaraRon ; également [#2](https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07/pull/2)  
**Commits TD08:** `c1c7467` (provider), `33093dc` (preuves), `1872e24` (corrections et tests), et le commit d'organisation des preuves sur la PR #5.

## Captures

| Fichier | Origine vérifiable | Réserve éventuelle |
| --- | --- | --- |
| `01_pull_request.png` | Capture existante de la PR #4 du **TD07**, réalisée par l'équipe | La PR est celle de Mathis ; les PR personnelles d'Enrique sont #1, #3 et #5 (liens ci-dessus). |
| `02_code_review.png` | Capture existante de la PR #2 avec un commentaire d'Enrique (TD précédent) | Ce n'est pas la capture de sa review formelle du TD07 (#4). Le lien de sa review TD07 est fourni ci-dessus. |
| `03_yahoo_market_data.png` | Capture originale du TD08, récupération réelle AAPL et SP500 (23 observations chacun) | Capture authentique et inchangée. |
| `04_instrument_benchmark.png` | Capture originale du TD08, comparaison AAPL et SP500 sur 23 dates communes | L'ancien affichage indique à tort `Data provider : csv` : ce défaut de libellé est corrigé dans le code de la branche. **Remplacer par une nouvelle capture après exécution** pour une preuve finale sans ambiguïté. |

Les captures sont **reprises sans retouche** des dossiers `evidence/td7/`, `evidence/td6/` et `evidence/Td8/`. Les originaux sont conservés.

## Validation

- `requirements.txt` inclut `yfinance`.
- Le provider conserve le format canonique (`date`, `ticker`, OHLC en `float`, `volume` en `int`) et les tickers `AAPL`/`SP500`.
- `src/analytics.py` est inchangé par la PR #5.
- Quatre tests unitaires du provider ont été exécutés dans un environnement isolé avec téléchargement Yahoo simulé : **4 OK**. Cette vérification ne remplace pas un test de téléchargement réel.
- La capture `03_yahoo_market_data.png` établit qu'un téléchargement Yahoo réel avait réussi le 13 novembre 2026.

Pour revérifier sur VS Code et remplacer la capture `04` :

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python src/main.py
```

La validation finale des preuves et l'approbation de la PR restent du ressort de l'équipe / du professeur. **Ne pas merger avant la review.**
