na, da, va = input().split()
nb, db, vb = input().split()

na = int(na)
da = int(da)
va = int(va)
nb = int(nb)
db = int(db)
vb = int(vb)

ta = da/va
tb = db/vb

if ta > tb:
    print(nb)
else:
    print(na)