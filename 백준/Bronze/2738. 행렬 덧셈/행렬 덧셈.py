import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(2*N):
        m_list = list(map(int, input().split()))
        for j in range(M):
            matrix[i % N][j] += m_list[j]
    
    for i in range(N):
        print(*matrix[i])
        
solution()