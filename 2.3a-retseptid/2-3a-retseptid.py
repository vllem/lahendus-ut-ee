fail = open("retseptid.txt", encoding="UTF-8")

retseptid_tabel = [] # Tühi järjend, kuhu lisame retseptid

for rida in fail:    # Iga rea jaoks failist
    koostisosad = []     # Kogume reas olevad koostisosad järjendisse
    osad = rida.split(",") # Jupitame rea koma koha pealt

    for osa in osad: # Vaatame iga juppi eraldi
        koostisosad.append(osa.strip()) # Lisame reas olevad koostisosad järjendisse

    retseptid_tabel.append(koostisosad) # Lisame koostisosade järjendi retseptide tabelisse

fail.close()

leitud_retseptid = list(filter(lambda x: all(koostisosa in x for koostisosa in ["suhkur", "maasikad"]), retseptid_tabel))

for leitud in leitud_retseptid:
    print(leitud)
