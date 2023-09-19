def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1List, s2List = [], []
    cnt = 0
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            s1List.append(str1[i:i + 2])
    for j in range(len(str2) - 1):
        if str2[j].isalpha() and str2[j + 1].isalpha():
            s2List.append(str2[j:j + 2])
            
    for ch in set(s1List):
        if ch in s2List:
            cnt += min(s2List.count(ch), s1List.count(ch))
            
    if (len(s1List) + len(s2List)) == cnt:
        return 65536
    else:
        return ((cnt / (len(s1List) + len(s2List) - cnt)) * 65536) // 1
    
    