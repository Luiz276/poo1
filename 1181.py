mat = [None] * 12
for x in range(len(mat)):
    mat[x] = [None] * 12

line = int(input())
op = input()

for x in range(12):
    for y in range(12):
        mat[x][y] = float(input())

soma = sum(mat[line])

if op == 'S':
    print(f"{soma:.1f}")
else:
    print(f"{soma/12:.1f}")