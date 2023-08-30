def solution(wallpaper):
    x = []
    y = []
    
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            x.append(i)
            for j in range(len(wallpaper[i])):
                if wallpaper[i][j] == '#':
                    y.append(j)
            
    return [x[0], min(y), x[-1] + 1, max(y) + 1]