a, b, c = input().split()
h, l = input().split()

z = int(a)
x = int(b)
y = int(c)
h = int(h)
l = int(l)

dPorta = ((h**2)+(l**2))**(1/2)

xTotal = z + x

if dPorta>=xTotal:
    print("S")
else:
    print("N")