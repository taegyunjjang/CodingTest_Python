import sys
input = sys.stdin.readline


def solution():
    dic = {chr(i+96):i for i in range(1, 27)}
    L = int(input())
    string = input().rstrip()
    
    H = 0
    for i, ch in enumerate(string):
        H += dic[ch] * (31**i)
    H %= 1234567891
    print(H)
                        
                    
solution()