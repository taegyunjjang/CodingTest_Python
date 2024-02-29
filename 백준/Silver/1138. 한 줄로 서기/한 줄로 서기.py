import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    num_list = list(map(int, input().split()))

    answer = [0 for _ in range(N)]
    for i, num in enumerate(num_list):
        if sum(answer[:num + 1]) == 0:
            answer[num] = i + 1
        else:
            cnt, j = 0, 0
            while cnt != num or answer[j] != 0:
                if answer[j] == 0:
                    cnt += 1
                j += 1
            answer[j] = i + 1
    print(*answer)

solution()