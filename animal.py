a = input()
b = input()
c = input()

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    else:
        if c == 'herbivoro':
            print("vaca")
        else:
            print("homem")
else:
    if b == 'inseto':
        if c == 'hematofago':
            print("pulga")
        else:
            print("lagarta")
    else:
        if c == 'onivoro':
            print("minhoca")
        else:
            print("sanguessuga")