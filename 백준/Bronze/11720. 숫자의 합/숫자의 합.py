import sys

input = sys.stdin.readline
N = int(input())
number = input().rstrip()
answer = 0

for num in number:
    answer += int(num)

print(answer)