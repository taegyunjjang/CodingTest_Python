def solution(keymap, targets):
    answer = []
    dic = {chr(ord('A') + i): 0 for i in range(26)}
    
    for key in keymap:
        for i in range(26):
            alp = chr(ord('A') + i)
            if alp in key:
                if dic[alp] == 0:
                    dic[alp] = key.index(alp) + 1
                else:
                    dic[alp] = min(key.index(alp) + 1, dic[alp])
    
    for t in targets:
        cnt = 0
        for i, ch in enumerate(t):
            if dic[ch] != 0:
                cnt += dic[ch]
            else:
                answer.append(-1)
                break
            if i == len(t) - 1:
                answer.append(cnt)
        
    return answer