q = int(input())
lista = list(map(int, input().strip().split()))

n = 2#número pelo qual as divisões ocorrem

#criando a matriz que contém os resultados
mat = [None] * 4
for x in range(4):
    mat[x] = [None] * q

for x in range(4):
    for y in range(q):
        if lista[y] % n == 0:
            mat[x][y] = 1
        else:
            mat[x][y] = 0
    print(f"{sum(mat[x])} Multiplo(s) de {n}")
    n+=1#incrementando o número pelo qual as divisões ocorrem