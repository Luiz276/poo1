t = int(input())
dicionario = {}
for _ in range(t):
    dicionario.clear()
    resposta = []
    m, n = map(int, input().split())

    for y in range(m):
        chave = input()
        valor = input()

        dicionario[chave] = valor
    
    for w in range(n):
        linha = input().split()
        resposta.clear()
        for x in range(len(linha)):
            if linha[x] in dicionario:
                resposta.append(dicionario[linha[x]])
            else:
                resposta.append(linha[x])
        
        print(*resposta, sep = " ")
    print("")