num=input().split()
first_no=int(num[0])
second_no=int(num[1])
third_no=int(num[2])
if(first_no>second_no and first_no>third_no):
    print(first_no)
elif(second_no>third_no):
    print(second_no)
else:
    print(third_no)
