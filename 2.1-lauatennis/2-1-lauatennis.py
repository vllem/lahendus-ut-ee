fail = open("tulemused.txt", encoding="UTF-8")

tulemuste_tabel = []

for rida in fail: # iga rea jaoks failist
    seti_punktid = [] # kogume ühe seti punkte
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        seti_punktid.append(int(osa)) # järjekordsed punktid juurde

    tulemuste_tabel.append(seti_punktid) # seti punktide järjend juurde
fail.close()


def tulemuste_loomine():
    eesti = 0
    soome = 0
    for tulemused in tulemuste_tabel:
        if abs(tulemused[0] - tulemused[1]) >= 2:
            if tulemused[0] > tulemused[1]:
                eesti += 1
            else:
                soome += 1
            if eesti == 3:
                break
            if soome == 3:
                break
        else:
            continue
    if eesti > soome:
        print(f"Eesti võitis {eesti}-{soome}")
    else:
        print(f"Soome võitis {soome}-{eesti}")


tulemuste_loomine()
