p=int(input())
q=list(map(int,input().split()))
r=max(q)
a,b=0,0
for c in range(0,len(q)):
  for d in range(c+1,len(q)):
    if abs(q[c]+q[d])<r:
      a,b=q[c],q[d]
      r=abs(e+f)
print(a,b)
