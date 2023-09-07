def solution(k, tangerine):
    answer = 1
    dic = {n : 0 for n in set(tangerine)}
    for num in tangerine:
        dic[num] += 1
    s = sorted(dic.values(), reverse=True)
    for i in s:
        if k <= i:
            return answer
        else:
            k -= i
            answer += 1
            
    return answer