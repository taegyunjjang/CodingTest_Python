import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    member = [list(input().split()) + [i] for i in range(N)]
    member.sort(key=lambda x: (int(x[0]), x[2]))       
    
    for mem in member:
        print(*mem[:2])
        
solution()