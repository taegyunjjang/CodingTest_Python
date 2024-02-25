import sys
input = sys.stdin.readline

def is_prime(N):
    m = int(N**0.5)
    if N == 1:
        return False
    if N == 2:
        return True
    if N % 2 == 0:
        return False
    
    for i in range(3, m + 1, 2):
        if N % i == 0:
            return False
    return True

def solution():
    N = input().rstrip()
    # 주어진 수가 소수가 아닐 때
    if not is_prime(int(N)):
        print("no")
# 1000000000000000
    # 주어진 수가 소수일 때
    else:
        if '3' in N or '4' in N or '7' in N:
            print("no")
        else:
            tmp = ''
            for num in N:
                if num == '6':
                    tmp = '9' + tmp
                elif num == '9':
                    tmp = '6' + tmp
                else:
                    tmp = num + tmp

            N = int(tmp)
            if is_prime(N):
                print("yes")
            else:
                print("no")
solution()