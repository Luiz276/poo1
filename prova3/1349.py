#cada vez que a matriz do scan for girada, basta calcular a porcentagem novamente
#((img[x][y]-100) < scan[x][y]) and ((img[x][y]+100) > scan[x][y])
l = int(input())
while l != 0:
    img = [0]*l
    scan = [0]*l
    scan_e = [0]*l
    porc = [0] * 8
    for x in range(l):
        img[x] = list(map(int, input().strip().split()))

    for x in range(l):
        scan[x] = list(map(int, input().strip().split()))

    #Girando a matriz 4 vezes:
    for a in range(4):
        total = 0

        #list(map(list, zip(*matrix[::-1]))
        #esta linha de código gira uma matriz em 90 graus
        scan = list(map(list, zip(*scan[::-1])))

        for x in range(l):
            for y in range(l):
                if 0 <= abs(scan[x][y]-img[x][y]) <= 100:
                    total += 1

        porc[a] = ((total*100)/(l**2))
    
    #espelhando a matriz:
    for a in range(l):
        scan[a].reverse()

    #girando a matriz espelhada 4 vezes
    for a in range(4):
        total = 0

        #list(map(list, zip(*matrix[::-1]))
        #esta linha de código gira uma matriz em 90 graus
        scan = list(map(list, zip(*scan[::-1])))

        for x in range(l):
            for y in range(l):
                if 0 <= abs(scan[x][y]-img[x][y]) <= 100:
                    total += 1

        porc[a+4] = ((total*100)/(l**2))
    
    print(f"{round(max(porc), 2):.2f}")
    
    l = int(input())