def solution(arr):
    cnt = 0
    tmp = [0] * len(arr)
    while(True):
        for i, num in enumerate(arr):
            if num >= 50 and num % 2 == 0:
                tmp[i] = arr[i] / 2
            elif num < 50 and num % 2 != 0:
                tmp[i] = arr[i] * 2 + 1
            else:
                tmp[i] = arr[i]
        
        if tmp == arr:
            break
        cnt += 1
        for i in range(len(arr)):
            arr[i] = tmp[i]
    return cnt
        