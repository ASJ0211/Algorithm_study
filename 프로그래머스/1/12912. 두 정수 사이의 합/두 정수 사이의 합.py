def solution(a, b):
    total = 0 
    if a>b:
        a,b =b,a
    for i in range(a,b+1):
        total +=i
    answer= total
    return answer