resultados = []
i = 1
while True:
    v = int(input())
    if v==0:
        break
    n50 = v/50
    v = v%50
    n10 = v/10
    v = v%10
    n5 = v/5
    v = v%5

    resultados.append(f"Teste {int(i)}\n{int(n50)} {int(n10)} {int(n5)} {int(v)}\n")
    i += 1
print(*resultados, sep = "\n")