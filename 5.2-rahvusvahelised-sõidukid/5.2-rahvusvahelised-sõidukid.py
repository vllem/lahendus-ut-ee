def failist_sonastik(failinimi):
    sonastik = {}
    with open(failinimi, 'r', encoding='utf-8') as fail:
        for rida in fail:
            osad = rida.strip().split(' ', 1)
            tahis, nimi = osad[0], osad[1]
            sonastik[tahis] = nimi
    return sonastik

def tahised_nimedeks(tahised, sonastik):
    nimed = [sonastik.get(tahis, None) for tahis in tahised]
    return nimed

def main():
    failinimi = input("Sisestage andmebaasi failinimi: ")
    sonastik = failist_sonastik(failinimi)

    tahised_sone = input("Sisestage piiri ületanud sõidukite riikide tähised: ")
    tahised = tahised_sone.split()

    nimed = tahised_nimedeks(tahised, sonastik)

    for nimi in nimed:
        if nimi is None:
            print("Tundmatu maa")
        else:
            print(nimi)

if __name__ == "__main__":
    main()

