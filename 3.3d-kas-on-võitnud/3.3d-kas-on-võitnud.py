def voitis_nurkademangu(tabel):
    return (tabel[0][0] == 'X' and
            tabel[0][4] == 'X' and
            tabel[4][0] == 'X' and
            tabel[4][4] == 'X')

def x_peadiagonaalil(tabel):
    return sum(1 for i in range(5) if tabel[i][i] == 'X')

def x_korvaldiagonaalil(tabel):
    return sum(1 for i in range(5) if tabel[i][4-i] == 'X')

def voitis_diagonaalidemangu(tabel):
    return x_peadiagonaalil(tabel) == 5 and x_korvaldiagonaalil(tabel) == 5

def voitis_taismangu(tabel):
    for rida in tabel:
        for lahter in rida:
            if lahter != 'X':
                return False
    return True

