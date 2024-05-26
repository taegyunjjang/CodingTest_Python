import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    board = [[ch for ch in input().rstrip()] for _ in range(N)]
    
    answer = 64
    for i in range(N - 7):
        for j in range(M - 7):
            start_w, start_b = 0, 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if k % 2 == 0 and l % 2 == 0:
                        if board[k][l] != 'W':
                            start_w += 1
                        else:
                            start_b += 1
                    elif k % 2 == 0 and l % 2 != 0:
                        if board[k][l] != 'B':
                            start_w += 1
                        else:
                            start_b += 1
                    elif k % 2 != 0 and l % 2 != 0:
                        if board[k][l] != 'W':
                            start_w += 1
                        else:
                            start_b += 1
                    elif k % 2 != 0 and l % 2 == 0:
                        if board[k][l] != 'B':
                            start_w += 1
                        else:
                            start_b += 1
            # print(f"start_w, start_b = {start_w, start_b}")
            answer = min(answer, min(start_b, start_w))  
    print(answer)
    
    
solution()
