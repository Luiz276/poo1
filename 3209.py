#Para cada regua, caso ela não seja a ultima subtrair 1 do numero de tomadas que els possui
n = int(input())

for _ in range(n):
    reguas = list(map(int, input().strip().split()))

    total = 0

    for x in range(1, reguas[0]+1):
        total += reguas[x]
        
        if x != reguas[0]:
            total -= 1

    print(total)