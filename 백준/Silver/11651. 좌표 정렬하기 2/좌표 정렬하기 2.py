import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    coord = [list(map(int, input().split())) for _ in range(N)]
    coord.sort(key=lambda x: (x[1], x[0]))
    
    for i in range(N):
        print(*coord[i])
    
solution()