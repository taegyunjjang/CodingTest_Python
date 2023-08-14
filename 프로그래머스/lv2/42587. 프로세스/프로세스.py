def solution(priorities, location):
    answer = [0 for _ in range(len(priorities))]
    tmp = []
    p = 1
    
    for i in range(len(priorities)):
        tmp.append(priorities[i])
    while True:
        for i, num in enumerate(priorities):
            if num == max(tmp):
                answer[i] = p
                p += 1
                tmp[i] = 0
        if p > len(priorities):
            return answer[location]