def solution(s):
    answer = ''
    isFirst = True
    s = s.lower()
    for ch in s:
        if isFirst and ch.isalpha() and ch != ' ':
            answer += ch.upper()
            isFirst = False
        else:
            answer += ch
            if ch == ' ':
                isFirst = True
            if ch.isdigit():
                isFirst = False
    return answer