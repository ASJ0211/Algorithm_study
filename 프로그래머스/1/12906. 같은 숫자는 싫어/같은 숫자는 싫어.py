def solution(arr):
    r=[]
    for i in arr:
        if len(r)>=1 and i == r[-1]:
            pass
        else:
            r.append(i)
#ㅁㄴㅇㄹ    
    return r