import sys
input = sys.stdin.readline

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
def solution():
    n = int(input())
    print(fib(n))
    
solution()