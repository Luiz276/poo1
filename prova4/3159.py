#Criar um dicionario com cada letra e as respectivas teclas
#Se a letra for maiúscula, adionar um # e convertêla para minúscula
#Caso ela não seja maiúscula, checar se a letra antecedente a ela usa a mesma tecla

teclado = {
    'a' : 2,
    'b' : 22,
    'c' : 222,
    'd' : 3,
    'e' : 33,
    'f' : 333,
    'g' : 4,
    'h' : 44,
    'i' : 444,
    'j' : 5,
    'k' : 55,
    'l' : 555,
    'm' : 6,
    'n' : 66,
    'o' : 666,
    'p' : 7,
    'q' : 77,
    'r' : 777,
    's' : 7777,
    't' : 8,
    'u' : 88,
    'v' : 888,
    'w' : 9,
    'x' : 99,
    'y' : 999,
    'z' : 9999,
    ' ' : 0
    }

n = int(input())

for _ in range(n):
    pal = list(input())
    res = []

    for num in range(len(pal)):

        if pal[num].isupper() == 1:
            res.append("#")
            pal[num] = pal[num].lower()
        
        else:
            if num>0:
                #Checar se o antecedente usa a mesma tecla
                tecla_1 = list(str(teclado[pal[num]]))
                tecla_2 = list(str(teclado[pal[num-1]]))

                if tecla_1[0] == tecla_2[0]:
                    res.append("*")
        
        res.append(teclado[pal[num]])
    
    print(*res, sep = "")