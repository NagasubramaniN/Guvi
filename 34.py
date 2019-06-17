mp,jp=map(str,input().split())
x=0
if len(mp)>len(jp):
  mp,jp=jp,mp
i=0
while i<len(mp):
  x+=(ord(jp[i])-ord(mp[i]))
  i+=1
for i in range(i,len(jp)):
  x+=ord(jp[i])-ord('a')+1
print(x)
