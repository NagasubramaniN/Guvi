from itertools import combinations
ltr1,num1=map(int,input().split())
num2=len(str(ltr1))
p=list(combinations(str(ltr1),num2-num1))
p=(sorted(p))
q="".join(p[0])
print(q)
