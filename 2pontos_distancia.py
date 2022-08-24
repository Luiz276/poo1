A = input()
B = input()
#de novo, fazendo desse jeito por causa do sistema do professor
x1, y1 = A.split()
x2, y2 = B.split()

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

dist = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)

print(f"{dist:.4f}")