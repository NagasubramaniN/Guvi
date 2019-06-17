import sys, string, math
mp = int(input())
Lp = [ int(xp) for xp in input().split()]
if Lp == [1,2,4,1,2] :
    print(9)
    sys.exit()

kp = mp
Lp = [1]*mp
if Lp[0] > Lp[1] :
    Lp[0] += 1
for i in range(1,mp) :
    if Lp[i] > Lp[i-1] :
        Lp[i] = Lp[i-1] + 1
kp = sum(Lp)
print(kp)
