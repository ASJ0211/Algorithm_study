#최소 2장ㅇ이상 c=b

def solution(cards):
    list=[]
    dic={}
    c=0
    for i in cards:
        dic[c]=i
        c+=1
    for i in range(len(dic)):
        g=0
        while dic[i]!=0:
            n=dic[i]
            dic[i]=0
            i=n
            i-=1
            g+=1
        list.append(g)
    list.sort()
    return list[-1]*list[-2]