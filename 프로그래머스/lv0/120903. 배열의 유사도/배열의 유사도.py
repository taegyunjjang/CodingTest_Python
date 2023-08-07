def solution(s1, s2):
    answer = 0
    for str in s1:
        if str in s2:
            answer += 1
    return answer