def keskmised(l):
    aine_keskmine = []

    for sl in l:
        a_k = []
        keskmine_l = []
        
        for i in sl:
            if isinstance(i, str):
                a_k.append(i)
            else:
                keskmine_l.append(i)
        
        if keskmine_l:
            keskmine = round(sum(keskmine_l) / len(keskmine_l), 1)
            a_k.append(keskmine)
        
        aine_keskmine.append(a_k)

    return aine_keskmine
