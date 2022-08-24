#receber as inputs do rendimento das plantas em formato de matriz e calcular divisão e módulo por 60 da soma de todas as inputs
while True:
    try:
        m,n = map(int, input().split())
        soma = 0

        mat = [None] * m
        for x in range(m):
            mat[x] = list(map(int, input().strip().split()))

        for x in mat:
            soma += sum(x)
        
        print(f"{int(soma/60)} saca(s) e {soma%60} litro(s)")
    except EOFError:
        break