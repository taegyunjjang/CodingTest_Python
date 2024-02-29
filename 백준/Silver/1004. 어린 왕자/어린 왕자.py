import sys
input = sys.stdin.readline

def isin_circle(x, y, r, x1, y1):
    d = (x1 - x)**2 + (y1 - y)**2
    if d < r**2:
        return True
    return False

def solution():
    T = int(input())
    for _ in range(T):
        cnt = 0
        x1, y1, x2, y2 = map(int, input().split())

        n = int(input())
        for _ in range(n):
            x, y, r = map(int, input().split())
            if isin_circle(x, y, r, x1, y1) and not isin_circle(x, y, r, x2, y2):
                cnt += 1
            elif not isin_circle(x, y, r, x1, y1) and isin_circle(x, y, r, x2, y2):
                cnt += 1
        print(cnt)

solution()