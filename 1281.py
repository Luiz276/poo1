t = int(input())
frutas = {}
for _ in range(t):
    soma = 0
    m = int(input())

    for _ in range(m):
        x, y = input().split()

        frutas[x]= float(y)
    
    n = int(input())

    for _ in range(n):
        frut, qnt = input().split()

        soma += frutas[frut] * int(qnt)
    
    print(f"R$ {soma:.2f}")