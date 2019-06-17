j=int(input())
k=list(map(int,input().split()))
l=[]
for i in k:
  if(k.count(i)>1):
    l.append(i)
  else:
    print(i)
