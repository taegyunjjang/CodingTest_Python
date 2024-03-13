from itertools import combinations
import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    
    answer = 0
    for c in combinations(num_list, 3):
        tot = sum(c)
        
        if tot == M:
            answer = tot
            break
        elif tot < M:
            if answer < tot:
                answer = tot
    print(answer)    
        
solution()