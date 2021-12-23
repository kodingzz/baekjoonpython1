n=int(input())
for i in range(n):
    sum=0
    score=0
    a=list(input())
    for j in a:
        if j=="O":
            sum+=1
            score+=sum
        else:
            sum=0
    print(score)

            

