import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    figure = [list(map(int, input().split())) for _ in range(N)]

    side1 = N * M

    side2 = 0
    for i in range(N):
        side2 += figure[i][0]
        for j in range(M - 1):
            if figure[i][j+1] > figure[i][j]:
                side2 += figure[i][j+1] - figure[i][j]

    side3 = 0
    for i in range(M):
        side3 += figure[0][i]
        for j in range(N - 1):
            if figure[j+1][i] > figure[j][i]:
                side3 += figure[j+1][i] - figure[j][i]

    answer = 2 * (side1 + side2 + side3)
    print(answer)
    
solution()