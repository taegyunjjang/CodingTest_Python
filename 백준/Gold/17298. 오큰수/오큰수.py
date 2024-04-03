import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    L = list(map(int, input().split()))[::-1]
    s = []
    answer = []
    
    for l in L:
        if len(s) == 0:
            answer.append(-1)
            s.append(l)
        else:
            if s[-1] > l:
                answer.append(s[-1])
                s.append(l)
            else:
                while s[-1] <= l:
                    s.pop()
                    if len(s) == 0: break
                    
                if len(s) == 0:
                    answer.append(-1)
                    s.append(l)
                else:
                    answer.append(s[-1])
                    s.append(l)
    answer = answer[::-1]
    print(*answer)
    
solution()