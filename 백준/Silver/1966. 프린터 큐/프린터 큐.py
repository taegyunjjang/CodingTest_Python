from collections import deque
import sys
input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        order = 0
        N, M = map(int, input().split())
        l = list(map(int, input().split()))

        queue = deque()
        for i, num in enumerate(l):
            queue.append((num, i))

        max_q = sorted(queue, key=lambda x: -x[0])[0][0]
        while True:
            q = queue.popleft()
            if q[0] == max_q:
                order += 1
                if q[1] == M:
                    print(order)
                    break
                max_q = sorted(queue, key=lambda x: -x[0])[0][0]
            else:
                queue.append(q)

solution()