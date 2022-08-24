#Basta dividir o numero de galhos por 2 e realizar a diferença entre os galhos que amelia quer com bolinhas e quantas bolinhas ela possui
b = int(input())
g = int(input())

g = int(g/2)
x = g - b

if x<=0:
    print("Amelia tem todas bolinhas!")
else:
    print(f"Faltam {x} bolinha(s)")