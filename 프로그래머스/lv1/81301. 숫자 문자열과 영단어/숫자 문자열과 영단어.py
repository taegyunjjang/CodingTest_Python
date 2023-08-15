def solution(s):
    answer = ''
    tmp = ''
    for ch in s:
        if ch.isdigit():
            answer += ch
        else:
            tmp += ch
        
        if tmp == 'zero':
            answer += '0'
            tmp = ''
        elif tmp == 'one':
            answer += '1'
            tmp = ''
        elif tmp == 'two':
            answer += '2'
            tmp = ''
        elif tmp == 'three':
            answer += '3'
            tmp = ''
        elif tmp == 'four':
            answer += '4'
            tmp = ''
        elif tmp == 'five':
            answer += '5'
            tmp = ''
        elif tmp == 'six':
            answer += '6'
            tmp = ''
        elif tmp == 'seven':
            answer += '7'
            tmp = ''
        elif tmp == 'eight':
            answer += '8'
            tmp = ''
        elif tmp == 'nine':
            answer += '9'
            tmp = ''
    return int(answer)