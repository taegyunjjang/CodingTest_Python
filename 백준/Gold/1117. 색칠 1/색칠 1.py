import sys
input = sys.stdin.readline

def solution():
    W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

    area, x = 0, 0
    # x축 대칭 부분의 넓이가 더 작을 때
    if W//2 >= f:
        if x1 < f < x2:
            x = (x2 - x1) + (f - x1)
        elif x2 <= f:
            x = 2 * (x2 - x1)
        else:
            x = (x2 - x1)
    # x축 대칭 부분의 넓이가 더 클 때
    else:
        if x1 < (W - f) < x2:
            x = (x2 - x1) + ((W - f) - x1)
        elif x2 <= (W - f):
            x = 2 * (x2 - x1)
        else:
            x = (x2 - x1)
            
    area = W * H - (x * (y2 - y1) * (c + 1))
    print(area)
    
solution()