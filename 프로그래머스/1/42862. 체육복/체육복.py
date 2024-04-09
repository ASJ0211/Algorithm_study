def solution(n, lost, reserve):
    l=lost.copy()
    r=reserve.copy()
    for i in lost:
        if i in reserve:
            r.remove(i)
            l.remove(i)
    b0=[]
    b11=[]
    b12=[]
    b2=[]
    for i in l:
        c1=0
        c2=0
        if i-1 in r:
            c1+=1
        if i+1 in r:
            c2+=1
        if (c1+c2)==0:
            b0.append(i)
        elif (c1+c2)==2:
            b2.append(i)
        elif c1==1:
            b11.append(i)
        elif c2==1:
            b12.append(i)
    lc=0
    for i in b11:
        r.remove(i-1)
        lc+=1
    for i in b12:
        try:
            r.remove(i+1)
            lc+=1
        except:
            pass
        
    for i in b2:
        if i-1 in r:
            r.remove(i-1)
            lc+=1
        elif i+1 in r:
            r.remove(i+1)
            lc+=1
    result = n-(len(l)-lc)
    return result