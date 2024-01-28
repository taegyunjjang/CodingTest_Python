import sys

N = int(sys.stdin.readline())

for i in range(N):
    print(' ' * i, end='')
    print('*' * (N - i))