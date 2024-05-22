import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    answer = 0
    for a in A:
        if a < 0:
            a *= -1
        answer += a
    print(2*answer)
        

solution()