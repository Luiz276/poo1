tam = int(input())
while tam > 0:
    mat = [[1 for x in range(tam)] for y in range(tam)]

    for a in range(int(tam/2)):
        for x in range(a+1,tam-1-a):
            for y in range(a+1,tam-1-a):
                mat[x][y]+=1

    for x in range(tam):
        for y in range(tam):
            mat[x][y] = str(mat[x][y]).rjust(3)

    for x in range(tam):
        print(*mat[x], sep = " ")
    print("")
    tam = int(input())