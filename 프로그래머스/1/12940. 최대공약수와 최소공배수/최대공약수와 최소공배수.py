import math
def solution(n, m):
    if n > m:
        n,m = m,n
    for i in range(1,n+1):
        if n%i==0 and m%i==0:
            r1=i
    t=1
    nl=[]
    ml=[]
    while t>=1:
        nl.append(n*t)
        ml.append(m*t)
        if n*t in ml:
            r2=n*t
            t=0
            break
        t+=1
            
    ans=[]
    ans.append(r1)
    ans.append(r2)
    return ans