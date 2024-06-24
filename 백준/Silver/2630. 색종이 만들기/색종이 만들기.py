import sys
input = sys.stdin.readline

# 하얀색:0, 파란색:1

def is_divide(graph):
    N = len(graph)
    if N == 1:
        return False
    
    tmp = graph[0][0]
    for i in range(N):
        for j in range(N):
            if graph[i][j] != tmp:
                return True
            
    return False

def divide_paper(graph, N, li):
    if is_divide(graph):
        g1 = [row[:N//2] for row in graph[:N//2]]
        g2 = [row[N//2:] for row in graph[:N//2]]
        g3 = [row[:N//2] for row in graph[N//2:]]
        g4 = [row[N//2:] for row in graph[N//2:]]
        divide_paper(g1, N//2, li)
        divide_paper(g2, N//2, li)
        divide_paper(g3, N//2, li)
        divide_paper(g4, N//2, li)
    else:
        li[graph[0][0]] += 1

def solution():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = [0, 0]
    divide_paper(graph, N, answer)
    print(*answer, sep='\n')

            
solution()