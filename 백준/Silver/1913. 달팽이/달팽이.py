import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    num = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 1
    is_stop = False

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    x = N//2; y = N//2
    arr[x][y] = cnt; cnt += 1
    
    while x != 0 and y != 0:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N and arr[new_x][new_y] == 0:
                arr[new_x][new_y] = cnt
                x = new_x; y = new_y
                cnt += 1
            else:
                while 0 <= x + dx[i] < N and 0 <= y + dy[i] < N and arr[x + dx[i]][y + dy[i]] != 0:
                    x += dx[i - 1]
                    y += dy[i - 1]
                    if x == 0 and y == 0:
                        is_stop = True
                        break
                    arr[x][y] = cnt
                    cnt += 1
                if is_stop:
                    break
                arr[x + dx[i]][y + dy[i]] = cnt
    arr[x][y] = N ** 2                        

    answer = []    
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
            if arr[i][j] == num:
                answer.append([i + 1, j + 1])
        print()
    print(*answer[0])  
     
solution()