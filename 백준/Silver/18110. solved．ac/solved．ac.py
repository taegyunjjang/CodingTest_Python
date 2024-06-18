import sys
input = sys.stdin.readline


def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)


def solution():
    N = int(input())
    if N:
        A = [int(input()) for _ in range(N)]
        A.sort()
        n = my_round(N * 0.15)
        if n:
            A = A[n:-n]
        print(my_round(sum(A)/len(A))) 
    else:
        print(0)
                        

solution()