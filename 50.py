np,mp=map(int,input().split())
tp=list(map(int,input().split()))
up=0
yp=sorted(tp)
xp=(yp[::-1])
for i in range(0,len(xp)):
    zp = mp //(xp[i])
    up = up + zp
    mp = mp - (zp *xp[i])
print(up)
