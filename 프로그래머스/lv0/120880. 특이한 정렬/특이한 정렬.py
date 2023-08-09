def solution(numlist, n):
    dic = {}
    numlist.sort(reverse=True)
    
    for num in numlist:
        dic[num] = abs(num - n)
    
    answer = sorted(dic, key=lambda k: dic[k])
    return answer