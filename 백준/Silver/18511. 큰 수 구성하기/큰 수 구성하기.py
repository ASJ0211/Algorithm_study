from itertools import product

N, K = map(int, input().split())
pick = list(input().split())


pick.sort(reverse=True)
L=len(str(N))
found = False
r=0
e=0
for i in range(L,0,-1):
    make= product(pick,repeat=i)
    if e==1:
        break
    for j in make:
        num = int(''.join(j))
        #print(num)
        if num<=N:
            e=1
            break
             
print(num)
