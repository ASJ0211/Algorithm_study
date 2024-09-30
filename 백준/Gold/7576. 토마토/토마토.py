#https://www.acmicpc.net/problem/7576

import sys
from collections import deque

mg,ms = map(int,input().split())
graph= []
for i in range(ms):
    l = list(map(int,input().split()))
    graph.append(l)

q= deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans=1
def bfs(g,s):

    if graph[s][g] == 1:
        q.append((g,s))

def search(q):
    global ans
    while q:
        g,s = q.popleft()
        for i in range(4):
            new_g = g+dx[i]
            new_s = s+dy[i] 
            if 0<=new_g<mg and 0<=new_s<ms and graph[new_s][new_g]==0:                    
                q.append((new_g,new_s))
                graph[new_s][new_g] = graph[s][g]+1
                ans = graph[new_s][new_g] 
for s in range(ms):
    for g in range(mg):
        bfs(g,s)
search(q)
#print(graph)

for i in graph:
    #print("i",i)
    if 0 in i:
        ans=0
print(ans-1)
# 