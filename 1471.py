while True:
    try:
        resultados = []
        i = 1
        count = 1
        n, r = map(int, input().split())
        lista = input().split()
        lista = [int(x) for x in lista]
        lista.sort()

        if (n == r):
            print("* ")
            continue
    
        while (i <= n):
            resultados.append(i)
            i += 1
    
        l3 = [x for x in resultados if x not in lista] #Usando list comprehension para retirar os elementos de lista presentes em resultados
        #l3.append(" ")
        print(*l3," ")
    except EOFError:
        break