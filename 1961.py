p, n = map(int, input().split())
canos = input().split()
canos = [int(x) for x in canos]
for i in range(0, n):
    if i+1 == n:
        print("YOU WIN")
        break
    elif canos[i] > canos[i+1] and canos[i] - p <= canos[i+1]:
        continue
    elif canos[i+1] >= canos[i] and canos[i] + p >= canos[i+1]:
        continue
    else:
        print("GAME OVER")
        break