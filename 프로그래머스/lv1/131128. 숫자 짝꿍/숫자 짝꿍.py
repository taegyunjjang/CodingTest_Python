def solution(X, Y):
    tmp = ''
    for i in range(9, -1, -1):
        x, y = X.count(str(i)), Y.count(str(i))
        if x * y != 0:
            tmp += str(i) * (min(x, y))
            if tmp[0] == '0':
                return "0"
    if tmp == '':
        return "-1"
    else:
        return tmp
