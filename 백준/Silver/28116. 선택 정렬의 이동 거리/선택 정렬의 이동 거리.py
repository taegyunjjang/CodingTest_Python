import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    answer = {i:0 for i in range(1, N + 1)}
    location = {}
    for i in range(N):
        location[A[i]] = i

    i = 0
    while i < N:
        if A[i] != i + 1:
            loc = location[i + 1]
            location[A[i]], location[A[loc]] = loc, i
            A[i], A[loc] = A[loc], A[i]

            d = loc - i
            answer[A[i]] += d; answer[A[loc]] += d
        i += 1

    for i in range(N):
        print(answer[i + 1], end=' ')

solution()