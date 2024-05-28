import csv

def loe_andmed_failist(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as fail:
        reader = csv.reader(fail, delimiter=';')
        andmed = [rida for rida in reader]
    return andmed

def leia_suurima_osalejate_arvuga_maakond(andmed):
    suurim_maakond, suurim_osalejate_arv = max(
        ((rida[0], sum(map(int, rida[1:]))) for rida in andmed),
        key=lambda x: x[1]
    )
    return suurim_maakond, suurim_osalejate_arv

def leia_kogu_osalejate_summa(andmed):
    kogu_osalejate_summa = sum(
        sum(map(int, rida[1:])) for rida in andmed
    )
    return kogu_osalejate_summa

def main():
    failinimi = "maalähedane.csv"
    andmed = loe_andmed_failist(failinimi)

    suurim_maakond, suurim_osalejate_arv = leia_suurima_osalejate_arvuga_maakond(andmed)
    kogu_osalejate_summa = leia_kogu_osalejate_summa(andmed)

    print(f"Kõige rohkem osalejaid - {suurim_maakond}, {suurim_osalejate_arv} inimest.")
    print(f"Kokku on kursusel osalenud {kogu_osalejate_summa} inimest.")

if __name__ == "__main__":
    main()

