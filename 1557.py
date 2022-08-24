while True:
    n = int(input())
    if  n == 0:
        break

    mat = [1] * n
    for x in range(n):
        mat[x] = [1] * n

    t = len(str(pow(4, n-1)))

    for x in range(n):
        for y in range(n):
            if x == 0 and y == 0:
                print(str(mat[x][y]).rjust(t), end = "")
            elif x != 0 and y == 0:
                mat[x][y] = mat[x-1][y] * 2
                print(str(mat[x][y]).rjust(t), end = "")
            else:
                mat[x][y] = mat[x][y-1] * 2
                print(str(mat[x][y]).rjust(t), end = "")

            if y == n-1:
                print("")
            else:
                print(" ", end = "")
    print("")