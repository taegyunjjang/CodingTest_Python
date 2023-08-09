def solution(common):
    n = len(common) + 1
    
    if common[1] - common[0] == common[-1] - common[-2]:
        return common[0] + (n - 1) * (common[1] - common[0])
    else:
        return common[0] * (common[1] // common[0]) ** (n - 1)