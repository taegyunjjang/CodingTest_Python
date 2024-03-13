import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    
    i = 0; pivot = 1
    while True:
        if N <= pivot:
            print(i + 1)
            break
        i += 1
        pivot += 6*i
        
solution()