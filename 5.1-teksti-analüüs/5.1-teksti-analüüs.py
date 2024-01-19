# Olin sellega varem tegelenud sellepärast suutsin nii kiiresti lahenduse leida

def symbolite_sagedus(sõnad: str):
    symbolite_kogus = {}
    for symbol in sõnad:
        if symbol in symbolite_kogus:
            symbolite_kogus[symbol] += 1
        else:
            symbolite_kogus[symbol] = 1
    return symbolite_kogus

print(symbolite_sagedus("l@htek00d"))
