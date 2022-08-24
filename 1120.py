while True:
    dig, num = input().split()
    dig = int(dig)
    num = list(num)
    num = [int(x) for x in num]

    #checar para ver se chegou ao final da input
    if dig == num[0] == 0:
        break

    #checar se o numero a ser retirado esta dentro da lista
    if dig in num:
        while dig in num:
            num.remove(dig)
    
    #printar os resultados
    if not num:
        print(0)
    else:
        if max(num) == 0:
            print(0)
        else:
            num = [str(x) for x in num]
            num = "".join(num)
            num = int(num)
            print(num)