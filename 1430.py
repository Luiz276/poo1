length = {
    'W':(1),
    'H':(1/2),
    'Q':(1/4),
    'E':(1/8),
    'S':(1/16),
    'T':(1/32),
    'X':(1/64),
}

while True:
    acerto = 0
    comp = input()

    if comp == '*':
        break

    comp = comp.strip('/').split('/')

    for element in comp:
        soma = 0
        for letra in element:
            soma += length[letra]
        if soma == 1:
            acerto += 1
    
    print(acerto)