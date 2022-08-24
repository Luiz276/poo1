#Utilizando os dados ja conhecidos, é calculada a idade do terceiro filho
#Com as idades dos filhos em mãos, basta comprar os 3 inteiros e imprimir o maior
m = int(input())
a = int(input())
b = int(input())

c = m - (a + b)

mais_velho = 0

if a==c:
    if a>b:
        mais_velho = a
    else:
        mais_velho = b
elif b==c:
    if b>a:
        mais_velho = b
    else:
        mais_velho = a
elif a>b and a>c:
    mais_velho = a
elif b>a and b>c:
    mais_velho = b
elif c>a and c>b:
    mais_velho = c

print(mais_velho)