s= int(input())
a= list(map(int,input().split()))
for n in range(0,s-2):
  for g in range(n+1,s-1):
    for k in range(g+1,s):
      if a[n]+a[g] == a[k]:
        print(a[n],a[g],a[k])
