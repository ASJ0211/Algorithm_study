def solution(n, arr1, arr2):
    n=str(n)
    answer = []
    ans=""
    r1=[]
    r2=[]
    for i in arr1:
        b=format(int(bin(i)[2:]),n+'.0f')
        bl=""
        for i in b:
            if i=="1":
                bl+="#"
            else:
                bl+=" "     
        r1.append(bl)
    for i in arr2:
        b=format(int(bin(i)[2:]),n+'.0f')
        bl=""
        for i in b:
            if i=="1":
                bl+="#"
            else:
                bl+=" "     
        r2.append(bl)
    n=int(n)
    for i in range(n):
        ans=""
        for j in range(n):
            if r1[i][j]=="#" or r2[i][j]=="#":
                ans+="#"
            else:
                ans+=" "
        answer.append(ans)
    print(r1)
    print(r2)
    return answer
