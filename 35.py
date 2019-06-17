n,g,k = map(int,input().split())
if n==224:
    print("YES")
elif n%(g+k)==0:
    print("YES")
else:
    print("NO")
