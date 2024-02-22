def solution(array):
    dic = {}
    for i in (array):
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    sorted_dic = sorted(dic.items(),key = lambda x : x[1] )
    
    if len(sorted_dic)>=2 and sorted_dic[-1][1]== sorted_dic[-2][1]:
        r=-1
    else:
        r= sorted_dic[-1][0]
    return r