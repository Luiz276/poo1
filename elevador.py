n, c = map(int, input().split())
t = 0
count = 0
for x in range(0, n):
    s, e = map(int, input().split())
    t = t-s
    t = t+e
    if t>c:
        count = 1
if count == 1:
    print("S")
else:
    print("N")