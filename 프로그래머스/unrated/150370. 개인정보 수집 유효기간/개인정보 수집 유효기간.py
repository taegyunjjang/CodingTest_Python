def isExpired(year, month, date, today):
    Y, M, D = map(int, today.split('.'))
    if Y > year:
        return True
    elif Y == year:
        if M > month:
            return True
        elif M == month:
            if D > date:
                return True

def solution(today, terms, privacies):
    answer = []
    dic = {}
    
    for i in range(len(terms)):
        ch, period = terms[i].split()[0], int(terms[i].split()[1])
        dic[ch] = period
    
    for j in range(len(privacies)):
        year, month, date = map(int, privacies[j][:-2].split('.'))
        y, m = dic[privacies[j][-1]] // 12, dic[privacies[j][-1]] % 12
        year += y
        month += m
        date -= 1
        if month > 12:
            year += month // 12
            month %= 12
            
        if isExpired(year, month, date, today):
            answer.append(j + 1)
    return answer