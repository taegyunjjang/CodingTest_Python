def comb(n, k):
    result = 1
    kFactorial = 1
    for i in range(n, n - k, -1):
        result *= i
    for j in range(2, k + 1):
        kFactorial *= j
    return result // kFactorial

def solution(n):
    cnt = 0
    k = 0
    while n >= k:
        cnt += comb(n, k)
        n -= 1
        k += 1
    return cnt % 1234567
# 111111
# 11112
# 1122
# 222
# 6C0 + 5C1 + 4C2 + 3C3 = 13