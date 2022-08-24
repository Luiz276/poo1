#basta checar o segundo indice da entrada pela letra referente ao gênero e somar a variável correspondente
n = int(input())
f = 0
m = 0
for x in range(n):
    entrada = input().split()
    if entrada[1] == 'M':
        m += 1
    else:
        f += 1
print(f"{m} carrinhos\n{f} bonecas")