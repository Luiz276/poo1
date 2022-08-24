n= int(input())
while n!= 0:
    j = 0
    m = 0
    lista = input().split()
    result = [int(x) for x in lista]
    for i in range(0,n):
        if result[i] == 1:
            j += 1
        else:
            m += 1
    print(f"Mary won {m} times and John won {j} times")
    n = int(input())