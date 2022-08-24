#Somar os valores antecedidos por v e or valores antecedidos por g, comparando-os para decidir qual resultado imprimir
n = int(input())
x=0
verba = 0
gasto = 0
while x<n:
    x+=1
    t, c = input().split()
    c = int(c)
    if t == "V":
        verba += c
    else:
        gasto += c
if verba>gasto:
    print("A greve vai parar.")
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")