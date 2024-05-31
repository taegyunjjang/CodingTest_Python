import sys
from collections import deque
input = sys.stdin.readline


def BFS(graph, visited):
    N = len(graph)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            
            cmp = graph[i][j]
            dq = deque()
            dq.append([i, j])
            
            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    
                    if visited[nx][ny]:
                        continue
                    
                    if cmp == graph[nx][ny]:
                        visited[nx][ny] = True
                        dq.append([nx, ny])
            cnt += 1
            
    return cnt
    
                
def solution():
    N = int(input())
    graph = [[i for i in input().rstrip()] for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = []  
    
    answer.append(BFS(graph, visited))
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'
                
    visited = [[False] * N for _ in range(N)]
    answer.append(BFS(graph, visited))
    print(*answer)
    
    
solution()
