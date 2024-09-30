#https://www.acmicpc.net/problem/1012

import sys
#input = sys.stdin.readline
from collections import deque
turn = int(input())
ans = []
for _ in range(turn):

    mg,ms,k = map(int,input().split())

    graph = [[0]*(mg) for _ in range(ms)]

    for _ in range(k):
        g,s = map(int,input().split())
        graph[s][g]=1


    q = deque()

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    cnt=0
    def bfs(graph,g,s):
        global cnt
        q.append((g,s))
        if graph[s][g]==1:
            cnt+=1
        while q:
            g,s = q.popleft()
            if graph[s][g]==1:
                graph[s][g]=0
                for i in range(4):
                    new_g = g+dx[i]
                    new_s = s+dy[i]
                    if 0<= new_g <mg and 0<=new_s <ms:
                        q.append((new_g,new_s))


    for s in range(ms):
        for g in range(mg):
            bfs(graph,g,s)
    ans.append(cnt)
for i in ans:
    print(i)
