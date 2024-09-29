#https://www.acmicpc.net/problem/2178

import sys
#input = sys.stdin.readline
from collections import deque
q =deque()

def make(s):
    for _ in range(s):
        l = list(map(int,input()))
        graph.append(l)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited=[]
parent = []
#그래프를 새로그려 각칸을 노드로 생각하고 노드를 연결하는
def bfs(graph,s,g):
    global cnt
    q.append((s,g))

    while q:
        s,g = q.popleft()

        for i in range(4):
            new_s = s+dx[i]
            new_g = g+dy[i]
            if 0<=new_s<ms and 0<=new_g<mg and graph[new_s][new_g]==1:
                q.append((new_s,new_g))
                graph[new_s][new_g] = graph[s][g]+1
    print(graph[ms-1][mg-1])     
       
        
cnt =1
ms,mg = map(int,input().split())

visit = [[0]*mg for _ in range(ms)]
graph = []

make(ms)

bfs(graph,0,0)
