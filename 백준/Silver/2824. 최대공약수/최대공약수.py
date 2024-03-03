from math import gcd
import sys
input = sys.stdin.readline

def solution():
    n, m = 1, 1
    N = int(input())
    for num in list(map(int, input().split())):
        n *= num
    M = int(input())
    for num in list(map(int, input().split())):
        m *= num
        
    answer = gcd(n, m)

    s = str(answer)
    l = len(s)
    if l > 9:
        print(s[l-9:])
    else:
        print(answer)

solution()