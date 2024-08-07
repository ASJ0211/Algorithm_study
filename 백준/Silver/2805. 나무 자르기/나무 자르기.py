# import sys
# input = sys.stdin.read

#2805
#https://www.acmicpc.net/problem/2805

n,m =map(int,input().split())
array1 =list(map(int,input().split()))
#print(list1)
top = max(array1)-1
bot = 0
while top>=bot:
    cut = (bot+top)//2
    total = sum(x - cut for x in array1 if x > cut)
    if total>=m:
        bot = cut+1
    else:
        top = cut-1

    #print(top,bot,cut,total)
print(top)       