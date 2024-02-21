import sys
''' 시간 초과 코드
input = sys.stdin.readline
N = int(input())

routes = []
for _ in range(N):
    routes.append(list(map(int, input().split())))

min_distance = 9999
start = routes[0]
for i in range(1, N - 1):
    dist = 0

    for j in range(1, N):
        dx, dy = routes[j][0], routes[j][1] 
        if j != i:
            dist += abs(dx - start[0]) + abs(dy - start[1])
            start = [dx, dy]

    min_distance = min(min_distance, dist)
    start = routes[0]

print(min_distance)
'''

input = sys.stdin.readline
N = int(input())

routes = []
for _ in range(N):
    routes.append(list(map(int, input().split())))

distances = 0
for i in range(N - 1):
    distances += abs(routes[i+1][0] - routes[i][0]) + abs(routes[i+1][1] - routes[i][1])

answer = distances
for i in range(1, N - 1):
    prev = abs(routes[i][0] - routes[i-1][0]) + abs(routes[i][1] - routes[i-1][1])
    next = abs(routes[i][0] - routes[i+1][0]) + abs(routes[i][1] - routes[i+1][1])
    new = abs(routes[i+1][0] - routes[i-1][0]) + abs(routes[i+1][1] - routes[i-1][1])
    answer = min(answer, distances - (prev + next - new))

print(answer)