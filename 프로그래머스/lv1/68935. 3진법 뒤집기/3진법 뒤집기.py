def solution(n):
    tmp = ''
    answer = 0
    while n > 0:
        tmp += str(n % 3)
        n //= 3
    
    for i, ch in enumerate(tmp[::-1]):
        if ch != 0:
            answer += int(ch) * (3 ** i)
    return answer