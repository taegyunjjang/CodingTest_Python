import sys
input = sys.stdin.readline

def solution():
    answer = 0
    N = int(input())
    dist = list(map(int, input().split()))
    price = list(map(int, input().split()))
    
    tmp = price[0]
    for i in range(1, N - 1):
        if price[i] < tmp:
            answer += tmp * dist[i - 1]
            tmp = price[i]
        else:
            dist[i] += dist[i - 1] 
            
        if i == N - 2:
            answer += tmp * dist[i]
    print(answer)
    
solution()