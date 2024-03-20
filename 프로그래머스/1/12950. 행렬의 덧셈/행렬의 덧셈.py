def solution(arr1, arr2):
    result2=[]
    for i in range(len(arr1)):       
        result1=[]
        
        for j in range(len(arr1[i])):
            
            r=0
            r+=arr1[i][j]
            r+=arr2[i][j]
            result1.append(r)
        result2.append(result1)
    return result2