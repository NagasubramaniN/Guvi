n1p,m1p=map(int,input().split())
lp=[]
uip=0
for i in range(n1p):
    l.append(list(map(int,input().split())))   
for i in range(n1p):
    for j in range(m1p-1):
        for k in range(j+1,m1p+1):
            if lp[i][j:k]==[1p]*len(lp[i][j:k]):
                 if all(lp[p+i][j:k]==[1p]*len(lp[p+i][j:k]) for p in range(len(lp[i][j:k])-1)):
                     if len(lp[i][j:k])>uip:
                        uip=len(lp[i][j:k])
if len(lp)==1 and len(lp[0])==1 and lp[0][0]==1:
    print(1)
for i in range(uip):
    print(*[1]*uip) 
