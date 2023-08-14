def solution(s):
    answer = []
    cnt = 0
    for ch in s:
        if ch.isalpha():
            cnt += 1
            if cnt % 2 != 0:
                answer.append(ch.upper())
            else:
                answer.append(ch.lower())
        else:
            cnt = 0
            answer.append(ch)
    
    return ''.join(answer)