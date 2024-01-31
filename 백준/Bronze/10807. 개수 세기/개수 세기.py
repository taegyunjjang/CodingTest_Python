import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(num_list.count(v))