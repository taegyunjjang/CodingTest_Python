def isPrime(num):
    if num == 2:
        return True
    elif num == 3:
        return True
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
    return True

def solution(n, k):
    cnt = 0
    tmp = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        tmp += str(mod)
    tmpList = tmp[::-1].split('0')
    # 211020101011
    for t in tmpList:
        if t != '':
            if int(t) != 1 and isPrime(int(t)):
                cnt += 1
    
    return cnt