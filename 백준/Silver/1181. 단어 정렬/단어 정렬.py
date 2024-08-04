#https://www.acmicpc.net/problem/1181
#1181 단어정렬
list1 = ['bc','abc']
list1.sort()
dict1 = {}


n =int(input())
for i in range(n):
    x = input()
    leng = len(x)
    if leng not in dict1:
        dict1[leng] = []
    dict1[leng].append(x)
    #print(dict1)
dict2=sorted(dict1.items())
dict3 = {k:sorted(set(v)) for k,v in dict2}
for i in dict3.values():
    for j in i:
        print(j)