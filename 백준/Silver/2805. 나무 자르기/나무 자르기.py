import sys
input = sys.stdin.readline


def solution():
    answer = 0
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))
    tree.sort()
    
    s, e = 1, tree[-1]
    while True:
        if s > e:
            answer = e
            break
            
        mid = (s + e) // 2
        
        tot = 0
        for t in tree:
            if t > mid:
                tot += t - mid
                
        if tot > M:
            s = mid + 1
        elif tot < M:
            e = mid - 1
        else:
            answer = mid
            break
    
    print(answer)   
            
            
solution()