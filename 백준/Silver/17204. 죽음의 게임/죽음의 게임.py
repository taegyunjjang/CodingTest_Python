import sys

input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    pairs = [(i, int(input())) for i in range(N)]
    answer = 0

    idx = 0
    while True:
        # K에 도달하지 못하는 경우
        if answer > N:
            print(-1)
            break

        answer += 1
        target = pairs[idx][1]

        # 0번 인덱스에서 시작하여 K에 도달하는 경우
        if target == K:
            print(answer)
            break
        
        idx = target

solution()