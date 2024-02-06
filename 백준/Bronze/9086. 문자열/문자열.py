import sys

input = sys.stdin.readline

T = int(input())
answer = []

for _ in range(T):
    S = input().rstrip()
    if len(S) == 1:
        answer.append(S*2)
    else:
        answer.append(S[0] + S[-1])

for ch in answer:
    print(ch)