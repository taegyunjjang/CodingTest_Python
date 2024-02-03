import sys

input = sys.stdin.readline
X = int(input())

n = 1
while True:
    if (n**2 - n + 2) // 2 <= X < (n**2 + n + 2) // 2:
        break
    n += 1

tmp = X - (n**2 - n + 2) // 2
if n % 2 == 0:
    print(f"{1 + tmp}/{n - tmp}")
else:
    print(f"{n - tmp}/{1 + tmp}")