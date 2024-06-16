import sys
from math import ceil
input = sys.stdin.readline


def solution():
    N = int(input())
    people = list(map(int, input().split()))
    T, P = map(int, input().split())
    
    cntT = 0    
    for num in people:
        cntT += ceil(num/T)
        
    print(cntT)
    print(f"{N//P} {N%P}")          
                    
solution()