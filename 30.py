p,q=map(int,input().split())
r=list(map(int,input().split()))
s=list(map(int,input().split()))
g = 0
if(all(x in r for x in s)): 
    g = 1
if(g==0):
    print("NO")
else:
    print("YES")
