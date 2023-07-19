def solution(arr):
    for i, num in enumerate(arr):
        if num >= 50 and num % 2 == 0:
            arr[i] = arr[i] / 2
        elif num < 50 and num % 2 != 0:
            arr[i] = arr[i] * 2
    return arr