#Ir somando os numeros da lista de input
#Caso a soma seja menor que 0, resetar a soma a 0
#Caso a soma atual seja maior que a maior soma registrada, atribuir soma a maior soma
n = int(input())
lista = list(map(int, input().strip().split()))
soma = 0
maior_soma = 0

for x in lista:
    soma += x
    if soma < 0:
        soma = 0
    elif soma > maior_soma:
        maior_soma = soma

print(maior_soma)