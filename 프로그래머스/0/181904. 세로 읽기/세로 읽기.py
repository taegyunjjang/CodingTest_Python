def solution(st, m, c):
    temp = []
    answer = ''
    x = int(len(st)/m)
    for i in range(x):
        temp.append(st[i*m:(i+1)*m])
        answer += temp[i][c-1]
    return answer