manp,sanp=map(int,input().split())
arrayp=list(map(int,input().split()))
ranp=0
for i in range(len(arrayp)):
	for j in range(i+1,len(arrayp)):
		if (arrayp[i]+arrayp[j]==sanp):
			ranp+=1
			break
if(ranp):
	print("yes")
else:
	print("no")
