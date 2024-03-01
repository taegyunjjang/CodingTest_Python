import sys
input = sys.stdin.readline

def solution():
    R, C = map(int, input().split())
    MAP = [[ch for ch in input().rstrip()] for _ in range(R)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    sea_list, land_list = [], []
    for x in range(R):
        for y in range(C):
            cnt = 0
            if MAP[x][y] == 'X':
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]

                    # 지도를 벗어남
                    if new_x < 0 or new_x >= R or new_y < 0 or new_y >= C:
                        cnt += 1
                    # 인접한 칸이 바다
                    elif MAP[new_x][new_y] == '.':
                        cnt += 1

                # 인접한 세 칸 또는 네칸이 바다        
                if cnt >= 3:
                    sea_list.append((x, y))
                else:
                    land_list.append((x, y))

    for sea in sea_list:
        MAP[sea[0]][sea[1]] = '.'

    min_row = land_list[0][0]
    max_row = land_list[-1][0]

    land_list.sort(key=lambda x: x[1])
    min_col = land_list[0][1]
    max_col = land_list[-1][1]

    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            print(MAP[i][j], end='')
        print()
    
solution()