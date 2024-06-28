import sys
input = sys.stdin.readline


def solution():
    N, r, c = map(int, input().split())
    answer = 0
    while N:
        N -= 1
        tmp = (2**(N)) * (2**(N))
        # 제1사분면
        if r < 2**N and c >= 2**N:
            answer += tmp * 1
            c -= 2**N
        # 제2사분면
        elif r < 2**N and c < 2**N:
            answer += tmp * 0
        # 제3사분면
        elif r >= 2**N and c < 2**N:
            answer += tmp * 2
            r -= 2**N
        # 제4사분면
        else:
            answer += tmp * 3
            r -= 2**N
            c -= 2**N

    print(answer)
    
            
solution()