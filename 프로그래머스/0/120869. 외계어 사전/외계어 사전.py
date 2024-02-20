def solution(spell, dic):
    ans=[]
    for i in dic:
        c=0
        for j in spell:
            if j in i:
                c+=1
        if c== len(spell):
            ans.append(1)
        else:
            ans.append(2)
    return min(ans)