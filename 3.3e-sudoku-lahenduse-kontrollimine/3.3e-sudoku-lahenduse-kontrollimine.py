def kastid_korras(maatriks):
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
            if sorted(kast) != list(range(1, 10)):
                return False
    return True

def read_korras(maatriks):
    for row in maatriks:
        if sorted(map(int, row)) != list(range(1, 10)):
            return False
    return True

def veerud_korras(maatriks):
    for col in range(9):
        veerg = [int(maatriks[row][col]) for row in range(9)]
        if sorted(veerg) != list(range(1, 10)):
            return False
    return True

def kontrolli_sudoku(failinimi):
    try:
        with open(failinimi, 'r') as fail:
            maatriks = [line.strip().split() for line in fail.readlines()]
        
        if read_korras(maatriks) and veerud_korras(maatriks) and kastid_korras(maatriks):
            print("OK")
        else:
            print("VIGA")
    except FileNotFoundError:
        print(f"Faili nimega {failinimi} ei leitud.")
    except Exception as e:
        print(f"Ilmnes viga: {e}")

if __name__ == "__main__":
    failinimi = input("Sisestage failinimi: ")
    kontrolli_sudoku(failinimi)

