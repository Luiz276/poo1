letra = input()
soma = []
mat = [None] * 12
for x in range(len(mat)):
    mat[x] = [None] * 12

for x in range(12):
    for y in range(12):
        mat[x][y] = float(input())

for x in range(1,12):
    n = 0
    while n < x:
        soma.append(mat[x][n])
        n+=1

if letra == 'S':
    print(f"{sum(soma):.1f}")
else:
    print(f"{(sum(soma) / len(soma)):.1f}")