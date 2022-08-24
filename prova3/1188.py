#Basta criar dois for loop que iterem entre as coordenadas desejadas da matriz, onde x itera de 11 a 7
#e y itera entre um intervalo decrescente de acordo com cada novo valor de x
mat = [None] * 12
for x in range(12):
    mat[x] = [None] * 12

op = input()

for x in range(12):
    for y in range(12):
        mat[x][y] = float(input())
a=0
soma = [0]
for x in range(11,6, -1):
    for y in range(1+a, 11-a):
        #print(x, y)
        soma.append(mat[x][y])
    a+=1

if op == 'S':
    print(f"{sum(soma):.1f}")
else:
    print(f"{(sum(soma) / 30):.1f}")