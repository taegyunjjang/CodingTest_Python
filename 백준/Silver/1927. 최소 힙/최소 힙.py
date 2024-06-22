import sys
from heapq import heappush,heappop
input = sys.stdin.readline


def solution():
    N = int(input())
    heap = []
    for _ in range(N):
        n = int(input())
        if n:
            heappush(heap, n)
        else:
            if heap:
                print(heappop(heap))
            else:
                print(0)
    
            
solution()