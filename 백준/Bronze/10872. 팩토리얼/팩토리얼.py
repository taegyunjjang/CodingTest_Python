import sys

input = sys.stdin.readline
N = int(input())
answer = 1

for i in range(1, N + 1):
    answer *= i

if N == 0:
    print(1)
else:
    print(answer)