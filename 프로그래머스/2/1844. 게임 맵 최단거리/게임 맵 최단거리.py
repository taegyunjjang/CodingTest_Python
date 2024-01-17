def find_min_cnt(maps, visited, x, y, n, m):
    queue = [(x, y)]
    
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.pop(0)
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            # map을 벗어나는 경우
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                continue
            
            # 벽인 경우
            if maps[new_x][new_y] == 0:
                continue

            # 처음 방문하는 길
            if visited[new_x][new_y] == 0:
                visited[new_x][new_y] = visited[x][y] + 1
                queue.append((new_x, new_y))
            
def solution(maps):
    n, m = len(maps), len(maps[0])    
    x, y = 0, 0
    
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    
    find_min_cnt(maps, visited, x, y, n, m)
    
    if visited[n - 1][m - 1] == 0:
        return -1
    
    return visited[n - 1][m - 1]
           