n=int(input())
g=list(map(int,input().split()))
cnt=0
for i in range(len(g)-2):
    for j in range(i+1,len(g)-1):
        for k in range(j+1,len(g)):
            if g[i]<g[j]<g[k] and i<j<k:
                cnt=cnt+1
print(cnt)
