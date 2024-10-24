def solution(numbers, target):
    from collections import deque


    q1 = deque([0])
    q2 = deque()
    for i in numbers:
        print(i)
        for d in q1:
            q2.append(d+i)
            q2.append(d-i)
        q1 =q2
        q2 = deque()
    return q1.count(target)