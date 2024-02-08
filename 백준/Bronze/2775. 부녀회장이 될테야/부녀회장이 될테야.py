import sys


apartment =[[i for i in range(1, 15)] for _ in range(15)] 

for i in range(1, 15):
    for j in range(1, 14):
        apartment[i][j] = apartment[i-1][j] + apartment[i][j - 1]

input = sys.stdin.readline
T = int(input())
answer = []

for _ in range(T):
    floor = int(input())
    room = int(input()) - 1
    answer.append(apartment[floor][room])

for num in answer:
    print(num)

