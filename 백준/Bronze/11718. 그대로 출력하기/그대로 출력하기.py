import sys

input = sys.stdin.readline
answer = []

for _ in range(100):
    s = input()
    if s == '\n':
        break
    s = s.rstrip()
    answer.append(s)

answer_len = len(answer)
for i in range(answer_len):
    print(answer[i])