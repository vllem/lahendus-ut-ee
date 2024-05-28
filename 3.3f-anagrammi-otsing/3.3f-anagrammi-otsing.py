def leidub_anagramm(maatriks):
    return any(sorted(maatriks[i][j]) == sorted((maatriks[i][j-1] if j > 0 else "") + (maatriks[i][j+1] if j < len(maatriks[i]) - 1 else "")) for i in range(len(maatriks)) for j in range(len(maatriks[i])))

