#dividi-se n por m para se obter a razão entre os dois números
#multiplica-se essa razão por y, e caso o resultado seja maior ou igual a x, x pertence ao exército 1
n, m, s = map(int, input().split())

raz = n / m
e1 = 0
e2 = 0

for x in range(s):
    x, y, h = map(int, input().split())
    if (x <= (y * raz)):
        e1 += h
    else:
        e2 += h

print(e1, e2)