def solution(picture, k):
    row = ""
    rtn = []
    for i in range(len(picture)):
        for j in picture[i]:
            row += j * k
        for _ in range(k):
            rtn.append(row)
        row = ""
    return rtn