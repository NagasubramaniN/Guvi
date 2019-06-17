np = int(input())
kp = 1000
for x in range(0,20):
    if pow(2,x)<=np:
        a = abs(pow(2,x)-np)
        if a<=kp:
            kp=a
print(kp)
