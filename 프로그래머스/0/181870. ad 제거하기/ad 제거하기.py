def solution(strArr):
    r = []
    for i in strArr:
        if "ad" not in i:
            r.append(i)
    return r