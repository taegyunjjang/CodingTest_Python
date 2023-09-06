# 단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정
def solution(n,a,b):
    answer = 1
    a, b = min(a,b), max(a,b)
    while  a // 2 + a % 2 != b // 2 + b % 2:
        if a % 2 == 0:
            a /= 2
            if b % 2 == 0:
                b /= 2
                answer += 1
            else:
                b = b//2 + 1
                answer += 1
        else:
            a = a//2 + 1
            if b % 2 == 0:
                b /= 2
                answer += 1
            else:
                b = b//2 + 1
                answer += 1
    return answer