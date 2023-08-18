def solution(n):
    answer = 0
    if n == 2 or n == 3:
        return 1
    elif n == 4:
        return 2
    else:
        answer += 2
        for i in range(5, n + 1, 2):
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    answer -= 1
                    break
            answer += 1
    return answer