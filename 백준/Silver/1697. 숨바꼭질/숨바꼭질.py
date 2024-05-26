import sys
from collections import deque
input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    dq = deque()
    dq.append((N, 0))
    
    M = 100000
    visited = [False] * (M + 1)
    answer = 0
    
    while dq:
        x = dq.popleft()
        if x[0] == K:
            answer = x[1]
            break
        
        cnt = x[1] + 1
        if 0 <= x[0] * 2 <= M and not visited[x[0] * 2]:
            dq.append((x[0] * 2, cnt))
            visited[x[0] * 2] = True
        if 0 <= x[0] + 1 <= M and not visited[x[0] + 1]:
            dq.append((x[0] + 1, cnt))
            visited[x[0] + 1] = True
        if 0 <= x[0] - 1 <= M and not visited[x[0] - 1]:
            dq.append((x[0] - 1, cnt))
            visited[x[0] - 1] = True
    print(answer)
    
        
solution()
