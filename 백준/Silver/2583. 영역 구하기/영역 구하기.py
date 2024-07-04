import sys
from collections import deque
input = sys.stdin.readline


def bfs(graph, s):
    cnt = 1
    graph[s[0]][s[1]] = 0
    
    M, N = len(graph), len(graph[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    dq = deque()
    dq.append(s)
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    dq.append((nx, ny))
                    cnt += 1
    return cnt
             
def solution():
    M, N, K = map(int, input().split())
    graph = [[1] * N for _ in range(M)]
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        y1 = M - y1
        y2 = M - y2 
        for i in range(y2, y1):
            for j in range(x1, x2):
                graph[i][j] = 0
    
    answer = 0
    area = []
    for i in range(M):
        for j in range(N):
            if graph[i][j]:
                answer += 1
                area.append(bfs(graph, (i, j)))
    
    print(answer)
    area.sort()
    print(*area)


solution()