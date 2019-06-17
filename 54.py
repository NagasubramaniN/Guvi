nump=int(input())
vp=[]
kp=bin(2**nump-1)[2::]
lp=len(kp)
for i in range(0,2**nump):
	sp=bin(i)[2::]
	if len(sp)<lp:
		vp.append([sp.count("1"),(lp-len(sp))*"0"+sp])
	else:
		vp.append([sp.count("1"),sp])
vp.sort()
for i in range(0,len(vp)):
        print(vp[i][1])
