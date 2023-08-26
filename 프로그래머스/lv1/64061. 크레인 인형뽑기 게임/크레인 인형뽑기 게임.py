def solution(board, moves):
    answer = 0
    basket = []
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m - 1] != 0:
                if len(basket) > 0 and basket[-1] == board[i][m - 1]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
    
    return answer