p=int(input())
q=input().split()
r=[]
s=''
for i in (q):
    r.append(i)
r.sort(reverse=True)
for i in range(len(r)):
    s+=str(r[i])
print(s)
