@"
# Hangman Solver (CSV -> CSV)

## Cum rulezi
python src/joc.py

## Structură
/src      - codul sursă (joc.py)
/data     - fișier CSV de intrare (cuvinte_de_verificat.csv)
/results  - rezultate generate (rezultate.csv)
/docs     - prezentarea PPTX

## Format I/O
Input CSV:  game_id,pattern_initial,cuvant_tinta
Output CSV: game_id,total_incercari,cuvant_gasit,status,secventa_incercari

## Ipoteze & limitări
- Se folosește o ordine fixă de ghicire a literelor.
- Fișierele sunt UTF-8, fără antet (sau scriptul ignoră primul rând dacă e antet).
"@ | Out-File README.md -Encoding utf8

"# doar biblioteca standard (csv, os); fără dependențe externe" | Out-File requirements.txt -Encoding utf8
