import sys

input = sys.stdin.readline
answer = [1, 1, 2, 2, 2, 8]

piece_list = list(map(int, input().split()))

for i in range(6):
    answer[i] -= piece_list[i]

print(*answer)