#Basta utilizar set para descartar as figurinhas repetidas e contar quantos tipos de figurinhas existem
#depois, basta subtrair do total de figurinhas a len() do set para obter a tanto de repetidas
n = int(input())
fig = [None] * n

for a in range(n):
    fig[a] = int(input())

print(len(set(fig)))
print(n - len(set(fig)))