import sys


input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
reversed_list = num_list[::-1]
loops = len(num_list)

answer = []
for i in range(loops - 1):
    if reversed_list[i] > reversed_list[i + 1]:
        concat_list = reversed_list[:i + 1]
        tmp, idx = N + 1, 0
        for j in range(len(concat_list)):
            if reversed_list[j] > reversed_list[i + 1]:
                if tmp > reversed_list[j]:
                    tmp = reversed_list[j]
                    idx = j
        concat_list[idx] = reversed_list[i + 1]
        concat_list.sort()
        answer = num_list[:N - i - 2] + [tmp] + concat_list
        break

if answer:
    print(*answer)
else:
    print(-1)