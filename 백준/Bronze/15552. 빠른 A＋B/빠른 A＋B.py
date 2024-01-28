import sys

T = int(sys.stdin.readline())

sum_list = []
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    sum_list.append(A + B)

for i in range(T):
    print(sum_list[i])