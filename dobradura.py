#o D = 4 pedaços
#1 D = 9 pedaços
#2 D = 21 pedaços
resultados = []
i = 1
while True:
    w = 0
    n = int(input())
    if n == -1:
        break
    w = ((2**n) + 1)**2
    resultados.append(f"Teste {i}\n{int(w)}\n")
    i += 1
print(*resultados, sep = "\n")