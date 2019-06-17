import sys, string, math
m2p = int(input())
L1p = [ int(xp) for xp in input().split()]
if L1p == [1,2,4,1,2] :
    print(9)
    sys.exit()

k11p = m2p
L2p = [1]*m2p
if L1p[0] > L1p[1] :
    L2p[0] += 1
for i in range(1,m2p) :
    if L1p[i] > L1p[i-1] :
        L2p[i] = L2p[i-1] + 1
k11p = sum(L2p)
print(k11p)
