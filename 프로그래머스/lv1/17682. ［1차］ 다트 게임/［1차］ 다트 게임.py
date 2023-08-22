def solution(dartResult):
    answer = 0
    tmp = ''
    bonus = []
    
    for ch in dartResult:
        if ch.isdigit():
            tmp += ch
        else:
            if ch == 'S':
                bonus.append(int(tmp))
                tmp = ''
            elif ch == 'D':
                bonus.append(int(tmp) ** 2)
                tmp = ''
            elif ch == 'T':
                bonus.append(int(tmp) ** 3)
                tmp = ''
            elif ch == '*':
                if len(bonus) == 1:
                    bonus[-1] = bonus[-1] * 2
                else:
                    bonus[-2] = bonus[-2] * 2
                    bonus[-1] = bonus[-1] * 2
            else:
                bonus[-1] = bonus[-1] * (-1)
    answer = sum(bonus)
    return answer