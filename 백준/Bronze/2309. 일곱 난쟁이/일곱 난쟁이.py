import sys

num_list = []
is_stop = False

for _ in range(9):
    num_list.append(int(sys.stdin.readline().strip()))

for i in range(8):
    if is_stop:
        break
    for j in range(i + 1, 9):
        if sum(num_list[:i]) + sum(num_list[i + 1:j]) + sum(num_list[j + 1:]) == 100:
            num_list.pop(j)
            num_list.pop(i)
            is_stop = True
            break

num_list.sort()
for num in num_list:
    print(num)
    