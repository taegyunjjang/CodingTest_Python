import sys
from collections import deque
input = sys.stdin.readline

    
def bfs(graph):
    N, M = len(graph), len(graph[0])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    dq = deque()
    dq.append((0, 0, 0))
    while dq:
        x, y, w = dq.popleft()
        if (x, y) == (N - 1, M - 1):
            return visited[x][y][w] + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if not visited[nx][ny][w] and graph[nx][ny] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                dq.append((nx, ny, w))
            elif w == 0 and graph[nx][ny]:
                visited[nx][ny][1] = visited[x][y][0] + 1
                dq.append((nx, ny, 1))
    return -1
                
def solution():
    N, M = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for i in range(N):
        for j, ch in enumerate(input().rstrip()):
            graph[i][j] = int(ch)
    
    print(bfs(graph))
    

solution()