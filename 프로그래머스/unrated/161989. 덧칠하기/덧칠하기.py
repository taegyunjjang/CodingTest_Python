def solution(n, m, section):
    answer = 0
    paint = [1] * n
    for i in section:
        paint[i - 1] = 0
    
    j = 0
    while j < n:
        if paint[j] == 0:
            answer += 1
            j += m
        else:
            j += 1
    return answer