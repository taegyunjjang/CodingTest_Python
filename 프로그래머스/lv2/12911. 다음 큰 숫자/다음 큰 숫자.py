def solution(n):
    answer = n + 1
    while True:
        if bin(n)[2:].count('1') == bin(answer)[2:].count('1'):
            return answer
        else:
            answer += 1
