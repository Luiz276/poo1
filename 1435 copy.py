tam = int(input())
while tam > 0:
    mat = [1] * tam
    for x in range(len(mat)):
        mat[x] = [1] * tam

    for x in range(1,len(mat)-1):
        print(x)

    for x in range(len(mat)):
        print(*mat[x], sep = "   ")
    print("")
    tam = int(input())