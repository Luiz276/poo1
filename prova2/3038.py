#identificar quais caracteres são os simbolos especiais e substitui-los pela letra correta. O print dessa questão deu um pouco de trabalho por causa de presentation error
cifra = ['@', 'a', '&', 'e', '!', 'i', '*', 'o', '#', 'u']
simb = "@&!*#"
palavra = []
while True:
    try:
        count = 0
        texto = input().split()
        for x in range(len(texto)):
            if count < len(texto) and count > 0:
                print("", end = " ")
            palavra = list(texto[x])
            for y in range(len(palavra)):
                if palavra[y] in simb:
                    cord = cifra.index(palavra[y])
                    del palavra[y]
                    palavra.insert(y, cifra[cord+1])
            print(*palavra, sep = "", end = "")
            count +=1
        print("")
    except EOFError:
        break