def solution(board, h, w):
    n = len(board)
    cnt = 0
    dh = [1, -1, 0, 0]
    dw = [0, 0, 1, -1]
    
    for i in range(4):
        if 0 <= h + dh[i] < n and 0 <= w + dw[i] < n:
            if board[h + dh[i]][w + dw[i]] == board[h][w]:
                cnt += 1
    
    return cnt