import sys
input = sys.stdin.readline


def is_right_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False

def solution():
    while True:
        L = list(map(int, input().split()))
        if L == [0, 0, 0]:
            break
        
        L.sort()
        if is_right_triangle(L[0], L[1], L[2]):
            print("right")
        else:
            print("wrong")    
        
solution()