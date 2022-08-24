n = int(input())
while n != 0:
    lista = input().split()
    lista = [int(x) for x in lista]
    suspeitos = [int(x) for x in lista]
    suspeitos.sort(reverse = True)
    culpado = lista.index(suspeitos[1])
    culpado += 1
    print(culpado)
    lista = []
    suspeitos = []
    n = int(input())