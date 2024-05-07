def nurkademanguks_vaja(read: list):
    numbrid = []

    if isinstance(read[0][0], int):
        numbrid.append(read[0][0])

    if isinstance(read[0][4], int):
        numbrid.append(read[0][4])

    if isinstance(read[4][0], int):
        numbrid.append(read[4][0])

    if isinstance(read[4][4], int):
        numbrid.append(read[4][4])

    return numbrid


def diagonaalidemanguks_vaja(read: list):
    numbrid = []

    # esimene rida
    if isinstance(read[0][0], int):
        numbrid.append(read[0][0])

    if isinstance(read[0][4], int):
        numbrid.append(read[0][4])

    # teine rida
    if isinstance(read[1][1], int):
        numbrid.append(read[1][1])

    if isinstance(read[1][3], int):
        numbrid.append(read[1][3])

    # kolmas rida
    if isinstance(read[2][2], int):
        numbrid.append(read[2][2])

    # neljas rida
    if isinstance(read[3][1], int):
        numbrid.append(read[3][1])

    if isinstance(read[3][3], int):
        numbrid.append(read[3][3])

    # viies rida
    if isinstance(read[4][0], int):
        numbrid.append(read[4][0])

    if isinstance(read[4][4], int):
        numbrid.append(read[4][4])

    return numbrid


def taismanguks_vaja(read: list):
    numbrid = []
    for a in range(5):
        for b in range(5):
            if read[a][b] != 'X':
                numbrid.append(read[a][b])
    return numbrid
