import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        case = input().rstrip()
        answer = 0
        cnt = 0
        for ch in case:
            if ch == 'O':
                cnt += 1
            else:
                cnt = 0
            answer += cnt
        print(answer)
        
solution()