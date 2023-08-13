def solution(progresses, speeds):
    answer = []
    cmp = []
    l = len(progresses)
    tot = 1
    for i in range(l):
        if (100 - progresses[i]) % speeds[i] == 0:
            cmp.append((100 - progresses[i]) // speeds[i])
        else:
            cmp.append(((100 - progresses[i]) // speeds[i]) + 1)
    
    # [7, 3, 9] -> [2, 1]
    # [5, 10, 1, 1, 20, 1] -> [1, 3, 2]        
    j = 1
    M = cmp[0]
    while j != l:
        if M >= cmp[j]:
            tot += 1
            j += 1
        else:
            answer.append(tot)
            tot = 1
            M = cmp[j]
            j += 1
    answer.append(tot)
            
    return answer
