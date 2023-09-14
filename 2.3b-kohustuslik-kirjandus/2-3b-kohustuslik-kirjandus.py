from math import ceil

fail = open("raamatud.txt", encoding="UTF-8")

kirjandus_tabel = [] # Tühi järjend, kuhu lisame raamatud

for rida in fail:    # Iga rea jaoks failist
    raamat = []     # Kogume reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    osad = rida.split(":") # Jupitame rea semikooloni koha pealt

    pealkiri = osad[0].strip() # Eraldame pealkirja
    lehekyljed = int(osad[1].strip()) # Eraldame lehekülgede arvu

    raamat.append(pealkiri) # Lisame reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    raamat.append(lehekyljed)

    kirjandus_tabel.append(raamat) # Lisame raamatute järjendi kirjanduse tabelisse

fail.close()


kui_palju_kokku = 0
print("Raamatud, mille lugemiseks kulub rohkem kui neli päeva:")
for kirjandus in kirjandus_tabel:
    kui_palju_kokku += kirjandus[1]
    kirjandus[1] = ceil(kirjandus[1] / 60)
    if kirjandus[1] <= 4:
        continue
    else:
        raamat = kirjandus[0]
        p2ev = kirjandus[1]
        print(f"{raamat} - {p2ev} päeva")
print(f"Kõigi raamatute lugemiseks kulub {round(kui_palju_kokku / 30, 1)} h")
