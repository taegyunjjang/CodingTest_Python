import sys
input = sys.stdin.readline


def binary_search(s, e, LAN, N):
    answer = 0
    if s > e:
        return -1
    
    mid = (s + e)//2
    cnt = sum(l//mid for l in LAN)
    
    if cnt < N:
        answer = binary_search(s, mid - 1, LAN, N)
    else:
        answer = max(mid, binary_search(mid + 1, e, LAN, N))
    
    return answer
    

def solution():
    K, N = map(int, input().split())
    LAN = [int(input()) for _ in range(K)]
    print(binary_search(1, max(LAN), LAN, N))
                        

solution()