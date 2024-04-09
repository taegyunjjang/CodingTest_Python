import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N = int(input())
    E = int(input())
    answer = 0
    
    visited = [False]*(N + 1)
    
    graph = {i:[] for i in range(1, N + 1)}
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque()
    q.append(1)
    while q:
        front = q.popleft()
        visited[front] = True
        
        for node in graph[front]:
            if not visited[node]:
                visited[node] = True
                answer += 1
                q.append(node)

    print(answer)
    
solution()