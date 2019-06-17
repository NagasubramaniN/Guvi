import math
import functools
inpt11,inpt21=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(inpt21):
    cp,dp=map(int,input().split())
    tempe=functools.reduce(math.gcd,List[cp-1:dp])
    print(tempe)
