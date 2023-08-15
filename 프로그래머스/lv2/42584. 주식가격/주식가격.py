def solution(prices):
    answer = []
    l = len(prices)
    isDescend = False
    
    for i in range(l):
        if i == l - 1:
            answer.append(0)
            break
        for j in range(i + 1, l):
            if prices[i] > prices[j]:
                answer.append(j - i)
                isDescend = True
                break
        
        if isDescend:
            isDescend = False
            continue
        else:
            answer.append(l - (i + 1))
    return answer