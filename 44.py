ap,bp=map(int,input().split())
mp=list(map(int,input().split()))
tp=[]
for i in range(0,bp):
    dp = []
    dp=list(map(int,input().split()))
    sp = mp[dp[0]-1]
    for j in range(min(dp),max(dp)):
        sp=sp^mp[j]
    tp.append(sp)
for i in range(0,len(tp)):
    print(tp[i])
