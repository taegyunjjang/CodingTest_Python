import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    print(abs(N - M))
    
solution()