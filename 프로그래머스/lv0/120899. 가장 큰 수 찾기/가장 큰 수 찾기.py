def solution(array):
    answer = []
    for i, num in enumerate(array):
        if num == max(array):
            return [num, i]
