def solution(name, yearning, photo):
    answer = []
    dic = {}
    
    for i, n in enumerate(name):
        dic[n] = yearning[i]
        
    for j in range(len(photo)):
        cnt = 0
        for photoName in photo[j]:
            if photoName in dic.keys():
                cnt += dic[photoName]
        answer.append(cnt)
    return answer