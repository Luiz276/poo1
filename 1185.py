letra = input()
soma = []
mat = [None] * 12
for x in range(len(mat)):
    mat[x] = [None] * 12

for x in range(12):
    for y in range(12):
        mat[x][y] = float(input())

for x in range(len(mat)):
    y = len(mat)-2-x
    while y >= 0:
        soma.append(mat[x][y])
        y -= 1

if letra == 'S':
    print(f"{sum(soma):.1f}")
else:
    print(f"{(sum(soma) / len(soma)):.1f}")