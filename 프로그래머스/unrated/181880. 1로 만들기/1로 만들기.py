def solution(num_list):
    cnt = 0
    tmp = [0 for _ in range(len(num_list))]
    isOne = False
    
    while(True):
        for i, num in enumerate(num_list):
            if num % 2 == 0:
                tmp[i] = num / 2
                cnt += 1
            elif num % 2 != 0 and num != 1:
                tmp[i] = (num - 1) / 2
                cnt += 1
            else:
                tmp[i] = num
                
        for num in tmp:
            if num != 1:
                isOne = False
                break
            else:
                isOne = True
            
        if isOne:
            break
        else:
            for i in range(len(num_list)):
                num_list[i] = tmp[i]
    return cnt
# [12, 4, 15, 1, 14]
# [6, 2, 7, 1, 7]
# [3, 1, 3, 1, 3]
# [1, 1, 1, 1, 1]