import sys
input = sys.stdin.readline

def solution():
    answer = 0
    P, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    i = 0
    while P < 200 and i < N:
        P += A[i]
        i += 1
        answer += 1
        
    print(answer)

solution()