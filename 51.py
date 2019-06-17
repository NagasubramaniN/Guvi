pp=int(input())
qp=list(map(int,input().split()))
x1p=yp=up=kp=0

for i in range(0,pp-1):
    if i==0:
        x1p=(x1p+qp[i])/(i+1)
    else:
        x1p=0
        for tp in range(0,i):
            x1p=x1p+qp[tp]
        x1p = (x1p + qp[i]) // (i + 1)
    kp=0
    for j in range(i+1,pp):
        yp=yp+qp[j]
        kp=kp+1
        if j==pp-1:
            yp=yp//(kp)
    if x1p==yp:
        up=1
        print("yes")
if up==0:
    print("no")
