from collections import deque
q = deque()
def solution(maps):
    ms = len(maps)
    mg = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def bfs(g,s):
        q.append((g,s))
        while q:
            g,s = q.popleft()
            for i in range(4):
                new_g = g+dx[i]
                new_s = s+dy[i]
                if 0<=new_g<mg and 0<=new_s<ms and maps[new_s][new_g]==1:
                    q.append((new_g,new_s))
                    maps[new_s][new_g] = maps[s][g]+1
                    
                    
                    
                    
    bfs(0,0)
    print(maps)
    ans = maps[-1][-1]
    if ans == 1:
        return -1
    else:
        return ans
    