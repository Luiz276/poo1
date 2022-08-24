while True:
    count = 0
    palavras = input().split()
    if palavras[0] == '*':
        break
    for x in range(0, len(palavras)):
        palavras[x] = palavras[x].upper()
        caracteres = list(palavras[x])
        if x==0:
            primeiraletra = caracteres[0]
        if caracteres[0] != primeiraletra:
            count = 1
    if count == 1:
        print("N")
    else:
        print("Y")