import sys
from collections import deque
input = sys.stdin.readline


def find_target(graph, N, M):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                graph[i][j] = 0
                return (i, j)
            
def distance_from_target(graph, target, visited, N, M):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    dq = deque()
    dq.append(target)
    while dq:
        x, y = dq.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if visited[nx][ny]:
                continue
            
            if graph[nx][ny] == 0:
                visited[nx][ny] = True
                continue
            
            if graph[nx][ny] == 1:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))

def solution():
    N, M = map(int, input().split())
    visited = [[False] * M for _ in range(N)]
    graph = [list(map(int, input().split())) for _ in range(N)]
    target = find_target(graph, N, M)
    distance_from_target(graph, target, visited, N, M)
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j]:
                graph[i][j] = -1
                
    for i in range(N):
        print(*graph[i])

            
solution()