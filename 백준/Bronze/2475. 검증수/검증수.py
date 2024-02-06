import sys

input = sys.stdin.readline

num_list = list(map(int, input().split()))
answer = 0

for num in num_list:
    answer += num**2

print(answer % 10)