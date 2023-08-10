def solution(board):
    n = len(board)
    answer = n ** 2
    cnt = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if 0 <= i + k < n and 0 <= j + l < n:
                            if board[i + k][j+ l] != 1:
                                board[i + k][j+ l] = 'X'
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 or board[i][j] == 'X':
                cnt += 1
    return answer - cnt