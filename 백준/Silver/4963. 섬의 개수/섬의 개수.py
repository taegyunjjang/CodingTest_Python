import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, visited, li):
    w, h = len(graph[0]), len(graph)
    dx = [-1, 0, 1, 0, -1, -1, 1, 1]
    dy = [0, -1, 0, 1, -1, 1, -1, 1]
    
    dq = deque()
    dq.append(li)
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            
            if not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = True
                dq.append((nx, ny))
    
def solution():
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        
        graph = [list(map(int, input().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        
        cnt = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] and not visited[i][j]:
                    cnt += 1
                    visited[i][j] = True
                    bfs(graph, visited, [i, j])
        print(cnt)


solution()