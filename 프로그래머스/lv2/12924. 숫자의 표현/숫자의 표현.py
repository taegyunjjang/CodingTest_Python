def solution(n):
    cnt = 0
    if n % 2 == 0 or n == 1:
        cnt = 1
    else:
        cnt = 2
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            cnt += 1
    for i in range(4, n, 2):
        rest = n % i
        if n // 2 > rest:
            break
        elif rest == i // 2:
            cnt += 1
    return cnt
    # cnt = 0
    # nList = [i for i in range(1, n + 1)]
    # for i in range(n - 1):
    #     for j in range(1, n - i - 1):
    #         if sum(nList[i:i + j]) == n:
    #             cnt += 1
    # return cnt

    # [1,2,3,4,5]
    # 36
    # 1, 2, 3, 4, 6, 9, 12, 18, 36
    # 36, 111213 78910