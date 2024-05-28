def arvuta_protsendi_muutused(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as fail:
        read = fail.readlines()

    tulemused = [f"{osad[0]} - {int(osad[-1]) - int(osad[1])}%" 
                 for rida in read 
                 if (osad := rida.strip().split()) 
                 and (int(osad[-1]) - int(osad[1])) > 10]

    return tulemused

def peamine():
    failinimi = input("Sisestage failinimi: ")
    muutused = arvuta_protsendi_muutused(failinimi)

    for muutus in muutused:
        print(muutus)

if __name__ == "__main__":
    peamine()

