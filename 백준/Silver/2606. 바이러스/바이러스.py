#https://www.acmicpc.net/problem/2606

visited = set()
graph = dict()
a= int(input())
num = int(input())

def make(n):
    for i in range(n):
        a,b = map(int,input().split())
        if a not in graph:
            graph[a]= []
        if b not in graph:
            graph[b]= []       
        graph[a].append(b)
        graph[b].append(a)     

ans =set()      
def dfs(graph,start):
    if start not in visited:
        visited.add(start)
        ans.add(start)
        for i in graph[start]:
            dfs(graph,i)


make(num)

try:
    dfs(graph,1)

    print(len(ans)-1)
except:
    print(0)
