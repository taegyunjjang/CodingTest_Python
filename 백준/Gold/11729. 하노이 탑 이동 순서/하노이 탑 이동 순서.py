import sys
input = sys.stdin.readline

def hannoi(N, s, e, t):
    if N == 1:
        print(s, end =' ')
        print(e)
    else:
        hannoi(N - 1, s, t, e)
        hannoi(1, s, e, t)
        hannoi(N - 1, t, e, s)
    
def solution():
    N = int(input())
    print(2**N - 1)
    hannoi(N, 1, 3, 2)
            
solution()
