n, m = map(int, input().split())
lista = [None] * n
j = 0#número de jogadores que marcaram em todas as partidas
for x in range(n):
    lista[x] = list(map(int, input().strip().split()))
    if min(lista[x]) != 0:
        j += 1

print(j)