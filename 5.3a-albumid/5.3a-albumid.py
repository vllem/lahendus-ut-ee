def sorteeri(failinimi):
    albumid_sonastik = {}
    with open(failinimi, 'r', encoding='utf-8') as fail:
        for rida in fail:
            osad = rida.strip().split(';')
            esitaja, albumi_nimi, aasta, koopiad = osad[0], osad[1], osad[2], osad[3]
            aastakümme = (int(aasta) // 10) * 10
            if aastakümme not in albumid_sonastik:
                albumid_sonastik[aastakümme] = []
            albumid_sonastik[aastakümme].append([esitaja, albumi_nimi, aasta, koopiad])
    return albumid_sonastik

def kuva(albumid_sonastik):
    for aastakümme in sorted(albumid_sonastik):
        albumid = albumid_sonastik[aastakümme]
        albumite_arv = len(albumid)
        enim_muunud_album = max(albumid, key=lambda x: int(x[3]))
        esitaja, albumi_nimi = enim_muunud_album[0], enim_muunud_album[1]
        print(f"{aastakümme}: {albumite_arv} album(it) ({esitaja} - {albumi_nimi})")

def main():
    failinimi = "albumid.txt"
    albumid_sonastik = sorteeri(failinimi)
    kuva(albumid_sonastik)

if __name__ == "__main__":
    main()

