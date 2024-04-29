import sys
from collections import deque
input = sys.stdin.readline

def find_earthworm(board, x, y):
    N, M = len(board), len(board[0])
    cnt = 1
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    dq = deque()
    dq.append((x, y))
    board[x][y] = 0
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0 <= new_x < N and 0 <= new_y < M:
                if board[new_x][new_y] == 1:
                    dq.append((new_x, new_y))
                    board[new_x][new_y] = 0
                    cnt += 1
    
    return cnt
                    

def solution():
    T = int(input())
    
    # 배추 심기
    for _ in range(T):
        answer = []
        M, N, K = map(int, input().split())
        board = [[0]*M for _ in range(N)]
        for _ in range(K):
            X, Y = map(int, input().split())
            board[Y][X] = 1
            
            
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    answer.append(find_earthworm(board, i, j))
    
        print(len(answer))       
        
solution()