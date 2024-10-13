def solution(n, computers):
    
    visited = set()
    graph = [[] for _ in range(len(computers))]
             
    for i,c in enumerate(computers):
        for ii,ic in enumerate(computers[i]):
             if ic ==1:
                graph[i].append(ii) 
    def dfs(start):
        if start not in visited:
            visited.add(start)
            for i in graph[start]:
                if i not in visited:
                    dfs(i)
            return 1
        else:
            return 0
    cnt =0
    for i in range(n):
        if dfs(i)>=1:
            cnt+=1
        
    return cnt