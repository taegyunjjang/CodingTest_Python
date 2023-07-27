def solution(date1, date2):
    isBig = True
    for i in range(3):
        if date1[i] > date2[i]:
            return 0
        elif date1[i] < date2[i]:
            return 1
        else:
            continue
    return 0