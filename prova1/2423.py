#Obter as razoes entre os ingredientes disponiveis e os ingredientes da receita e checar qual a menor razao, este é o numero de bolos que se consegue fazer
a, b, c = map(int, input().split())

r1 = int(a/2)
r2 = int(b/3)
r3 = int(c/5)

if r1==r2 and r2==r3:
    qt = r1
elif r1==r2:
    if r1<r3:
        qt = r1
    else:
        qt = r3
elif r3==r2:
    if r2<r1:
        qt = r2
    else:
        qt = r1
elif r1==r3:
    if r1<r2:
        qt = r1
    else:
        qt = r2
elif r1<r2 and r1<r3:
    qt = r1
elif r2<r1 and r2<r3:
    qt = r2
elif r3<r1 and r3<r2:
    qt = r3
print(qt)