plugue = input().split()
soquete = input().split()
res = []
for i in range(0, 5):
    if plugue[i] == '1' and soquete[i] == '0':
        res.append(1)
    elif plugue[i] == '0' and soquete[i] == '1':
        res.append(1)
    else:
        res.append(0)
prova = all(elem == 1 for elem in res)
if prova:
    print("Y")
else:
    print("N")