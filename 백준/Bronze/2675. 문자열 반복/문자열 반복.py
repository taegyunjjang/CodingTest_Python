import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        R, S = input().split()
        R = int(R)
        for ch in S:
            print(ch*R, end='')
        print()
        
solution()