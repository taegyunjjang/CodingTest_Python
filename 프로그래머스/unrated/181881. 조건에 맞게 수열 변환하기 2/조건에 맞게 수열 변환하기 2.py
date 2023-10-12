def solution(arr):
    cnt = 0
    
    while True:
        isChange = False
        for i, num in enumerate(arr):
            if num >= 50 and num % 2 == 0:
                arr[i] = num // 2
                isChange = True
            elif num < 50 and num % 2 != 0:
                arr[i] = num * 2 + 1
                isChange = True
        if isChange:
            cnt += 1
        else:
            return cnt
        
        