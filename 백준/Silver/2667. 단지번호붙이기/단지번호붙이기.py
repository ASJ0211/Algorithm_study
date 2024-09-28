#https://www.acmicpc.net/problem/2667
import sys

#input = sys.stdin.readlines
from collections import deque
q= deque()

n = int(input())

graph=[]
visited = [[0]*(n) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def make(n):
    for i in range(n):
        graph.append(list(map(int,input())))

def bfs(graph,s,g):
    q.append((s,g))
    c = 0
    while q:
        x,y = q.popleft()
        if visited[x][y]==1: #아직 방문하지 않은 노드가 2,2 일때 (1,2) (2,1) 를 search하면서 (1,3),(2,2),(2,2) 처럼 두번 들어가는 경우 visit 체크가 필요해서 넣음
            continue
        visited[x][y]=1
        c+=1
        #print("현재",x,y,"C =",c,"Q=",q)
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            #print("new=",new_x,new_y)
            if 0 <= new_x <n and 0 <= new_y <n:
                if visited[new_x][new_y]==0 and graph[new_x][new_y]==1:                    
                    q.append((new_x,new_y))
    #print("q end ------------------",q)
    return c

make(n)
#print(graph)
#print(visited)
cnt = []

for s in range(n):
    for g in range(n):
        if visited[s][g]==0 and graph[s][g]==1:
            cnt.append(bfs(graph,s,g))
print(len(cnt))
cnt.sort()
for i in cnt:
    print(i)
#print(cnt)