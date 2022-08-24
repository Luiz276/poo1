#Caso o numero registrado na lista "hora" seja maior que 0, adicionar um ao contador. Após isso, basta comprara o contador ao número de alunos que podem faltar em uma aula
#Caso ele extrapole este número, imprimir "NO"
n, k = map(int, input().split())
hora = list(map(int, input().strip().split()))
count = 0

for x in hora:
    if x > 0:
        count+=1
if count <= (n-k):
    print("YES")
else:
    print("NO")