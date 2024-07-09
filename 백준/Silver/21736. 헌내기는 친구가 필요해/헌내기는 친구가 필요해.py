import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, start):
    N, M = len(graph), len(graph[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    cnt = 0
    
    visited = [[False] * M for _ in range(N)]    
    visited[start[0]][start[1]] = True
    
    dq = deque()
    dq.append(start)
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 'X':
                    continue
                
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                    if graph[nx][ny] == 'P':
                        cnt += 1
    return cnt       
             
def find_idx(graph):
    N, M = len(graph), len(graph[0])
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'I':
                return (i, j)

def solution():
    N, M = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(N)]
    start = find_idx(graph)
    cnt = bfs(graph, start)
    
    if cnt:
        print(cnt)
    else:
        print('TT')
    
    
solution()