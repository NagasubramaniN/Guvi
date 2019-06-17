ratp=int(input())
gatp=[]
for i in range(ratp):
    lip=[]
    lip=list(map(int,input().split()))
    gatp.append(lip)
 
fatp=[]   
for i in gatp:
    for j in i:
        fatp.append(j)
fatp.sort()
for i in fatp:
    print(i,end=" ")
