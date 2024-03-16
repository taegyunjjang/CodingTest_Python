import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    A = [0 for _ in range(46)]
    A[1] = 1; A[2] = 1
    
    if n == 1:
        print(1)
    else:
        for i in range(3, n + 1):
            A[i] = A[i - 1] + A[i - 2]
        print(A[n])

solution()