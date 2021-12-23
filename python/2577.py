a=int(input())
b=int(input())
c=int(input())
d=a*b*c
number=list(str(d))

for i in range(10):
    account = 0
    for j in range(len(number)):
        if number[j]==str(i):
             account+=1
    print(account)
'''
for i in range(10):
    print(number.count(str(i)))
'''




