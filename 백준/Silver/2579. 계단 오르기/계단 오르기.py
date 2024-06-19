import sys
input = sys.stdin.readline


def find_max_value(N, stairs, dp):
    if N == 1:
        return stairs[1]
    if N == 2:
        return stairs[1] + stairs[2]
    if N == 3:
        return max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    
    if dp[N]:
        return dp[N]
    
    dp[N] = max(find_max_value(N - 3, stairs, dp) + stairs[N - 1] + stairs[N], 
                 find_max_value(N - 2, stairs, dp) + stairs[N])
    
    return dp[N]


def solution():
    N = int(input())
    stairs = [0] + [int(input()) for _ in range(N)]
    dp = [0] * 301
    
    if N == 1:
        print(stairs[1])
    elif N == 2:
        print(stairs[1] + stairs[2])
    elif N == 3:
        print(max(stairs[1] + stairs[3], stairs[2] + stairs[3]))
    else:   
        print(find_max_value(N, stairs, dp))
    
    
solution()