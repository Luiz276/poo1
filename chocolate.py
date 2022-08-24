l = int(input())
q = 1
while True:
    if l>=2:
        l = l/2
        q = q*4
    else:
        break
print(q)