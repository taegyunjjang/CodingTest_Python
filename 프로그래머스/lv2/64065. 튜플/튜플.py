def solution(s):
    answer = []
    dic = {}
    s = s.replace("},{", " ")
    l = s[2:len(s) - 2].split()
    # print(l)
    
    for i in l:
        dic[len(i.split(','))] = i.split(',')
    # print(dic)
    
    for j in range(len(l)):
        for k in dic[j + 1]:
            if int(k) not in answer:
                answer.append(int(k))
    return answer