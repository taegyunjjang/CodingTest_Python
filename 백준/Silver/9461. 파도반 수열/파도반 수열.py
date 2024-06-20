import sys
input = sys.stdin.readline


def solution():
    T = int(input())
    dp = [0] * 101
    dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2
    
    for i in range(6, 101):
        dp[i] = dp[i - 1] + dp[i - 5]
        
    for _ in range(T):
        N = int(input())
        print(dp[N])
    
        
solution()