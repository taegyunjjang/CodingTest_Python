import sys

S = sys.stdin.readline().rstrip()

alphabet_list = [0] * 26

for ch in S:
    alphabet_list[ord(ch) - 97] += 1

print(*alphabet_list)
