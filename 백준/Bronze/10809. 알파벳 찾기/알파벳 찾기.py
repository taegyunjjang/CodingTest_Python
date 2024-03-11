import sys
input = sys.stdin.readline

def solution():
    S = input().rstrip()
    answer = [S.index(chr(i)) if chr(i) in S else -1 for i in range(97, 123)]
    print(*answer)
    
solution()