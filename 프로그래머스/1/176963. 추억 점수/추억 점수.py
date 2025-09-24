def solution(name, yearning, photo):
    d=dict(zip(name,yearning))
    
    answer=list()
   
    for i in photo:
        ans=0
        for j in i:
            try:
                ans+=d[j]
                #ans += d.get(j, 0)
                
            except:
                continue
        answer.append(ans)
    return answer








# def solution(name, yearning, photo):
#     answer = []
#     dic={}
#     c=0

#     for i in name:
#         dic[i]=yearning[c]
#         c+=1
#     for i in photo:
#         r=0
#         for j in i:
#             if j not in dic:
#                 dic[j]=0
#             r+=dic[j]
#             print(r)
#         answer.append(r)
#     return answer