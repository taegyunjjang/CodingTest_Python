def solution(array):
    dic = {}
    s = set(array)
    max_count = 0
    cnt = 0
    
    for num in s:
        dic[num] = 0
        
    for e in array:
        dic[e] += 1
    
    for v in dic.values():
        if max_count < v:
            max_count = v
    
    for m in dic.values():
        if m == max_count:
            cnt += 1
    
    if len(array) == 1:
        return array[0]
    elif cnt == 1:
        for key in dic.keys():
            if dic[key] == max_count:
                return key
    else:
        return -1