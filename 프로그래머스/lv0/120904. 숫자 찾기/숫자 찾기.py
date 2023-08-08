def solution(num, k):
    for i in range(len(str(num))):
        if str(k) == str(num)[i]:
            return i + 1
    return -1