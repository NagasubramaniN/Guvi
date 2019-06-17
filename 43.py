sap,nap=map(int,input().split())
pap=list(map(int,input().split()))
zzp=[]
for i in range(0,n):
    fp=[]
    fp=list(map(int,input().split()))
    mp=fp[0]
    for j in range(min(fp)-1,max(fp)):
        if mp>pap[j]: mp=pap[j]
    zzp.append(mp)
for i in range(0,len(zzp)):
    print(zzp[i])
