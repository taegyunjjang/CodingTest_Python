import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    S_list = []
    
    for _ in range(N):
        s = input().rstrip()
        if s not in S_list:
            S_list.append(s)
    
    S_list.sort(key=lambda x: (len(x), x))
    for s in S_list:
        print(s)
    
solution()