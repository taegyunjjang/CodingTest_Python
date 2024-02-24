import sys

input = sys.stdin.readline

MAX = 1000000

def solution():
    answer = [0 for _ in range(MAX + 1)]
    divisor_list = [0 for _ in range(MAX + 1)]

    for i in range(1, MAX + 1):
        j = 1
        while i * j < MAX + 1:
            divisor_list[i * j] += i
            j += 1
        answer[i] = answer[i - 1] + divisor_list[i]

    T = int(input())
    for _ in range(T):
        num = int(input())
        print(answer[num])

solution()