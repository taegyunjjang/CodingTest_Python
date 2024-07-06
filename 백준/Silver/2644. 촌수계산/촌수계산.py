import sys
input = sys.stdin.readline


def dfs(dic, a, b, visited):
    if a == b:
        return visited[b]
    
    for num in dic[a]:
        if not visited[num]:
            visited[num] = visited[a] + 1
            dfs(dic, num, b, visited)


def solution(): 
    N = int(input())
    a, b = map(int, input().split())
    M = int(input())
    
    dic = {(i + 1):[] for i in range(N)}
    visited = [0 for _ in range(N + 1)]
    for _ in range(M):
        p, c = map(int, input().split())
        dic[p].append(c)
        dic[c].append(p)

    dfs(dic, a, b, visited)
    if visited[b]:
        print(visited[b])
    else:
        print(-1)
    
    
solution()
# {1: [2, 3], 2: [1, 7, 8, 9], 3: [1], 4: [5, 6], 5: [4], 6: [4], 7: [2], 8: [2], 9: [2]}