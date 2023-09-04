def solution(s):
    cnt, delZero = 0, 0
    
    while s != '1':
        delZero += s.count('0')
        s = bin(len(s.replace('0','')))[2:]
        cnt += 1
    return [cnt, delZero]
        
    