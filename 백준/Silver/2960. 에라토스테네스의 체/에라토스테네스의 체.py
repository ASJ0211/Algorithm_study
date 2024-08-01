#2960번 
#에라토스테네스의 체
n,k = map(int,input().split())
list1 = []
for i in range(2,n+1):
    list1.append(i)
#print(list1)

def era(list1,k):
    count = k
    first = list1[0]
    list2 = []
    for i in list1:
        if i%first !=0:
            list2.append(i)
        else:
            count -=1
            if count ==0:
                print(i)
                break
    list1 = list2
    if count >=1:
        era(list1,count)
era(list1,k)
    