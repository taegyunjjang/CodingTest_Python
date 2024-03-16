import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    visited = [[False for _ in range(100)] for _ in range(100)]
    
    answer = 0
    for _ in range(N):
        x, y = map(int, input().split())
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                if not visited[i][j]:
                    visited[i][j] = True
                    answer += 1
    print(answer)
    
solution()