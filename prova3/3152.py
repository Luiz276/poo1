#Usa-se a fórmula da área de Gauss, também conhecida como "shoelace formula"
va = [None] * 4
vb = [None] * 4

for x in range(4):
    va[x] = list(map(int, input().strip().split()))

for x in range(4):
    vb[x] = list(map(int, input().strip().split()))

#Calculando terreno A:
#aplicação da 1° parte da fórmula:
d1 = (va[0][0]*va[1][1])+(va[1][0]*va[2][1])+(va[2][0]*va[3][1])+(va[3][0]*va[0][1])
d2 = (va[0][1]*va[1][0])+(va[1][1]*va[2][0])+(va[2][1]*va[3][0])+(va[3][1]*va[0][0])

#obtenção do resultado:
da = (1/2)*abs(d1-d2)

#Calculando terreno B:
#aplicação da 1° parte da fórmula:
d1 = (vb[0][0]*vb[1][1])+(vb[1][0]*vb[2][1])+(vb[2][0]*vb[3][1])+(vb[3][0]*vb[0][1])
d2 = (vb[0][1]*vb[1][0])+(vb[1][1]*vb[2][0])+(vb[2][1]*vb[3][0])+(vb[3][1]*vb[0][0])

#obtenção do resultado:
db = (1/2)*abs(d1-d2)

if db>= da:
    print("terreno B")
else:
    print("terreno A")