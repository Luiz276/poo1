#Basta contar quantos números não estão repetidos na lista e printar o total ao final
#Para tal, uso set() para converter uma lista com todos os numeros em uma apenas sem os números repetidos
n = int(input())

lista = [None]*n

for x in range(n):
    lista[x] = int(input())

print(len(set(lista)))