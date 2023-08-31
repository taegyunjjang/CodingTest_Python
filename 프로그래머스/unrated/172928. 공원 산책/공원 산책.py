def solution(park, routes):
    W, H = len(park[0]), len(park)
    idx = [0, 0]
    k = 0
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                idx = [i, j]
                break
                
    for r in routes:
        op, n = r.split()[0], int(r.split()[1])
        isCollide = False
        
        if op == 'E':
            # east
            for k in range(1, n + 1):
                if idx[1] + k < W:
                    if park[idx[0]][idx[1] + k] == 'X':
                        isCollide = True
                        break
                else:
                    isCollide = True
                    break
            if not isCollide:
                    idx[1] += n
                    
        elif op == 'W':
            # west
            for k in range(1, n + 1):
                if idx[1] - k >= 0:
                    if park[idx[0]][idx[1] - k] == 'X':
                        isCollide = True
                        break
                else:
                    isCollide = True
                    break
            if not isCollide:
                    idx[1] -= n
                    
        elif op == 'N':
            # north
            for k in range(1, n + 1):
                if idx[0] - k >= 0:
                    if park[idx[0] - k][idx[1]] == 'X':
                        isCollide = True
                        break
                else:
                    isCollide = True
                    break
            if not isCollide:
                    idx[0] -= n
                    
        else:
            # south
            for k in range(1, n + 1):
                if idx[0] + k < H:
                    if park[idx[0] + k][idx[1]] == 'X' or idx[0] + k >= H:
                        isCollide = True
                        break
                else:
                    isCollide = True
                    break
            if not isCollide:
                    idx[0] += n
    return idx