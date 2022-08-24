#coletar input da lista de cartas e do numero de casos de teste, usando uma série de estruturas de decisão para calcular os pontos
n = int(input())
for x in range(n):
    cartas = list(map(int, input().strip().split()))
    cartas.sort()
    
    if (cartas[0]+4) == (cartas[1]+3) == (cartas[2]+2) == (cartas[3]+1) == (cartas[4]):
        pontos = cartas[0] + 200
        #print(1)
    elif ((cartas[0] == cartas[1] and cartas[1] == cartas[2] and cartas[2] == cartas[3]) and (cartas[0] != cartas[4])) or ((cartas[1] == cartas[2] and cartas[2] == cartas[3] and cartas[3] == cartas[4]) and cartas[1]!= cartas[0]):
        pontos = cartas[1] + 180
        #print(2)
    elif cartas[0] != cartas[1] != cartas[2] != cartas[3] != cartas[4]:
        pontos = 0
        #print(3)
    elif (cartas[0] == cartas[1] == cartas[2]):
        if (cartas[3] == cartas[4]):
            pontos = cartas[0] + 160
            #print(4)
        else:
            pontos = cartas[0] + 140
            #print(5)
    elif (cartas[2] == cartas[3] == cartas[4]):
        if (cartas[0] == cartas[1]):
            pontos = cartas[2] + 160
            #print(6)
        else:
            pontos = cartas[2] + 140
            #print(7)
    elif cartas[1] == cartas[2] == cartas[3]:
            pontos = cartas[2] + 140
            #print(16)
    elif cartas[0] == cartas[1]:
        if cartas[2] == cartas[3] or cartas[3] == cartas[4]:
            pontos = 3 * cartas[3] + 2 * cartas[0] + 20
            #print(8)
        else:
            pontos = cartas[0]
            #print(9)
    elif cartas[1] == cartas[2]:
        if cartas[3] == cartas[4]:
            pontos = 3 * cartas[3] + 2 * cartas[1] + 20
            #print(10)
        else:
            pontos = cartas[1]
            #print(11)
    elif cartas[2] == cartas[3]:
        if cartas[0] == cartas[1]:
            pontos = 3 * cartas[2] + 2*cartas[0] + 20
            #print(12)
        else:
            pontos = cartas[2]
            #print(13)
    elif cartas[3] == cartas[4]:
        if cartas[0] == cartas[1] or cartas[1] == cartas[2]:
            pontos = 3*cartas[3] + 2*cartas[1] + 20
            #print(14)
        else:
            pontos = cartas[3]
            #print(15)
    print(f"Teste {x+1}\n{pontos}", end = "\n")