def solution(ingredient):
    answer = 0
    a = ''

    for i in ingredient:
        a += str(i)
        if a[-4:] == '1231':
            a = a[:-4]
            answer += 1
    return answer

# def solution(ingredient):
    
#     stack = []
#     c=0
#     for i in ingredient:
#         stack.append(i)
#         if stack[-4:]==[1,2,3,1]:
#             stack = stack[:-4]
#             c+=1
#         #print(stack)
#     return c
    