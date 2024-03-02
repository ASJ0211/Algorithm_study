def solution(s):
    s= list(s)
    r=[]
    c=0
    for i in s:
        if c==0:
            i=i.upper()
        else:
            i=i.lower()
        r.append(i)
        c+=1
        if i ==" ":
            c=0
            
    result=""
    for i in r:
        try:
            result+=int(i)
        except:
            result+=i
    return result

        