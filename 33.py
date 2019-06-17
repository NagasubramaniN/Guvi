n,a=map(str,input().split())
g=abs(len(n)-len(a))
for i in range(len(n)):
        if len(a)==1 and a[i] in n:
            break
        if n[i]!=a[i]:
            g=g+1
print(g)
