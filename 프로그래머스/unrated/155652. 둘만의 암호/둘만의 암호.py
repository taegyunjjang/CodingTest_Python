def solution(s, skip, index):
    answer = ''
    alpList = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in skip]
    l = len(alpList)
    
    for ch in s:
        answer += alpList[(alpList.index(ch) + index) % l]
    return answer