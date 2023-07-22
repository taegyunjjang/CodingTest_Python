def solution(binomial):
    bList = binomial.split()
    if bList[1] == '+':
        return int(bList[0]) + int(bList[2])
    elif bList[1] == '-':
        return int(bList[0]) - int(bList[2])
    else:
        return int(bList[0]) * int(bList[2])