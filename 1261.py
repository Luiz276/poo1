m,n = map(int, input().split())

hay = {}
for _ in range(m):
    chave, valor = input().split()
    hay[chave] = int(valor)

for _ in range(n):
    soma = 0

    while True:
        texto = input().split()
        if texto[len(texto)-1] == ".":
            break
    
    #continuar
                    
    print(soma)