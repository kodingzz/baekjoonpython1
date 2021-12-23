c=int(input())
for i in range(c):
    d=list(map(int,input().split()))
    avg=sum(d[1:])/d[0]
    score=0
    for j in d[1:]:
        if j>avg:
            score+=1
    #print(f"{score/d[0]*100:.3f}%")
    print('%.3f%%'%(score/d[0]*100))
