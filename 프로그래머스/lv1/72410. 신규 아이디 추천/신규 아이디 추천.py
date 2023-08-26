def solution(new_id):
    answer = ''
    
    for ch in new_id:
        if ch.isalpha():
            if ch.isupper():
                answer += ch.lower()
            else:
                answer += ch
        else:
            if ch.isdigit() or ch in ['-', '_', '.']:
                if ch == '.':
                    answer += ch
                    if len(answer) > 1 and answer[-2] == '.':
                        answer = answer[:-1]
                else:
                    answer += ch
    answer = answer.strip('.')

    if answer == '':
        answer += 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
        
    return answer