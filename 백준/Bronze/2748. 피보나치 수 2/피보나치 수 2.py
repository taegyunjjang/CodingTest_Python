import sys
input = sys.stdin.readline

def fib(n, li):
    if n <= 1 or li[n] != 0:
        return li[n]
    elif li[n] == 0:
        li[n] = fib(n - 1, li) + fib(n - 2, li)
        return li[n]

def solution():
    n = int(input())
    li = [0 for _ in range(n + 1)]
    li[1] = 1
    print(fib(n, li))

    
solution()