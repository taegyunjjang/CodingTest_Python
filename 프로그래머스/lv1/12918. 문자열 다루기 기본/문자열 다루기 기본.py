def solution(s):
    if len(s) == 4 or len(s) == 6:
        for ch in s:
            if ch.isdigit():
                print(ch)
                continue
            else:
                return False
        return True
    else:
        return False