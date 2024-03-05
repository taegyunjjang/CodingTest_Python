import sys
input = sys.stdin.readline

def solution():
    X = int(input())
    N = int(input())

    tot = 0
    for _ in range(N):
        a, b = map(int, input().split())
        tot += a * b
    
    if X == tot:
        print("Yes")
    else:
        print("No")

solution()