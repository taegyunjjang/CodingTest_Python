import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def is_empty(dic):
    for v in dic.values():
        if v:
            return False
    return True

def solution():
    N = int(input())
    for _ in range(N):
        T = int(input())
        min_heap = []
        max_heap = []
        dic = dict()
        
        for _ in range(T):
            op, n = input().split()
            n = int(n)
            
            if op == 'I':
                if n in dic:
                    dic[n] += 1
                else:
                    heappush(min_heap, n)
                    heappush(max_heap, -n)
                    dic[n] = 1
                    
            elif op == 'D':
                if not is_empty(dic):
                    if n == -1:
                        while min_heap and (min_heap[0] not in dic or dic[min_heap[0]] < 1):
                            top = heappop(min_heap)
                            if top in dic and dic[top] < 1:
                                del dic[top]
                        if min_heap:
                            dic[min_heap[0]] -= 1
                            if dic[min_heap[0]] == 0:
                                del dic[min_heap[0]]
                    else:
                        while max_heap and (-max_heap[0] not in dic or dic[-max_heap[0]] < 1):
                            top = heappop(max_heap)
                            if -top in dic and dic[-top] < 1:
                                del dic[-top]
                        if max_heap:
                            dic[-max_heap[0]] -= 1
                            if dic[-max_heap[0]] == 0:
                                del dic[-max_heap[0]]

        if is_empty(dic):
            print("EMPTY")
        else:
            while min_heap and (min_heap[0] not in dic or dic[min_heap[0]] < 1):
                heappop(min_heap)
            while max_heap and (-max_heap[0] not in dic or dic[-max_heap[0]] < 1):
                heappop(max_heap)
            print(-max_heap[0], min_heap[0])

solution()
