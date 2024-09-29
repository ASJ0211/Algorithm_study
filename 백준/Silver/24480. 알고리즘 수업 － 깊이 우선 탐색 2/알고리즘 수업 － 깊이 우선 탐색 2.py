#https://www.acmicpc.net/problem/24480

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def make(m):
    for i in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

def dfs(graph,r):
    global cnt
    visited[r]=cnt
    cnt+=1
    for i in graph[r]:
        if visited[i]==0:
            dfs(graph,i)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt=1
make(m)
for i in range(1,n+1):
    graph[i].sort(reverse=True)
dfs(graph,r)
for i in range(1,n+1):
    print(visited[i])