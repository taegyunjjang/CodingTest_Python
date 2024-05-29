import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def build_wall(graph, wall):
    new_graph = [row[:] for row in graph]
    for w in wall:
        x, y = w
        new_graph[x][y] = 1
        
    return new_graph

def find_max_safety_area(graph):
    N = len(graph)
    M = len(graph[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    dq = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                dq.append([i, j])
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                dq.append([nx, ny])
    
    cnt0 = 0
    for i in range(N):
        cnt0 += graph[i].count(0)
    
    return cnt0

def solution():
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    walls = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                walls.append([i, j])
    
    answer = 0
    for wall in combinations(walls, 3):
        new_graph = build_wall(graph, wall)
        answer = max(answer, find_max_safety_area(new_graph))
    print(answer)
    
solution()
