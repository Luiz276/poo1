n = int(input())
lista = input().split()
lista = [int(x) for x in lista]
yes = lista.count(0)
no = lista.count(1)
if no >= yes:
    print("N")
else:
    print("Y")