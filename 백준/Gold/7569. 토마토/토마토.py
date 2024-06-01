import sys
from collections import deque
input = sys.stdin.readline


def find_ripe_tomato(graph, M, N, H):
    li = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    li.append([i, j, k])
    return li

def solution():
    M, N, H = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    
    v = find_ripe_tomato(graph, M, N, H)  
    dq = deque()
    dq.extend(v)
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    dz = [-1, 1]
    
    while dq:
        z, x, y = dq.popleft()
        for k in range(2):
            nz = z + dz[k]
            if 0 <= nz < H and graph[nz][x][y] == 0:
                dq.append([nz, x, y])
                graph[nz][x][y] = graph[z][x][y] + 1
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[z][nx][ny] == 0:
                dq.append([z, nx, ny])
                graph[z][nx][ny] = graph[z][x][y] + 1
    
    answer = 0
    for i in range(H):
            for j in range(N):
                for k in range(M):
                    if graph[i][j][k] == 0:
                        print(-1)
                        return 0

                    answer = max(answer, graph[i][j][k])
    print(answer - 1)
                    
                    
solution()