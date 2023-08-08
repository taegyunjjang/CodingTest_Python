def solution(n):
    for i in range(1001):
        if n == i ** 2:
            return 1
    return 2