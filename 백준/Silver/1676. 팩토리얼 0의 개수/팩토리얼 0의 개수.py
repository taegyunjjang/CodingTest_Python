import sys
input = sys.stdin.readline


def fact(n):
    tot = 1
    for i in range(1, n + 1):
        tot *= i
    return tot


def solution():
    N = int(input())
    tmp = fact(N)
    
    for i, num in enumerate(str(tmp)[::-1]):
        if num != '0':
            print(i)
            break
                        

solution()