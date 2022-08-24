#Basta somar os exércitos do lado do bem e do lado do mal, realizando uma comparação entre eles para decidir o vencedor
#Caso o lado do bem seja maior ou igual ao lado do mal, a Terra Média está a salvo, porém caso o lado do mal seja superior, Sauron terá retornado
h, e, a, o, w, x = map(int, input().split())

lado_bem = h + e + a + x
lado_mal = o + w

if lado_bem >= lado_mal:
    print("Middle-earth is safe.")
else:
    print("Sauron has returned.")