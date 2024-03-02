def solution(s):
    sl = list(s)
    result=[]
    ans=""

    sl.sort(reverse=True)
    for i in sl:
        ans+=i
    
    
    return ans