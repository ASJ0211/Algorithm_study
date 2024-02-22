from collections import deque
def solution(cards1, cards2, goal):
    cards1=deque(cards1)
    cards2=deque(cards2)
    r="Yes"
    for i in goal:
        if len(cards1)>=1 and i== cards1[0]:
            if len(cards1)!=0:
                cards1.popleft()
        elif len(cards2)>=1 and i == cards2[0]:
            if len(cards2)!=0:
                cards2.popleft()
        else:
            r="No"
            break
    return r