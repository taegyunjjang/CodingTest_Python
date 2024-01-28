import sys

A, B = map(int, sys.stdin.readline().split())
tmp = max(A, B)
A = min(A, B)
B = tmp

if A == B:
    print(0)
else:
    print(B - A - 1)

for num in range(A + 1, B):
    print(num, end=' ')