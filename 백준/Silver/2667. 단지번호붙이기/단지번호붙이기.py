import sys
from collections import deque
input = sys.stdin.readline

def find_house(board, x, y, N):
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
            
            if 0 <= new_x < N and 0 <= new_y < N:
                if board[new_x][new_y] == 1:
                    dq.append((new_x, new_y))
                    board[new_x][new_y] = 0
                    cnt += 1
    
    return cnt
                    

def solution():
    N = int(input())
    answer = []
    board = [[int(i) for i in input().rstrip()] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                answer.append(find_house(board, i, j, N))
    
    answer.sort()         
    print(len(answer))
    print(*answer, sep='\n')
    
solution()