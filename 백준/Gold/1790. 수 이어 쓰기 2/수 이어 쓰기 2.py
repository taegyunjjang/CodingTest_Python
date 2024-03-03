import sys
input = sys.stdin.readline

def solution():
    # 1~9 : 9, 9*1
    # 10~99 : 90, 90*2
    # 100~999 : 900, 900*3
    # ...
    N, k = map(int, input().split())

    # 수의 길이가 k보다 작을 때
    num_len = 0
    d, p = len(str(N)), 0
    for i in range(d - 1):
        p += 9 * (10**i) * (i + 1)
    num_len = p + d * (N - 10**(d - 1) + 1)
    
    if num_len < k:
        print(-1)
        exit()


    # k번째 자릿수(digit) 계산
    digit, pivot = 1, 0
    for i in range(10):
        pivot += 9 * (10**i) * (i + 1)
        if k <= pivot:
            pivot -= 9 * (10**i) * (i + 1)
            break
        digit += 1
    # print(f'digit={digit}, pivot={pivot}')

    # 몫과 나머지
    q = (k - pivot) // digit
    r = (k - pivot) % digit

    # k번째 자리의 수
    if r == 0:
        print(str(10**(digit - 1) + (q - 1))[-1])
    else:
        print(str(10**(digit - 1) + q)[r -1])

solution()