#Para obter a solução basta comparar os numeros fornecidos com as regras estabelecidas no enunciado, caso eles atendam os requisitos pedidos imprimir "YES"
a = int(input())
b = int(input())

if a<6 or b<6:
    print("NO")
elif a>=14 and b>=14:
    print("YES")
elif a>=18 or b>=18:
    print("YES")
else:
    print("NO")