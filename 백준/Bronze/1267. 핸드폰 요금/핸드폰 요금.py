import sys

N = int(sys.stdin.readline())

call_time_list = list(map(int, sys.stdin.readline().split()))

Y_list, M_list = [], []
for call_time in call_time_list:
    Y_list.append(call_time // 30 * 10 + 10)
    M_list.append(call_time // 60 * 15 + 15)

Y_sum, M_sum = sum(Y_list), sum(M_list)
if Y_sum == M_sum:
    print(f"Y M {Y_sum}")
elif Y_sum < M_sum:
    print(f"Y {Y_sum}")
else:
    print(f"M {M_sum}")