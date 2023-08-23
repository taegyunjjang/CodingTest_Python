def solution(N, stages):
    answer = []
    failureRate = [0 for _ in range(N)]
    d = len(stages)
    
    for i in range(N):
        failureRate[i] = (stages.count(i + 1) / d, i + 1)
        d -= stages.count(i + 1)
        if d == 0:
            for j in range(i + 1, N):
                failureRate[j] = (0, j + 1)
            break
    failureRate.sort(reverse=True, key=lambda x: x[0])
    
    for j in range(N):
        answer.append(failureRate[j][1])
    return answer