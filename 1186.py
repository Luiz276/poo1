letra = input()
soma = []
mat = [None] * 12
for x in range(len(mat)):
    mat[x] = [None] * 12

for x in range(len(mat)):
    for y in range(len(mat)):
        mat[x][y] = float(input())

for x in range(len(mat)):
    for y in range(len(mat)-1, (len(mat)-1)-x, -1):
        soma.append(mat[x][y])

if letra == 'S':
    print(f"{sum(soma):.1f}")
else:
    print(f"{(sum(soma) / len(soma)):.1f}")