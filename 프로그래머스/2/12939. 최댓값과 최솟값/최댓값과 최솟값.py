def solution(s):
    sl=list(map(int,s.split()))
    sl.sort()
    a=str(min(sl))
    b=str(max(sl))
    
    #해ㅐㅇ
    answer=str(a+' '+b)
    return answer