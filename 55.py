np=int(input())
lstp=list(map(int,input().split()))
m1p=[]
a1p=1
for i in range(np-1):
    if lstp[i]<lstp[i+1]:
        a1p+=1
    else:
        m1p.append(a1p)
        a1p=1
m1p.append(a1p)
print(max(m1p))
