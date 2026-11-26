Dans ce TD, nous avons modifié main.py pour afficher les informations d'Apple et du S&P 500.
puis nous avons utilisé load_instruments() et load_prices() pour lire les fichiers JSON et CSV.
Et avec filter_prices(), nous avons séparé les données des deux actifs.
Nous avons ajouté trois fonctions :get_first_close() pour récupérer le premier prix,
get_last_close() pour récupérer le dernier prix. et display_market_summary() pour afficher les résultats sans répéter le même code.
Nous avons aussi utilisé float() pour convertir les prix en nombres.
Le programme fonctionne avec python src/main.py et affiche les résultats attendus.