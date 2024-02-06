def solution(k, m, score):
    dic={}
    for i in range(k):
        dic[i]=0
    for i in score:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    t=len(score)//m
    r=0
    for i in range(t):
        for j in range(m):
            while dic[k]==0:
                k-=1
            dic[k]-=1  
        r+= k*m
    return r