def solution(lottos, win_nums):
    cnt, zero = 0, 0
    dic = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    
    for num in lottos:
        if num in win_nums:
            cnt += 1
        if num == 0:
            zero += 1
        
    return [dic[cnt + zero], dic[cnt]]