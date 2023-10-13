def solution(s):
    stackList = []
    for ch in s:
        if ch == '(':
            stackList.append(ch)
        else:
            if len(stackList) == 0:
                return False
            stackList.pop()
    if len(stackList) == 0:
        return True
    else:
        return False