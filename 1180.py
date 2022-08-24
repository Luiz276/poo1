n = int(input())
lista = input().split()
lista = [int(x) for x in lista]
val = min(lista)
pos = lista.index(val)
print(f"Menor valor: {val}\nPosicao: {pos}")