x, y = map(int, input().split())
l1, h1 = map(int, input().split())
l2, h2 = map(int, input().split())

rh = 3
hl = 3
rl = 3

#checando y
if (h1+h2)<=y:
    rh = 1
    hl = 0
elif (h1+l2)<=y:
    rh = 1
    hl = 1
elif (l1+h2)<=y:
    rh = 1
    hl = 2

#checando x
if hl == 0:
    if l1<=x and l2<=x:
        rl = 1
if hl == 1:
    if l1<=x and h2<=x:
        rl = 1
if hl == 2:
    if h1<=x and l2<=x:
        rl = 1

#resultado final
if rl==rh:
    print("S")
else:
    print("N")