
import csv


INPUT_CSV  = "cuvinte_de_verificat.csv"
OUTPUT_CSV = "rezultate.csv"

ORDINE_GHICIRE = [
    "A","E","I","R","L",
    "O","T","N","U","C",
    "S","Ă","M","D","P","G","B","F","Ț","Ș","V","Z","H","Â",
    "Î","J","K","X","Y","W","Q"
]


def aflare_litere_hint(litere_ajutatoare: list[str]) -> list[str]:
    litere_hint = []
    for caracter in litere_ajutatoare:
        if caracter.isalpha():
            litere_hint.append(caracter)
    return litere_hint


def masca(cuvant: str, revealed: set[str]) -> str:
    litere_afisate = []
    for litera in cuvant:
        if litera in revealed:
            litere_afisate.append(litera)
        else:
            litere_afisate.append("_")
    rezultat = " ".join(litere_afisate)
    return rezultat


def toate_descoperite(cuvant: str, revealed: set[str]) -> bool:
    for litera in cuvant:
        if litera not in revealed:
            return False
    return True


def joaca_un_joc(pattern_initial: str, cuvant_tinta: str):
    litere_ajutatoare = pattern_initial
    TARGET = cuvant_tinta

    litere_hint = set(aflare_litere_hint(litere_ajutatoare))
    revealed = {ch for ch in TARGET if ch in litere_hint}
    incercate = set(litere_hint)

    pasi = 0
    corecte = 0
    gresite = 0
    secventa = []

    for lit in ORDINE_GHICIRE:
        if toate_descoperite(TARGET, revealed):
            break
        if lit in incercate:
            continue

        pasi += 1
        incercate.add(lit)
        secventa.append(lit)

        if lit in TARGET:
            corecte += 1
            for ch in TARGET:
                if ch == lit:
                    revealed.add(ch)
        else:
            gresite += 1

    status = "OK" if toate_descoperite(TARGET, revealed) else "FAIL"
    secventa_str = " ".join(l.lower() for l in secventa)
    return pasi, TARGET, status, secventa_str


def citeste_intrari_din_csv(cale_input: str):
    intrari = []
    with open(cale_input, "r", encoding="utf-8", newline="") as f:
        rdr = csv.reader(f)
        rows = list(rdr)

    if not rows:
        return intrari

    start_idx = 0
    if rows[0] and (not rows[0][0].strip().isdigit()):
        start_idx = 1

    for row in rows[start_idx:]:
        if not row:
            continue
        game_id = row[0].strip()
        pattern_initial = row[1].strip() if len(row) > 1 else ""
        cuvant_tinta = row[2].strip() if len(row) > 2 else ""
        if not game_id or not cuvant_tinta:
            continue
        intrari.append((game_id, pattern_initial, cuvant_tinta))
    return intrari


def scrie_rezultate_in_csv(cale_output: str, rezultate):
    with open(cale_output, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["game_id", "total_incercari", "cuvant_gasit", "status", "secventa_incercari"])
        for r in rezultate:
            w.writerow(r)


def main():
    intrari = citeste_intrari_din_csv(INPUT_CSV)
    rezultate = []
    for game_id, pattern_initial, cuvant_tinta in intrari:
        pasi, cuvant_gasit, status, secventa = joaca_un_joc(pattern_initial, cuvant_tinta)
        rezultate.append((game_id, pasi, cuvant_gasit, status, secventa))
    scrie_rezultate_in_csv(OUTPUT_CSV, rezultate)
    total_pasi = sum(pasi for _, pasi, _, _, _ in rezultate)
    print(f"Am scris rezultatele în: {OUTPUT_CSV}")
    print(f"\nSuma totală a pașilor: {total_pasi}")

if __name__ == "__main__":
    main()
