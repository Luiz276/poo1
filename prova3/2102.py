#Basta coletar as inputs e somar os valores dados as coordenadas pedidas, printando valores diferentes de zero ao final
t = int(input())

for a in range(t):
    n, i = map(int, input().split())

    maiorl = 0
    maiorc = 0
    #inicializando a matriz:
    mat = [0] * 100
    for x in range(100):
        mat[x] = [0]*100
    
    #coletando input de p,l,c,v e atribuindo valores a matriz:
    for b in range(i):
        p,l,c,v = map(int, input().split())

        if l > maiorl:
            maiorl = l
        if c > maiorc:
            maiorc = c
        
        mat[l][c] += v
    
    #printando valores diferentes de zero presentes na matriz:
    for x in range(maiorl+1):
        for y in range(maiorc+1):
            if mat[x][y] != 0:
                print(x, y, mat[x][y])
    
    #linha em branco ao final do caso de teste:
    if a!=t-1:
        print("")