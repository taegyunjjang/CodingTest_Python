import sys
input = sys.stdin.readline

def factorial(n):
    tot = 1
    for i in range(1, n + 1):
        tot *= i
    return tot

def solution():
    n, k = map(int, input().split())
    print(factorial(n)//(factorial(n - k)*factorial(k)))
    
solution()