import sys
input = sys.stdin.readline

def solution():
    M, N = map(int, input().split())
    if M > N:
        print(2*(N - 1) + 1)
    else:
        print(2*(M - 1 ))
    
    x = 1; y = 1
    if M > N:
        if N % 2 == 0:
            x += N//2; y += N//2 - 1
        else:
            x += N//2 + (M - N); y += N//2
    else:
        if M % 2 == 0:
            x += M//2; y += M//2 - 1
        else:
            x += M//2; y += M//2 + (N - M)
    print(x, y)
     
solution()