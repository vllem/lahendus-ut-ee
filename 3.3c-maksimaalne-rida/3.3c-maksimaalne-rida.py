def leia_max_summa_rida(faili_nimi):
    try:
        with open(faili_nimi, 'r') as fail:
            max_summa = None
            max_rida_number = 0
            praegune_rida_number = 0
            
            for rida in fail:
                praegune_rida_number += 1
                numbrid = list(map(int, rida.split()))
                rea_summa = sum(numbrid)
                
                if max_summa is None or rea_summa > max_summa:
                    max_summa = rea_summa
                    max_rida_number = praegune_rida_number
            
            if max_summa is not None:
                print(f"Suurim summa on failis {max_rida_number}. real ja see on {max_summa}.")
            else:
                print("Fail on tühi või ei sisalda ühtegi rea numbrit.")
    
    except FileNotFoundError:
        print(f"Faili nimega {faili_nimi} ei leitud.")
    except Exception as e:
        print(f"Ilmnes viga: {e}")

if __name__ == "__main__":
    faili_nimi = input("Sisestage failinimi: ")
    leia_max_summa_rida(faili_nimi)

