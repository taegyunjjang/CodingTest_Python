def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if max(n, m) % i == 0 and min(n, m) % i == 0:
            answer.append(i)
            answer.append(n * m // i)
            return answer