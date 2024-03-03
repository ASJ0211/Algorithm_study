import math
def solution(n):
    r=0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            r+=i
            if i!=math.sqrt(n):
                r+=n//i
    return r
            
    