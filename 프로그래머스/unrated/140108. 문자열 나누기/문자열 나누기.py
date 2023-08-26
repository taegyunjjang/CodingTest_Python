def solution(s):
    answer = []
    cntA, cntB = 0, 0
    tmp = ""
    flag = s[0]
    isSame = False
    
    for i, ch in enumerate(s):
        if isSame:
            flag = ch
            isSame = False
            
        if ch == flag:
            cntA += 1
            tmp += ch
        else:
            cntB += 1
            tmp += ch
        
        if cntA == cntB:
            answer.append(tmp)
            cntA, cntB = 0, 0
            isSame = True
            tmp = ""
    if tmp != "":
        answer.append(tmp)
    return len(answer)