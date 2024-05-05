import sys
input = sys.stdin.readline

def solution():
    A, B = [], []
    for _ in range(3):
        p, y, s = input().split()
        p, y = int(p), int(y)
        y = y % 100
        
        A.append(str(y))
        B.append((p, s))
        
    A.sort()
    B.sort(key=lambda x:-x[0])
    B = [b[1][0] for b in B]
    
    print(''.join(A))
    print(''.join(B))
    
solution()