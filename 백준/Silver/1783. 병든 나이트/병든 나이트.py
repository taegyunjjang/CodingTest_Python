import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    answer = 0
    if N == 1:
        answer = 1
    elif N == 2:
        if M < 3:
            answer = 1
        elif M < 5:
            answer = 2
        elif M < 7:
            answer = 3
        else:
            answer = 4
    else:
        if M == 1:
            answer = 1
        elif M == 2:
            answer = 2
        elif M == 3:
            answer = 3
        elif M < 7:
            answer = 4
        else:
            answer = M - 2
    print(answer)

solution()