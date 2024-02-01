import sys

answer = 0

N, K = map(int, sys.stdin.readline().split())

female_cnt = {i:0 for i in range(1, 7)}
male_cnt = {i:0 for i in range(1, 7)}

for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    if S:
        male_cnt[Y] += 1
    else:
        female_cnt[Y] += 1

for key, value in female_cnt.items():
    answer += (value // K) if value % K == 0 else (value // K + 1)

for key, value in male_cnt.items():
    answer += (value // K) if value % K == 0 else (value // K + 1)

print(answer)