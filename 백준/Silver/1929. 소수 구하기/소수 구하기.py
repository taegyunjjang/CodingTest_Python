import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def solution():
    M, N = map(int, input().split())
    for num in range(M, N + 1):
        if is_prime(num):
            print(num)
        
solution()