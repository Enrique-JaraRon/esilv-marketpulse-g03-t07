# Checkpoint B — Enrique Jara-Ron

- Nom : Enrique Jara-Ron
- GitHub : `Enrique-JaraRon`
- Branche TD08 : `feature/yahoo-provider`
- PR ouverte : [#5 — Yahoo Finance](https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07/pull/5)
- PR revue (TD07) : [#4 — Analytics](https://github.com/Enrique-JaraRon/esilv-marketpulse-g03-t07/pull/4) (review/commentaire effectué avec ce compte)
- Commits principaux : voir l'historique de la PR #5 ; commits initiaux `c1c7467` (provider) et `33093dc` (captures)

## Captures obligatoires

- `01_pull_request.png` — **à ajouter** avec une véritable capture de la PR TD07
- `02_code_review.png` — **à ajouter** avec une véritable capture de la review TD07
- `03_yahoo_market_data.png` — capture réelle du 13/11/2026 : AAPL et SP500 récupérés depuis Yahoo (23 lignes chacun)
- `04_instrument_benchmark.png` — **à refaire** après correction de l'affichage `Data provider : yahoo`, avec AAPL et SP500 sur le même lookback et intervalle

Les captures originales restent dans `evidence/Td8/`. L'ancienne capture `instrument_benchmark.png` y montre encore `Data provider : csv` bien que les valeurs aient été obtenues avec Yahoo ; ne pas la présenter comme preuve finale sans nouvelle exécution.

## Vérification TD08

Depuis la racine du dépôt :

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python src/main.py
```

Le dossier sera complet après ajout des captures TD07 et nouvelle capture de comparaison.
