def euclides(a, b):
    if a == 0:
        return(b)
    elif b == 0:
        return(a)
    temp = euclides(b, (a%b))
    return(temp)

n = int(input())

for _ in range(n):
    cartas1, cartas2 = map(int, input().split())

    print(euclides(cartas1, cartas2))