import numpy as np
from collections import deque
def solution(name):
    #chr(65) >> A
    #ord(A) >>65
    #al = {chr(i).upper(): i-97 for i in range(97, 123)}
    #al = deque([chr(i).upper() for i in range(97,123)])
    nl = deque(name)
    sero = 0
    garo = []
    for t in nl:
        #print(ord(t)-ord("A"))
        #print(ord("Z")-ord(t)+1)
        spell = min(ord(t)-ord("A"),ord("Z")-ord(t)+1)
        sero+=spell 
    for i in range(len(nl)):
        l_r = name[-i:] + name[:-i] #왼쪽먼저 갔다가 + 오른쪽
        r_l = name[i: :-1] + name[i+1:][::-1] # 기준점에서 빠꾸 + 좌측
        l1, l2 = [n.rstrip('A') for n in [l_r, r_l]]
        print(l_r,r_l)
        #print(l1,l2)
        r = min(len(l1)-1+i,len(l2)-1+i)
        garo.append(r)
        
    #print(sero)
    print(garo)
    garo_result=min(garo)
    if garo_result<=0:
        garo_result = 0
            
    return sero+garo_result
