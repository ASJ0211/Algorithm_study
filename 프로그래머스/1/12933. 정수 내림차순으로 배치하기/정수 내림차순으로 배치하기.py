def solution(n):
    n=str(n)
    l= list(n)
    #l = reversed(l)
    #l = reversed(l)

    l.sort(reverse=True)
    

    l=list(map(str,l))
    r=''
    for i in l:
        r+=i
    r=int(r)
    return r

