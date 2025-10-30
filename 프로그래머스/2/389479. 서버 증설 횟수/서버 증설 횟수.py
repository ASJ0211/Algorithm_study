from collections import deque
def solution(players, m, k):
    ans = 0
    players=deque(players)
    lk=deque([0]*k)
    for t in range(24):
        np=players.popleft()
        needs=np//m
        lk.popleft()        
        nowserver=sum(lk)
        if needs>nowserver:
            ans+= needs-nowserver
            lk.append(needs-nowserver)
        else:
            lk.append(0)
        print(lk)
    return ans
        
    
    
    
# from collections import deque
# def solution(players, m, k):
#     ans = 0
#     players=deque(players)
#     lk=deque([0]*k)
#     for t in range(24):
#         np=players.popleft()
#         a=np//(m*( 1+sum(lk) ))
#         #print(sum(lk))
#         #print(a)
#         if a>=1:
#             ans+=a
#         lk.popleft()
#         lk.append(a)
#         print(a)
#     return ans
        