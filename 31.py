n=int(input())
g=[]
for k in range(0,n):  
    d=input()
    g.append(d)
list=[]
for k in zip(*g):
    if (k.count(k[0])==len(k)): 
        list.append(k[0])
    else:
        break
print(''.join(list))
