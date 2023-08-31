def solution(players, callings):
    dicA = {}
    dicB = {}
    for i, p in enumerate(players):
        dicA[p] = i
        dicB[i] = p
    
    for c in callings:
        dicA[c] -= 1
        tmp = dicB[dicA[c]]
        dicA[tmp] += 1
        dicB[dicA[c]] = c
        dicB[dicA[c] + 1] = tmp
    
    return list(dicB.values())
