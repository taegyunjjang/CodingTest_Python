def solution(citations):
    cList = [0 for _ in range(max(citations))]
    m = 0
    for c in citations:
        for i in range(c):
            cList[i] += 1
    
    for i, c in enumerate(cList):
        if (i + 1) <= c and (i + 1) > m:
            m = i + 1
    return m