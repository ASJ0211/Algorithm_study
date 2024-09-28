#https://www.acmicpc.net/problem/1260
#DFS BFS를 둘다 구현해야함
from collections import deque
import sys
#input() =sys.stdin.readline()
n,m,v = map(int,input().split())


graph = [[] for i in range(n+1)]
visitedd = [0]*(m+2)
visitedb = [0]*(m+2)

q= deque()
def make(m):
    for i in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)




def dfs(graph,start):
    global cnt
    if start not in visitedd:
        visitedd[cnt]=start
        cnt+=1
        for i in graph[start]:
            dfs(graph,i)

def bfs(graph,start):
    global cnt
    q.append(start)

    while q:
        now_node =q.popleft()

        if now_node not in visitedb:
            visitedb[cnt]=now_node
            cnt+=1
            for i in graph[now_node]:
                q.append(i)

make(m)
for i in graph:
    i.sort()
cnt =1
dfs(graph,v)

for i in range(1,m+2):
    if visitedd[i]==0:
        break
    print(visitedd[i],end=' ')

print('')
cnt =1
bfs(graph,v)

for i in range(1,m+2):
    if visitedb[i]==0:
        break
    print(visitedb[i],end=' ')