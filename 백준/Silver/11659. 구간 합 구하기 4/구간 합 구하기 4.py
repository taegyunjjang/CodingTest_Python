import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

accumulation_list = [0 for _ in range(N)]
for i, num in enumerate(num_list):
    if i == 0:
        accumulation_list[0] = num
    else:
       accumulation_list[i] = accumulation_list[i - 1] + num 

section_list = []
for _ in range(M):
    section_list.append(list(map(int, sys.stdin.readline().split())))

for section in section_list:
    i, j = section
    if i == 1:
        print(accumulation_list[j - 1])
    else:    
        print(accumulation_list[j - 1] - accumulation_list[i - 2])
    
    