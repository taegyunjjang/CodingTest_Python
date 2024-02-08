import sys

input = sys.stdin.readline
N = int(input())
cnt = 1

if N < 10:
    new_N = N * 11
else:
    s = str(N)
    new_N = int(s[1] + str(int(s[0]) + int(s[1]))[-1])

while N != new_N:
    if new_N < 10 or str(new_N)[-1] == 1:
        new_N = int(str(new_N)[-1]) * 11
    else:
        s = str(new_N)
        new_N = int(s[1] + str(int(s[0]) + int(s[1]))[-1])
    cnt += 1
    
print(cnt)
