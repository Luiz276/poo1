n = int(input())
hexadecimal = input().split()
resultados = []
for x in range (0, n):
    resultados.append(bytes.fromhex(hexadecimal[x]).decode("ASCII"))
print(*resultados, sep = '')