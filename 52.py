op=int(input())
a1p=list(map(int,input().split()))
b1p=[]
c1p=[]
for i1p in range(len(a1p)):
    if(i1p%2==0):
        b1p.append(a1p[i1p])
    else:
        c1p.append(a1p[i1p])
for j1p in b1p:
    d1p=sum(b1p)
for k1p in c1p:
    f1p=sum(c1p)
if(d1p>f1p):
    print(d1p)
else:
    print(f1p)
