fail = open("kalorid.txt", encoding="UTF-8")

toitude_tabel = []

for rida in fail: # iga rea jaoks failist
    korra_grammid = [] # kogume ühe toidukorra info
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        korra_grammid.append(int(osa)) # järjekordne info juurde

    toitude_tabel.append(korra_grammid) # toidukorra järjend juurde

fail.close()


def kalorsus_loomine():
    k6ik = []
    l6pp = 0
    for toidud in toitude_tabel:
        yks = (toidud[0] + toidud[1])*4 + toidud[2]*9
        k6ik.append(yks)
    for yks in k6ik:
        l6pp += yks
    print(l6pp)


kalorsus_loomine()
