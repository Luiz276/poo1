A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
# fiz desse jeito por causa do sistema que o professor usa

atriret = (A * C) / 2
acircRc = (C**2) * 3.14159
atrap = ((A + B) * C) / 2
aquad = B**2
aret = A * B

print(f"TRIANGULO: {atriret:.3f}\nCIRCULO: {acircRc:.3f}\nTRAPEZIO: {atrap:.3f}\nQUADRADO: {aquad:.3f}\nRETANGULO: {aret:.3f}")