def solution(s, n):
    answer = ''
    dic = {}
    
    # 'A' ~ 'Z' : 0 ~ 25, 'a' ~ 'z' : 26 ~ 51
    for i in range(26):
        dic[chr(65 + i)] = i
        dic[chr(97 + i)] = i + 26
    
    for ch in s:
        if ch.isupper():
            answer += chr((dic[ch] + n) % 26 + 65)
        elif ch.islower():
            answer += chr((dic[ch] + n) % 26 + 97)
        else:
            answer += ch
    return answer