import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def dfs(dic, visited, s):
    for next in dic[s]:
        if not visited[next]:
            visited[next] = s
            dfs(dic, visited, next)
    
def solution():
    N = int(input())
    dic = {i:[] for i in range(1, N + 1)}
    visited = [0] * (N + 1)

    for _ in range(N - 1):
        s, e = map(int, input().split())
        dic[s].append(e)
        dic[e].append(s)

    visited[1] = 1
    dfs(dic, visited, 1)
    
    for i in range(2, N + 1):
        print(visited[i])


solution()