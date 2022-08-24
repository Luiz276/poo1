resultados = []
t = int(input())
i = 0
while t!= 0:
    i+=1
    resultados.append(f"Teste {i}")
    r = 0
    for x in range(0,t):
        x, y = input().split()
        x = int(x)
        y = int(y)
        r = x-y+r
        resultados.append(f"{int(r)}")
    t = int(input())
    resultados.append(" ")
resultados.append(" ")
print(*resultados, sep = "\n")