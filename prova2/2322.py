#basta usar sort() para organizar a entrada das peças presentes e checar para ver qual a peça(número) que falta na sequência
n = int(input())
p = input().split()

#convertendo numeros para int
for x in range(len(p)):
    p[x] = int(p[x])

#usando sort() para organizar os números em ordem crescente
p.sort()

#iniciando os testes
if p[0] != 1:
    print(1)
elif p[n-2] != n:
    print(n)
else:
    for x in range(len(p)):
        if x+1 == n-1:
            break
        elif (p[x+1] - p[x]) != 1:
            print(p[x]+1)