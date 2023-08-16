def solution(s):
    answer = []
    tmp = []
    for i, ch in enumerate(s):
        if ch not in tmp:
            answer.append(-1)
            tmp.append(ch)
        else:
            answer.append(s[0:i][::-1].index(ch) + 1)
    return answer