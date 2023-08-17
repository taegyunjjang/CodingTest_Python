def solution(a, b, n):
    answer = 0
    tmp = 0
    while n >= a:
        answer += n // a * b
        if n % a != 0:
            tmp += n % a
        n = n // a * b + tmp
        tmp = 0
    return answer



