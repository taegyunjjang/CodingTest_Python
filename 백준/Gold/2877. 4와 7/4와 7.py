import sys
input = sys.stdin.readline

def solution():
    K = int(input())
    
    # digit : 자릿수
    digit = 0
    pivot = 1

    while K >= pivot:
        digit += 1
        pivot += 2**digit
    

    idx_list = []
    idx = 0

    n = K - (2**digit - 1)
    while n > 0:
        if n % 2 == 1:
            idx_list.append(idx)
        idx += 1
        n //= 2

    s = ['4'] * digit
    for i in idx_list:
        s[digit - i - 1] = '7'

    print(int(''.join(s)))
    
solution()