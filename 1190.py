op = input()

mat = [None] * 12
for x in range(12):
    mat[x] = [None] * 12

for x in range(12):
    for y in range(12):
        mat[x][y] = float(input())

lista= []

a=0
for y in range(11,6,-1):
    for x in range(1+a,11-a):
        lista.append(mat[x][y])
    a+=1

soma = sum(lista)

if op == 'S':
    print(f"{soma:.1f}")
else:
    print(f"{soma/len(lista):.1f}")