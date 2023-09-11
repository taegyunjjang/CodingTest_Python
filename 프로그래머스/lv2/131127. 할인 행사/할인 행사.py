def solution(want, number, discount):
    answer = 0
    dic = {}
    isCorrect = False
    
    for w, num in zip(want, number):
        dic[w] = num
    for i in range(len(discount) - 9):
        for w in want:
            if discount[i:i + 10].count(w) >= dic[w]:
                isCorrect = True
            else:
                isCorrect = False
                break
        if isCorrect:
            answer += 1
            
    return answer