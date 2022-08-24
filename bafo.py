resultados = []
x = int(input())
i=1
while x!=0:
    resultados.append(f"Teste {i}")
    ta = 0
    tb = 0
    for n in range(0, x):
        a, b = map(int, input().split())
        ta += a
        tb += b
    if ta>tb:
        resultados.append("Aldo\n")
    else:
        resultados.append("Beto\n")
    i += 1
    x = int(input())
print(*resultados, sep = "\n")