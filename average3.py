n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

med = ((2*n1)+(3*n2)+(4*n3)+(1*n4)) / 10

print(f"Media: {med:.1f}")
if med>=7:
    print("Aluno aprovado.")
elif med<5:
    print("Aluno reprovado.")
elif med>=5 and med<7:
    print("Aluno em exame.")
    n5 = float(input())
    med2 = (med + n5) / 2
    print(f"Nota do exame: {n5:.1f}")
    if med2>=5:
        print("Aluno aprovado.")
        print(f"Media final: {med2:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {med2:.1f}")