#Comparar a lista da aposta e do sorteio, usando uma variável para registrar a quantidade de números iguais. Tal variável é utilizada para printar a resposta correta
aposta = list(map(int,input().strip().split()))
sorteio = list(map(int,input().strip().split()))
count = 0
for x in aposta:
    if x in sorteio:
        count += 1

if count < 3:
    print("azar")
elif count == 3:
    print("terno")
elif count == 4:
    print("quadra")
elif count == 5:
    print("quina")
else:
    print("sena")