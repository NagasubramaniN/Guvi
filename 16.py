x,y=list(map(int,input().split()))
for p in range(x+1,y):
  for q in range(2,p):
    if p%q==0:
      break
  else:
    print(p,end=" ")
