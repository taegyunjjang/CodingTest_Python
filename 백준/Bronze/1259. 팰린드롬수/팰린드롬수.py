import sys
input = sys.stdin.readline


def solution():
    while True:
        str = input().rstrip()
        if str == '0':
            break
        
        idx = len(str) // 2
        if len(str) % 2 == 0:
            if str[:idx] == str[idx:][::-1]:
                print("yes")
            else:
                print("no")
        else:
            if str[:idx] == str[idx + 1:][::-1]:
                print("yes")
            else:
                print("no")
    
solution()
