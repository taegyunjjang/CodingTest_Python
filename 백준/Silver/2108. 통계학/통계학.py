import sys

input = sys.stdin.readline
N = int(input())

tot = 0
num_list = []
freq_dic = {}

for _ in range(N):
    num = int(input())

    tot += num
    num_list.append(num)

    if num in freq_dic.keys():
        freq_dic[num] += 1
    else:
        freq_dic[num] = 1
num_list.sort()
sorted_dic = sorted(freq_dic.items(), key=lambda x: -x[1])
max_value = sorted_dic[0][1]
duplicates = [key for key, value in freq_dic.items() if value == max_value]
duplicates.sort()

print(round(tot/N))
print(num_list[N//2])
print(duplicates[1] if len(duplicates) != 1 else duplicates[0])
print(num_list[-1] - num_list[0])