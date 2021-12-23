number=[]
Max=0
for i in range(9):
    number.append(int(input()))
    if number[i]>Max:
        Max=number[i]
        sequence=i+1
print(Max)
print(sequence)
