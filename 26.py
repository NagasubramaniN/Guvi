g = int(input())
h=list(map(int,input().split()))
i=0
for a in range(g):
	if h.count(h[a])>1:
		print(h[a],end="")
		break;
	else :
		i=i+1
if i==g :
        print("unique",end="")
