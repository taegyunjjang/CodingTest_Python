import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
    
def find_min_cnt(arr, x, y):
    visited = [[False]*M for _ in range(N)]
    
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < N and 0 <= new_y < M:
                if arr[new_x][new_y] and not visited[new_x][new_y]:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    
                    arr[new_x][new_y] = arr[x][y] + 1
                    
    return arr[N - 1][M - 1]

def solution():
    arr = [list(map(int, list(i for i in input().rstrip()))) for _ in range(N)]
    
    print(find_min_cnt(arr, 0, 0))
    
solution()