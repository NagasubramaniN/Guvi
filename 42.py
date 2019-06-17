nap,qap=map(int,input().split())
tap=list(map(int,input().split()))
stp=[]
for i in range(qap):
    stp.append(list(map(int,input().split())))
for i in stp:
  x=0
  for j in range(i[0]-1,i[1]):
      x=x+tap[j]
  print(x) 
