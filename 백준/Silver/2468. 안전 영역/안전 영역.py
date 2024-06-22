import sys
from collections import deque
input = sys.stdin.readline


def sinked_graph(graph, N, height):
    sinked_graph = [g[:] for g in graph]
    for i in range(N):
        for j in range(N):
            if sinked_graph[i][j] <= height:
                sinked_graph[i][j] = -1
    return sinked_graph

def find_unsinked_coordinate(graph, N):
    coord = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] != -1:
                coord.append([i, j])
    return coord

def find_safety_area(graph, N, coord):
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    dq = deque()
    for c in coord:
        if graph[c[0]][c[1]] == -1:
            continue
        
        cnt += 1
        dq.append(c)
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                
                if graph[nx][ny] != - 1:
                    graph[nx][ny] = -1
                    dq.append([nx, ny])
    return cnt     
    
def solution():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    s, e = 100, 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] < s:
                s = graph[i][j]
            if graph[i][j] > e:
                e = graph[i][j]

    answer = 1
    for h in range(s, e + 1):
        new_graph = sinked_graph(graph, N, h)
        unsinked_coord = find_unsinked_coordinate(new_graph, N)
        answer = max(answer, find_safety_area(new_graph, N, unsinked_coord))
        
    print(answer)
    
            
solution()