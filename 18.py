x,y=map(int,input().split())
for a in range(x+1,y):
 sum=0
 temp=a
 while(temp>0):
  digit=temp%10
  sum+=digit**3
  temp=temp//10
 if(a==sum):
  print(a,end=" ")
