import sys

answer = 0
num_list = [0] * 10
N = list(sys.stdin.readline().rstrip())

for ch in N:
    ch = int(ch)
    num_list[ch] += 1

num_list[9] += num_list[6]
num_list[6] = 0
answer = max(max(num_list[:9]), num_list[9] // 2 + num_list[9] % 2)

print(answer)
