n=int(input())
g=[int(i) for i in input().split()]
k=0
for i in range(n):
   for j in range(i):
      if g[j]<g[i]:
         k+=g[j]
print(k)   
