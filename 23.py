d=int(input())
e=list(map(int,input().split()))
f=[]
for i in e:
    if(i==e.index(i)):
        f.append(i)
print(*(sorted(f)))
if(len(f)==0):
    print(-1)
