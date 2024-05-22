import sys
input = sys.stdin.readline

def solution():
    answer = 0
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    A.sort(reverse=True)
    
    for coin in A:
        if K // coin:
            answer += K // coin
            K %= coin
    print(answer)
    
solution()