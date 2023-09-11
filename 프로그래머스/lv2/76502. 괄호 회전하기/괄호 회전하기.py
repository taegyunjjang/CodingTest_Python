def isParenthesis(strList):
    l = len(strList)
    dic = {']': '[', '}': '{', ')': '('}
    stack = []
    for ch in strList:
        if ch in ['[', '{', '(']:
            stack.append(ch)
        else:
            if len(stack) == 0 or dic[ch] not in stack:
                return False
            else:
                stack.pop()
    if stack == []:
        return True
    else:
        return False

def solution(s):
    cnt = 0
    l = len(s)
    for i in range(l):
        if isParenthesis(s[i:] + s[:i]):
            cnt += 1
                
    
    return cnt