import sys
from collections import deque
input = sys.stdin.readline

def solution():
    M, N = map(int, input().split())
    answer = 0
    
    board = [list(map(int, input().split())) for _ in range(N)]
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    dq = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                dq.append((i, j))
    
    while dq:
        loops = len(dq)
        for i in range(loops):
            x, y = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                
                if board[nx][ny] != 0:
                    continue
                
                board[nx][ny] = 1
                dq.append((nx, ny))
        if dq:
            answer += 1
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                answer = -1
    print(answer)
            
        
solution()
