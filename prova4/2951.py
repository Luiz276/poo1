#Colocar as runas e seus valores em dicionario
#transformar o texto em uma lista e adicionar o valor de cada runa que compõe a lista ao poder
n, g = map(int, input().split())

runas = {}
for _ in range(n):
    chave, valor = input().split()
    runas[chave] = int(valor)

x = int(input())

texto = list(input().split())

poder = 0

for letra in texto:
    poder += runas[letra]

print(poder)

if poder >= g:
    print("You shall pass!")
else:
    print("My precioooous")