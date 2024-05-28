def nummerda(korrused, kortereid_korrustel):
    vastus = []
    for korrus in range(1, korrused + 1):
        korruste_jada = []
        for korter in range(1, kortereid_korrustel + 1):
            korruste_jada.append(f"{korrus}{korter}")
        vastus.append(korruste_jada)
    return vastus
