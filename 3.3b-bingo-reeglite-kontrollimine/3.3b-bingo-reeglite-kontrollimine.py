def on_bingo_tabel(matrix):
    vahed = [
        range(1, 16),
        range(16, 31),
        range(31, 46),
        range(46, 61),
        range(61, 76)
    ]
    
    for veerg in range(5):
        for rida in range(5):
            if matrix[rida][veerg] not in vahed[veerg]:
                return False
    
    return True

