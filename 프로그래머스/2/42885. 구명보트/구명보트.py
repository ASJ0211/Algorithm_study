from collections import deque
def solution(people, limit):
    r=0
    people.sort()
    people= deque(people)
    while len(people)>=2:
        nl=limit -people[-1]
        people.pop()
        if people[0]> nl:
            r+=1
        else:
            people.popleft()
            r+=1
    if len(people)==1:
        r+=1
    return r



