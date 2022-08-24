#Basta dividir o valor pelo numero de parcelas, e caso a divisão apresente resto é só somar 1 as parcelas iniciais até fechar o valor do produto
v = int(input())
p = int(input())
pcheck = 0
count = v%p

while pcheck != p:
    parcela = int(v/p)
    if count>0:
        parcela = parcela + 1
        count -= 1
    print(parcela)
    pcheck += 1