import sys
from collections import deque
input = sys.stdin.readline


def solution():
    dq = deque()
    N = int(input())
    dq.extend([i for i in range(1, N + 1)])
    while len(dq) != 1:
        dq.popleft()
        dq.append(dq.popleft())
    print(dq[0])
        
    
solution()
