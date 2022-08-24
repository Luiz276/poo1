#Colocar todas as palavras do texto como chaves de um dicionário, com seus comprimentos como valores
#Caso uma palavra no texto corresponde com a plavara buscada, basta adicionar o comprimento de todas as palavras anteriores a ela e o numero de espacos entre elas para obter a posicao
n = int(input())

for number in range(n):
    texto = input().split()
    plv = input()

    dict_texto = {}
    count = 0
    res = []

    for element in texto:
        dict_texto[element] = len(element)
    
    for num in range(len(texto)):
        comp = 0
        if texto[num] == plv:
            for x in range(num):
                comp += dict_texto[texto[x]]
            res.append(comp+num)
            count = 1

    if count == 0:
        print(-1)
    else:
        print(*res, sep = " ")