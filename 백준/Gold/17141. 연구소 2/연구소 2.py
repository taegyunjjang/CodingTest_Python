import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def set_graph(graph, virus):
    new_graph = [row[:] for row in graph]
    N = len(new_graph)
    
    for i in range(N):
        for j in range(N):
            if new_graph[i][j] == 2 and [i, j] not in virus:
                new_graph[i][j] = 0
    return new_graph

def find_min_time(graph):
    N = len(graph)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    dq = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                dq.append([i, j])
                
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if graph[nx][ny] == 0:
                if graph[x][y] == 2:
                    graph[nx][ny] = -1
                else:
                    graph[nx][ny] = graph[x][y] - 1
                dq.append([nx, ny])
    
    answer = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                return -1
            
            if graph[i][j] < 0:
                answer = min(answer, graph[i][j])
    
    return -answer

def solution():
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    viruses = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                viruses.append([i, j])
    
    is_spread = False
    answer = float("inf")
    for virus in combinations(viruses, M):
        new_graph = set_graph(graph, virus)
        if find_min_time(new_graph) == -1:
            continue
        
        answer = min(answer, find_min_time(new_graph))
        is_spread = True
        
    if not is_spread:
        answer = -1
    print(answer)
    
    
solution()
