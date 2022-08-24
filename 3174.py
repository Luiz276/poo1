#Somar quantidades de horas a uma variavel para cada trabalho
#No final, dividir essa variavel pela quantia de horas que cada trabalho toma, considerando apenas a parte inteira do resultado.
#Somar resultados individuais para obter total de presentes

bnc = 0
arq = 0
mus = 0
des = 0

presentes = 0

n = int(input())

for _ in range(n):
    nome, area, hrs = input().split()

    if area == "bonecos":
        bnc += int(hrs)
    elif area == "arquitetos":
        arq += int(hrs)
    elif area == "musicos":
        mus += int(hrs)
    else:
        des += int(hrs)

presentes = int(bnc/8) + int(arq/4) + int(mus/6) + int(des/12)

print(presentes)