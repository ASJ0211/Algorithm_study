import numpy as np
import math
# def solution(numbers, target):
#     r=[0]
#     r2=[]
#     for i in numbers:
#         for j in r:
#             a1= j+i
#             a2 = j-i
#             r2.append(a1)
#             r2.append(a2)
#         r=r2
#         r2= []
#     result = r.count(target)
#     return result


# [0,0,0,0] 32 개 잘라서 제일 밑 자식 노드만 사용 
def solution(numbers, target):
    z = len(numbers)
    
    list1 = [0 for i in range(2**(z+1))]
    list2 = [0,0]
        
    
    
    
    def tree(numbers,list1,target):
        for i in range(2,len(list1)):
            if i%2 ==0:
                list1[i] = list1[i//2] - numbers[int(math.log(i, 2))-1]
            else:
                list1[i] = list1[i//2] + numbers[int(math.log(i, 2))-1]
            
            
        return list1[len(list1)//2 :].count(target)
    return tree(numbers,list1,target)
