# def solution(players, callings):
#     for i in callings:
#         for index,p in enumerate(players):
#             if i ==p:
#                 players[index-1],players[index] = players[index],players[index-1]
#                 print()
#                 break    
        
#     answer = players
#     return answer

#dict로 해서 바로 찾는 접근법으로 해야할듯
#dict를 2개를 해야하나? 
# gpt 
#앞사람은 index - 1 로 바로 접근할 수 있어요.
#그래서 dict랑 list를 같이 관리하면 O(1) 안에 해결됩니다 ✅ 라네요.

def solution(players, callings):
    d=dict()
    l=list()
    for i,p in enumerate(players):
        d[p]=i
        l.append(p)
        
    for c in callings:
        f=d[c]
        before= l[f-1]
        d[c]-=1
        d[before]+=1
        l[f],l[f-1]=l[f-1],l[f]

        
    return l