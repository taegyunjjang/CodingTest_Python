import sys
input = sys.stdin.readline


def solution():
    answer = 0
    N = int(input())
    for num in range(1, N):
        s = sum([int(i) for i in str(num)])
        if num + s == N:
            answer = num
            break
    print(answer)
  

solution()