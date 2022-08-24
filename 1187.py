letra = input()
soma = []
mat = [None] * 12
for x in range(len(mat)):
    mat[x] = [None] * 12

for x in range(len(mat)):
    for y in range(len(mat)):
        mat[x][y] = float(input())

for x in range(0,int((len(mat)/2))):
    for y in range(1+x, (len(mat)-1)-x):
        soma.append(mat[x][y])

if letra == 'S':
    print(f"{sum(soma):.1f}")
else:
    print(f"{(sum(soma) / len(soma)):.1f}")