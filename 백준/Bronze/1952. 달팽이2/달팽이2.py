import sys
input = sys.stdin.readline

def solution():
    M, N = map(int, input().split())
    if N < M:
        print(2*(N - 1) + 1)
    else:
        print(2*(M - 1))

solution()