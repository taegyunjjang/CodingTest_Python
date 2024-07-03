import sys
from collections import deque
input = sys.stdin.readline

    
def bfs(graph, visited, s):
    I = len(graph)
    dx = [-1, -1, -2, -2, 1, 1, 2, 2]
    dy = [-2, 2, -1, 1, -2, 2, -1, 1]
    
    dq = deque()
    dq.append(s)
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            
            if graph[nx][ny] == -1:
                graph[nx][ny] = graph[x][y] + 1
                return
            
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                dq.append([nx, ny])
    
def solution():
    T = int(input())
    for _ in range(T):
        I = int(input())
        graph = [[0] * I for _ in range(I)]
        visited = [[False] * I for _ in range(I)]
        s = list(map(int, input().split()))
        e = list(map(int, input().split()))
        graph[e[0]][e[1]] = -1
        
        if s == e:
            print(0)
            continue
        
        bfs(graph, visited, s)
        print(graph[e[0]][e[1]])


solution()