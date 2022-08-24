cv, ce, cs, fv, fe, fs = input().split()

cv = int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)

pontosc = (cv*3) + ce
pontosf = (fv*3) + fe

if pontosc == pontosf:
    if cs==fs:
        print("=")
    elif cs>fs:
        print("C")
    else:
        print("F")
elif pontosc>pontosf:
    print("C")
else:
    print("F")