import sys
input = sys.stdin.readline

def solution():
    answer = -1
    N = int(input())
    for i in range(5):
        if (N - 3*i) >= 0 and (N - 3*i) % 5 == 0:
            answer = i + (N - 3*i)//5
            break
    print(answer)
    
solution()