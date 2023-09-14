def kala_kaal(pikkus: int, tysedusindex: float):
    return round(pow(pikkus, 3) * tysedusindex / 100)


def main():
    sisestatud_fail = input("Sisesta failinimi: ")
    sisestatud_alam66t = int(input("Sisesta püügi alamõõt: "))
    sisestatud_tysedusindeks = float(input("Sisesta Fultoni tüsedusindex: "))
    ok_kalad = []

    try:
        with open(sisestatud_fail, encoding="UTF-8") as fail:
            for rida in fail:
                pikkus = int(rida.strip())
                if pikkus >= sisestatud_alam66t:
                    kaal = kala_kaal(pikkus, sisestatud_tysedusindeks)
                    print(f"Püütud kala kaaluga {kaal} grammi")
                    ok_kalad.append(kaal)
                else:
                    print("Kala lasti vette tagasi")

        if not ok_kalad:
            return 1
        else:
            raskeim_grammides = max(ok_kalad)
            raskeim_kilogrammides = round(raskeim_grammides / 1000, 3)
            print(f"Kõige raskem püütud kala: {raskeim_kilogrammides} kg")

    except FileNotFoundError:
        print(f"Viga: Faili '{sisestatud_fail}' ei leitud.")
    except ValueError:
        print("Viga: Sisend ei ole sobivas formaadis.")


main()
