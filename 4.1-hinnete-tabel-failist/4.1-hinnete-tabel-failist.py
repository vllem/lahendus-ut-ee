def keskmine_csv():
    keskmised = []
    with open("hinded.csv", 'r') as fail:
        for rida in fail:
            faili_osad = rida.strip().split(',')
            aine = faili_osad[0]
            hinded = [int(hinne) for hinne in faili_osad[1:]]
            keskmine = round(sum(hinded) / len(hinded), 1)
            keskmised.append((aine, keskmine))
    return keskmised

aine_keskmine = keskmine_csv()
for aine, keskmine in aine_keskmine:
    print(f"{aine}: {keskmine}")

