import sys

card_list = [i for i in range(1, 21)]

for _ in range(10):
    s, e = map(int, sys.stdin.readline().split())
    card_list[s - 1:e] = card_list[s - 1:e][::-1]

print(*card_list)