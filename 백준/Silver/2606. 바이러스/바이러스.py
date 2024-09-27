import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
pair = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(pair):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    global cnt

    visited[x] = True
    # cnt += 1
    for i in graph[x]:
        if not visited[i]:
            cnt+=1
            dfs(i)

dfs(1)
print(cnt)