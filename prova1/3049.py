#Calcular a área dos dois pedaços de papel resultantes do corte e comparar
b = int(input())
t = int(input())
a_total = 70*160
count = 0

q = t - b

a_esq_quadrado = b * 70
a_esq_tri = (q*70)/2

a_esq = a_esq_tri + a_esq_quadrado
a_dir = a_total - a_esq

if a_esq == a_dir:
    count = 0
elif a_esq > a_dir:
    count = 1
else:
    count = 2
print(count)