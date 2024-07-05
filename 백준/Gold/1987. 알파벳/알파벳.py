import sys
input = sys.stdin.readline

 
def DFS(x, y, cnt):
    global answer
    answer = max(answer, cnt)
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if not visited[ord(graph[nx][ny]) - ord('A')]:
                visited[ord(graph[nx][ny]) - ord('A')] = 1
                DFS(nx, ny, cnt + 1)
                visited[ord(graph[nx][ny]) - ord('A')] = 0
             
global answer
answer = 1

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [0] * 26
visited[ord(graph[0][0]) - ord('A')] = 1

DFS(0, 0, 1)
print(answer)