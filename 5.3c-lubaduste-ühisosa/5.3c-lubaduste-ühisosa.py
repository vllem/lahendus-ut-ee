def kooslubajad(parteid):
    maksimaalne_lubaduste_yhisosa = 0
    parim_paar = None

    for i in range(len(parteid)):
        for j in range(i + 1, len(parteid)):
            yhisosa_suurus = len(parteid[i].intersection(parteid[j]))
            if parim_paar is None or yhisosa_suurus > maksimaalne_lubaduste_yhisosa:
                maksimaalne_lubaduste_yhisosa = yhisosa_suurus
                parim_paar = (i, j)

    return parim_paar if parim_paar is not None else (0, 1) if len(parteid) > 1 else None
