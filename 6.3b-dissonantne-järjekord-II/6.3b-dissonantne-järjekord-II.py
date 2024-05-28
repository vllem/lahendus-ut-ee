def on_rahulik(arvamus1, arvamus2, erinevus):
    if arvamus1 == 0 or arvamus2 == 0:
        return True
    if arvamus1 * arvamus2 > 0 or abs(arvamus1 - arvamus2) <= erinevus:
        return True
    return False

def dissonandid(arvamused, lubatud_erinevus):
    erilased = []

    for i in range(len(arvamused) - 1):
        if not on_rahulik(arvamused[i], arvamused[i+1], lubatud_erinevus):
            erilased.append((i, i+1))

    return erilased

