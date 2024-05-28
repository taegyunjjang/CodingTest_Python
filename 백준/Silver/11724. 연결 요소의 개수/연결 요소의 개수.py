import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(start, graph, visited):
    visited[start] = True
    for v in graph[start]:
       if not visited[v]:
           DFS(v, graph, visited)

def solution():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [False] * (N + 1)
    answer = 0
    
    for start in range(1, N + 1):
        if not visited[start]:
            DFS(start, graph, visited)
            answer += 1
    print(answer)
            
        
solution()
