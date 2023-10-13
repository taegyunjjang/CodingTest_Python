def solution(arr):
    l = len(arr)
    answer = []
    for i in range(l - 1):
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer