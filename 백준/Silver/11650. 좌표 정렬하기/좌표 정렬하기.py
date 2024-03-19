import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    L.sort(key=lambda x: (x[0], x[1]))
    
    for l in L:
        print(*l)
    
solution()