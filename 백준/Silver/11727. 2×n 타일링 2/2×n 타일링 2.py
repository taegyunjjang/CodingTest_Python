import sys
input = sys.stdin.readline

'''
dp[1] = 1
dp[2] = 3
dp[3] = 5
dp[4] = 11
dp[5] = 21

'''
def solution():
    N = int(input())
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 3
    for i in range(3, 1001):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
        
    print(dp[N] % 10007)
    
            
solution()