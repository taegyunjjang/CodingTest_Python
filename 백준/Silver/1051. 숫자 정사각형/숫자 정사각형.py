import sys


input = sys.stdin.readline
N, M = map(int, input().split())
answer = 1
exit_loop = False

REC = [[] for _ in range(N)]
for i in range(N):
    REC[i] = [int(d) for d in input().rstrip()]

# size를 줄여가며 완전 탐색
sizes = min(N, M)
for size in range(sizes, 0, -1):
    if exit_loop:
        break

    dx = size - 1
    H, W = N - dx, M - dx
    for h in range(H):
        for w in range(W):
            if REC[h][w] == REC[h+dx][w] == REC[h][w+dx] == REC[h+dx][w+dx]:
                answer = size**2
                exit_loop = True

print(answer)