a, b, c = input().split()
x, y, z = input().split()

x = int(x)
y = int(y)
z = int(z)
a = int(a)
b = int(b)
c = int(c)

hx = x / a
hy = y / b
hz = z / c

hx = int(hx)
hy = int(hy)
hz = int(hz)

qch = hx * hy * hz

print(qch)