x=int(input())
y=list(map(int,input().split()))
z=[]
for p in range(x):
    for q in range(p+1,len(y)):
        if(y[q]==y[p]):
          z.append(y[p])
if (len(z)==0):
    print("unique")
else:
    z.sort()
    r=set(z)
    for p in r:
        print(p,end=" ")
