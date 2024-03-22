import sys
input = sys.stdin.readline


def solution():
    while True:
        S = input().rstrip()
        S = S.lower()
        if S == '#':
            break
        print(S.count('a') + S.count('e') + S.count('i') + S.count('o') + S.count('u'))
        
solution()