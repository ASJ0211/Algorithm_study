import numpy as np
# [0,0,0,0] 32 개 잘라서 제일 밑 자식 노드만 사용 
def solution(numbers, target):
    r=[0]
    r2=[]
    for i in numbers:
        for j in r:
            a1= j+i
            a2 = j-i
            r2.append(a1)
            r2.append(a2)
        r=r2
        r2= []
    result = r.count(target)
    return result
