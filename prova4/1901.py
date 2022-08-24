#Colocar o conteúdo das células que Bino visitou em uma lista e usar set(lista) para obter a quantidade de espécies borboletas diferentes
n = int(input())

floresta = [None] * n
pos = [None] * 2
esp = []

for x in range(n):
    floresta[x] = list(map(int, input().split()))

for x in range(2*n):
    pos[0], pos[1] = list(map(int, input().split()))
    esp.append(floresta[pos[0]-1][pos[1]-1])

print(len(set(esp)))