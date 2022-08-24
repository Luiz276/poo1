#usar itertools.combinations para gerar os pares e um if para verificar se satisfazem as condições propostas
from itertools import combinations

n, i, f = map(int, input().split())
seq = list(map(int, input().strip().split()))
count = 0

for combination in combinations(seq, 2):
    if (combination[0] + combination[1] <= f) and (combination[0] + combination[1] >= i):
        count += 1
print(count)