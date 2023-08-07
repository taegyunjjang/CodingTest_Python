def solution(score):
    answer = []
    eList = []
    dic = {}
    
    for s in score:
        eList.append((s[0] + s[1]) / 2)
    newList = reversed(sorted(eList))
    
    for i, num in enumerate(newList):
        if num in dic.keys():
            continue
        else:
            dic[num] = i + 1
            
    for num in eList:
        answer.append(dic[num])
        
    return answer
        
    