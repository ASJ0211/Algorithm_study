def solution(n):
    answer=[]
    for i in range(1,n+1):
        c=0
        if i<=3:
            answer.append(i)
        else:
            for k in range(2,i):
                if i%k==0:
                    c+=1
            if c==0:
                answer.append(i)
        
    return n-len(answer)