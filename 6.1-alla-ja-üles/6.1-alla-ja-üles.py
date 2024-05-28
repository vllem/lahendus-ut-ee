def alla_ules(n):
    if n < 0:
        return

    if n == 0:
        print("Põhi!")
        return
    
    if n % 2 == 1:
        print(n)
        if n - 2 > 0:
            alla_ules(n - 2)
        else:
            print("Põhi!")
        print(0 if n == 1 else n - 1)
    else:
        print(n)
        if n - 2 > 0:
            alla_ules(n - 2)
        else:
            print("Põhi!")
        if n - 1 > 0:
            print(n - 1)

