import sys
from collections import Counter

input = sys.stdin.readline

def binary_search(target, L):
    left = 0
    right = len(L) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == target:
            return True
        elif L[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def solution():
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = list(map(int, input().split()))
    
    N_counter = Counter(N_list)
    L = list(N_counter.keys())
    L.sort()
    
    for m in M_list:
        if binary_search(m, L):
            print(N_counter[m], end=' ')
        else:
            print(0, end=' ')
        
solution()
