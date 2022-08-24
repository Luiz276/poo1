n = input().split()
n = [int(x) for x in n]
while n[0] != 0 and n[1] != 0:
    copias = []
    res = []
    bilhetes = input().split()
    bilhetes = [int(x) for x in bilhetes]
    for y in bilhetes:
        if bilhetes.count(y) > 1:
            copias.append(y)
    for a in copias:
        if a not in res:
            res.append(a)
    print(len(res))
    n = input().split()
    n = [int(x) for x in n]