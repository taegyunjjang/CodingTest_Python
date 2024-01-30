import sys

answer = 0
n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

s, e = 0, n - 1
sequence.sort()

while s < e:
    if sequence[s] + sequence[e] == x:
        answer += 1
        s += 1
        e -= 1
    elif sequence[s] + sequence[e] > x:
        e -= 1
    else:
        s += 1

print(answer)