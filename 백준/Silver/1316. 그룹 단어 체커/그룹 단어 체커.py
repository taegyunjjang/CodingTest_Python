import sys

input = sys.stdin.readline
N = int(input())
answer = 0

for _ in range(N):
    S = input().rstrip()
    S_len = len(S)
    is_group_word = True
    tmp = []

    for i in range(S_len - 1):
        if S[i] != S[i + 1]:
            if S[i + 1] in tmp:
                is_group_word = False
                break
            tmp.append(S[i])

    if is_group_word:
        answer += 1

print(answer)

