import sys
input = sys.stdin.readline

def solution():
    answer = 0
    N = int(input())
    H = list(map(int, input().split()))
    
    for i in range(N - 1):
        h = abs(H[i] - H[i + 1])
        w = abs(H[i] + H[i + 1])
        answer += h**2 + w**2
    print(answer)
    
solution()