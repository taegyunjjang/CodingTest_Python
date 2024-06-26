import sys
from collections import deque
input = sys.stdin.readline


def solution():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dic = {i:[] for i in range(N)}
    for i in range(N):
        visited = [False] * N
        dq= deque()
        dq.append(i)
        while dq:
            start = dq.popleft()
            for end in range(N):
                if graph[start][end]:
                    dic[i].append(end)
                    if not visited[end]:
                        visited[end] = True
                        dq.append(end)

    for i in range(N):
        for j in range(N):
            if j in dic[i]:
                graph[i][j] = 1
      
    for i in range(N):
        print(*graph[i])
    
            
solution()