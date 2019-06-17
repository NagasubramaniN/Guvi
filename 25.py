t=input()
u=1
for v in range(len(t)-1):
    s=t[v]+t[v+1]
    p=int(s)
    if p<=26 and t[v]!="0":
        u+=1
if u==3:
    print(u)
else:
    print(u+(u-1)//2)
