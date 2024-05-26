import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    physical = [list(map(int, input().split())) + [1] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            
            if physical[i][0] < physical[j][0] and physical[i][1] < physical[j][1]:
                physical[i][2] += 1
    
    for i in range(N):
        print(physical[i][2], end=' ')
    
        
solution()
