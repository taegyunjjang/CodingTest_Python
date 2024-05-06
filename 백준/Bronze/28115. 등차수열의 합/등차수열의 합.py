import sys
input = sys.stdin.readline

def is_arithmetic_sequence(A):
    N = len(A)    
    
    if N <= 2:
        return True
    
    tmp = A[1] - A[0]
    for i in range(1, N - 1):
        if A[i + 1] - A[i] != tmp:
            return False
        
    return True

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    
    if is_arithmetic_sequence(A):
        print("YES")
        print(*[0 for _ in range(N)])
        print(*A)
    else:
        print("NO")
        
        
solution()