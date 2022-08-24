a, b, c = input().split()
h, l = input().split()

A = int(a)
B = int(b)
C = int(c)
H = int(h)
L = int(l)

if A <= H and B <= L:
    print("S")
elif A <= H and C <= L:
    print("S")
elif B <= H and A <= L:
    print("S")
elif B <= H and C <= L:
    print("S")
elif C <= H and A <= L:
    print("S")
elif C <= H and B <= L:
    print("S")
else:
    print("N")