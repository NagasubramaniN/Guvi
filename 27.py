n=int(input())
g=list(map(int,input().split()))
k=[]
for s in range(n):
	if s%2!=0 and g[s]%2==0:  
		k.append(g[s])
	if s%2==0 and g[s]%2!=0:  
		k.append(g[s])
for s in k:
	print(s,end=" ")
