from random import sample


def juhuslik_bingo():
    vahemik = {
        'B': range(1, 16),
        'I': range(16, 31),
        'N': range(31, 46),
        'G': range(46, 61),
        'O': range(61, 76)
    }

    veerg = {key: sample(value, 5) for key, value in vahemik.items()}

    bingo_tabel = []
    for i in range(5):
        rida = [veerg['B'][i], veerg['I'][i], veerg['N'][i], veerg['G'][i], veerg['O'][i]]
        bingo_tabel.append(rida)

    return bingo_tabel
