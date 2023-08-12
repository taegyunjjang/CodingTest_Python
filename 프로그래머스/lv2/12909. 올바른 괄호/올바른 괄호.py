def solution(s):
    tmp = []
    
    for str in s:
        if str == '(':
            tmp.append(str)
        else:
            if tmp != []:
                tmp.pop()
            else:
                tmp.append(str)

    return True if tmp == [] else False