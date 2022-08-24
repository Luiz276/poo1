casos = int(input())
n = 0
while n < casos:
    resultado = []
    e1, e2 = map(list, input().split())

    if len(e1)>len(e2):
        x = len(e2)
    else:
        x = len(e1)

    for y in range(x):
        resultado.append(e1[y])
        resultado.append(e2[y])

    if len(e1)>len(e2):
        for y in range(len(e2), len(e1)):
            resultado.append(e1[y])
    elif len(e2)>len(e1):
        for y in range(len(e1), len(e2)):
            resultado.append(e2[y])

    print(*resultado, sep = "")
    n+=1