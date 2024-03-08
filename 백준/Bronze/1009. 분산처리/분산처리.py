import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        a = a % 10
        
        dic = {2: [2, 4, 8, 6],
               3: [3, 9, 7, 1],
               7: [7, 9, 3, 1],
               8: [8, 4, 2, 6],
               4: [4, 6],
               9: [9, 1]}
        if a == 0:
            print(10)
        elif a == 1 or a == 5 or a == 6:
            print(a)
        elif a == 2 or a == 3 or a == 7 or a == 8:
            b = b % 4 - 1
            print(dic[a][b])
        else:
            b = b % 2 - 1
            print(dic[a][b])

solution()