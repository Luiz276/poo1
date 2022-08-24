irregulares = []
lista = []
resultados = []
l ,n = map(int, input().split())

for x in range(l):
    entrada1, entrada2 = input().split()
    irregulares.append(entrada1)
    irregulares.append(entrada2)

for x in range(n):
    entrada = input()
    if entrada in irregulares:
        print(irregulares[irregulares.index(entrada)+1])
        continue
    entrada = list(entrada)
    if ((entrada[-2] in "bcdfghjklmnpqrstvwxyz") and (entrada[-1] == 'y')):
        del entrada[-1]
        entrada.append("ies")
    elif entrada[len(entrada)-1] == ('o' or 's' or 'x'):
        entrada.append("es")
    elif (entrada[len(entrada)-1] == 'h') and (entrada[len(entrada)-2] == ('c' or 's')):
        entrada.append("es")
    else:
        entrada.append('s')
    print(*entrada, sep = "")