number=[]
for i in range(10):
    number.append(int(input())%42)
num=set(number)
print(len(num))
