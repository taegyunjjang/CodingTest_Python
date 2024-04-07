import sys
from collections import deque
input = sys.stdin.readline

def DFS(visited, edge, s):
    print(s, end=' ')
    for e in edge[s]:
        if not visited[e]:
            visited[e] = True
            DFS(visited, edge, e)
    
def BFS(visited, edge, s, dq):
    dq.append(s)
    while dq:
        front = dq[0]
        print(front, end=' ')
        dq.popleft()
        
        for e in edge[front]:
            if not visited[e]:
                visited[e] = True
                dq.append(e)

def solution():
    N, M, s = map(int, input().split())
    
    dq = deque()
    
    visited = [False for _ in range(N + 1)]
    visited[s] = True
    
    edge = {i:[] for i in range(1, N + 1)}
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
    
    for i in range(1, N + 1):
        edge[i].sort()
    
    # DFS
    DFS(visited, edge, s)
    print()
        
    # BFS
    visited = [False for _ in range(N + 1)]
    visited[s] = True
    BFS(visited, edge, s, dq)
    
solution()