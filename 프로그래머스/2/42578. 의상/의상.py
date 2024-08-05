def solution(clothes):
    dict1={}

 
    for i in clothes:
        if i[1] not in dict1:
            dict1[str(i[1])] = []
        dict1[i[1]].append(i[0])
    
    rl = list(dict1.values())
    print(rl)
    r=1
    for i in rl:
        print(i)
        r=r*(len(i)+1)

    return r-1