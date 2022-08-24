n = int(input())
q=0
for x in range (0, n):
    l, c = input(). split()
    l = int(l)
    c = int(c)
    if l>c:
        q += c
print(q)