import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    cnt = 99999
    
    for i in range(1, N//3 + 1):
        if (N - (3*i)) % 5 == 0:
            cnt = min(cnt, i + (N - (3*i))//5)
    
    for i in range(1, N//5 + 1):
        if (N -(5*i)) % 3 == 0:
            cnt = min(cnt, i + (N -(5*i))//3)
    
    if cnt == 99999:
        print(-1)
    else:
        print(cnt)
        
solution()