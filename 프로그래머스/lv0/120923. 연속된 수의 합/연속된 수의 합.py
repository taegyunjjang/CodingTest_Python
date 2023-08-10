def solution(num, total):
    if num % 2 != 0:
        start = total // num - num // 2
    else:
        flag = total // (num // 2)
        start = (flag - num + 1) // 2
    return [i for i in range(start, start + num)]
        