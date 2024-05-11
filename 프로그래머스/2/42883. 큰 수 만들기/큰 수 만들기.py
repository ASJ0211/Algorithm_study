
from collections import deque
def solution(number, k):
    dq = deque(['9'])
    nl = deque(number)

    lnl= len(nl)
    for i in range(lnl):
        j= nl.popleft()
        end=0
        #print('for---')
        #print(dq,'k:',k,'j',j)
        while len(dq)!=0 and end ==0:
            b = dq.pop()
            if b<j and k>=1:              
                end=0
                k-=1
            else:      
                dq.append(b)
                dq.append(j)
                end =1
       # print(dq,k,'B:',b)
    for i in nl:
        dq.append(i)
    s = ''
    for i in dq:
        s+=i
    #print(s,k)
    s=s[1:]
    if k>=1:
        s=s[:-k]
    return s