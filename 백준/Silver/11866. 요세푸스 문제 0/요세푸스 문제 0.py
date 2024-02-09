import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
c_list = [i for i in range(1, N + 1)]

answer = []
q = deque(c_list)
while len(q):
    q.rotate(-K + 1)
    answer.append(q.popleft())
print("<", end="")
print(*answer, sep=", ", end="")
print(">")