def DFS(n, computers, visited, s):
    visited[s] = True
    for i in range(n):
        if visited[i]:
            continue
        
        if computers[s][i]:
            DFS(n, computers, visited, i)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if not visited[i]:
            DFS(n, computers, visited, i)
            answer += 1
    
    return answer