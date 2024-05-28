import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    n = 0
    num = 1
    while N != n:
        num += 1
        if '666' in str(num):
            n += 1
    print(num)
    
    
solution()