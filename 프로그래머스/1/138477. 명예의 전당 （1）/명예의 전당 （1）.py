def solution(k, score):
    result= []
    l = []
    for i in score:
        l.append(i)
        l=sorted(l)
        if len(l) <=k:
            r=l[0]
        else:
            r=l[-k]
        result.append(r)
    return result