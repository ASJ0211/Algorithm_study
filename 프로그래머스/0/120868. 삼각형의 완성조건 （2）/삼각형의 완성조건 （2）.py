def solution(sides):
    sides.sort()
    l=sides[-1]
    s=sides[0]
    r1=l-s
    c=0
    for i in range(r1+1,l+1):
        c+=1
    r2=s-1
    return c+r2