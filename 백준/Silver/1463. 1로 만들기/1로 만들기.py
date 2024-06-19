import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    dp = [0] * 1000001
    
    for i in range(2, N + 1):
        if i % 3 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i//3] + 1)
        if i % 2 == 0:
            if dp[i]:
                dp[i] = min(dp[i - 1] + 1, dp[i//2] + 1, dp[i])
            else:
                dp[i] = min(dp[i - 1] + 1, dp[i//2] + 1)
        if i % 3 != 0 and i % 2 != 0:
            if dp[i]:
                dp[i] = min(dp[i - 1] + 1, dp[i])
            else:
                dp[i] = dp[i - 1] + 1
                
    print(dp[N])
    
    
solution()