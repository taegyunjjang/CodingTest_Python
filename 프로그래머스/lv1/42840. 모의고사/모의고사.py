def solution(answers):
    answer = []
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    h1, h2, h3 = 0, 0, 0
    
    for i, num in enumerate(answers):
        if num == m1[i % len(m1)]:
            h1 += 1
        if num == m2[i % len(m2)]:
            h2 += 1
        if num == m3[i % len(m3)]:
            h3 += 1
    maxScore = max(h1, h2, h3)
    if maxScore == h1:
        answer.append(1)
    if maxScore == h2:
        answer.append(2)
    if maxScore == h3: 
        answer.append(3)
    return answer