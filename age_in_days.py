d = int(input())

a = d/365
d = d%365
m = d / 30
d = d % 30
d = int(d)
m = int(m)
a = int(a)

print(f"{a} ano(s)\n{m} mes(es)\n{d} dia(s)")