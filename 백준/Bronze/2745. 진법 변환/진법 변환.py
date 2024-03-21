import sys
input = sys.stdin.readline


def solution():
    N, B = input().split()
    B = int(B)
    print(int(N, B))
        
solution()